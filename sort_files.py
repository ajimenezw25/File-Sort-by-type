#----------------------------------------------------------
#Sort de tipos de archivos en carpetas según su extensión
#Alejandro Jiménez Wilhelm
#----------------------------------------------------------

from pathlib import Path
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

# Archivos por categoría
CATEGORIES = {
    "PDF": {".pdf"},
    "IMAGES": {".jpg", ".jpeg", ".png", ".gif", ".webp"},
    "DOCS": {".doc", ".docx", ".txt", ".rtf"},
    "SHEETS": {".xls", ".xlsx", ".csv"},
    "PRESENTATIONS": {".ppt", ".pptx"},
    "VIDEOS": {".mp4", ".mov", ".avi", ".mkv"},
    "AUDIO": {".mp3", ".wav", ".m4a"},
    "ZIP": {".zip", ".rar", ".7z"},
    "CODE": {".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".sql"},
}

def get_category(ext: str) -> str:
    ext = ext.lower()
    for category, exts in CATEGORIES.items():
        if ext in exts:
            return category
    return "OTHER"

def unique_path(path: Path) -> Path:
    """Evita sobrescribir si ya existe el archivo destino."""
    if not path.exists():
        return path
    stem, suffix = path.stem, path.suffix
    parent = path.parent
    i = 1
    while True:
        candidate = parent / f"{stem}_{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def sort_folder(folder: Path, dry_run: bool, log_fn):
    if not folder.exists():
        raise FileNotFoundError(f"La carpeta no existe: {folder}")

    moved = 0
    for item in folder.iterdir():
        if item.is_file():
            category = get_category(item.suffix)
            dest_dir = folder / category
            dest_dir.mkdir(exist_ok=True)

            dest_path = unique_path(dest_dir / item.name)

            if dry_run:
                log_fn(f"[DRY RUN] {item.name} -> {category}/")
            else:
                shutil.move(str(item), str(dest_path))
                log_fn(f"Moved: {item.name} -> {category}/")
                moved += 1

    log_fn(f"\nListo. Archivos movidos: {moved}" if not dry_run else "\nListo (simulación). No se movió nada.")

# ---------------- UI ----------------

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Sorter (Python)")
        self.geometry("720x520")

        self.selected_path = tk.StringVar(value="")
        self.dry_run = tk.BooleanVar(value=True)

        
        top = tk.Frame(self)
        top.pack(fill="x", padx=12, pady=10)

        tk.Label(top, text="Folder:").pack(side="left")
        self.path_entry = tk.Entry(top, textvariable=self.selected_path)
        self.path_entry.pack(side="left", fill="x", expand=True, padx=8)

        tk.Button(top, text="Browse...", command=self.browse).pack(side="left")

        opts = tk.Frame(self)
        opts.pack(fill="x", padx=12)

        tk.Checkbutton(
            opts,
            text="Dry run (solo simula, no mueve archivos)",
            variable=self.dry_run
        ).pack(side="left")

        btns = tk.Frame(self)
        btns.pack(fill="x", padx=12, pady=10)

        tk.Button(btns, text="Sort", command=self.run_sort).pack(side="left")
        tk.Button(btns, text="Clear log", command=self.clear_log).pack(side="left", padx=8)

        self.log = scrolledtext.ScrolledText(self, wrap="word")
        self.log.pack(fill="both", expand=True, padx=12, pady=10)

        self.write_log("Elegí una carpeta con Browse... (Recomendado: primero Dry run).")

    def browse(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_path.set(folder)
            self.write_log(f"\nSeleccionado: {folder}")

    def write_log(self, msg: str):
        self.log.insert("end", msg + "\n")
        self.log.see("end")

    def clear_log(self):
        self.log.delete("1.0", "end")

    def run_sort(self):
        folder_str = self.selected_path.get().strip()
        if not folder_str:
            messagebox.showwarning("Falta carpeta", "Seleccioná una carpeta primero.")
            return

        folder = Path(folder_str)

        # Confirmación si NO es dry run 
        if not self.dry_run.get():
            ok = messagebox.askyesno(
                "Confirmar",
                "Esto moverá archivos de verdad.\n¿Querés continuar?"
            )
            if not ok:
                self.write_log("Cancelado.")
                return

        self.write_log("\n--- Ejecutando ---")
        try:
            sort_folder(folder, self.dry_run.get(), self.write_log)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.write_log(f"ERROR: {e}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
