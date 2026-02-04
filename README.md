# File-Sort-by-type
A simple Python app for Windows 64x to sort a Folder full of Files (images, music, videos, pdf, etc) into sub folders.
By Alejandro Jiménez Wilhelm
FILE SORTER – README

Description
-----------
This application is a simple file automation tool developed in Python and packaged
as a standalone Windows executable. Its purpose is to help users organize files inside
a selected folder by automatically sorting them into subfolders based on file type
(extension).

The application provides a graphical user interface (GUI) that allows the user to:
- Select a folder from the file system.
- Simulate the sorting process (Dry Run mode).
- Execute the sorting process safely with user confirmation.
- View a log of all actions performed by the program.

No installation of Python or additional software is required to run the executable.


How It Works
------------
1. The user selects a folder using the "Browse" button.
2. The program scans only the files located directly inside the selected folder
   (subfolders are not modified).
3. Files are classified according to their extension (e.g. .pdf, .jpg, .mp3).
4. For each file type, a corresponding subfolder is created if it does not already exist
   (e.g. PDF, IMAGES, AUDIO, DOCS).
5. Files are moved into their corresponding subfolders.
6. If a file with the same name already exists in the destination folder, the program
   automatically renames the file to avoid overwriting.


Safety Features
---------------
- Dry Run Mode:
  When enabled, the program does not move any files. It only displays what actions
  would be performed. This is recommended before running the actual sorting process.

- User Confirmation:
  When Dry Run mode is disabled, the program asks for confirmation before moving files.

- Filename Collision Protection:
  Existing files are never overwritten. New filenames are generated automatically
  when necessary.


Restrictions and Limitations
----------------------------
- This application is designed for Windows operating systems only.
- It should be used only on user-accessible folders such as Desktop, Documents,
  Downloads, or personal project folders.
- It is not recommended to run the program on system directories such as:
  - C:\Windows
  - Program Files
  - Other protected system folders
- The program only processes files in the root of the selected folder.
  Subfolders and their contents are ignored.
- The application does not provide an undo feature. Once files are moved,
  the changes are permanent.


Security Notice
---------------
This executable was created using PyInstaller from a Python script developed for
academic and educational purposes. It does not collect personal data, connect to
the internet, or perform any background operations.

Some antivirus software or Windows SmartScreen may display a warning when running
the application for the first time. This is normal for unsigned executables created
locally.


Author
------
Developed as an academic project to demonstrate basic Python programming,
file system automation, and GUI development.
