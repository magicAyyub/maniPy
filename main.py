from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox

common_file_ext = {
    ".exe": "EXE files",
    ".iso": "ISO files",
    ".msi": "MSI files",
    ".xlsx": "Excel files",
    ".docx": "Word files",
    ".pptx": "PowerPoints files",
    ".pdf": "PDF files",
    ".txt": "Text files",
    ".c": "C files",
    ".html": "HTML files",
    ".php": "PHP files",
    ".js": "JS files",
    ".json": "JSON files",
    ".sql": "SQL files",
    ".png": "Images_",
    ".jpg": "Images_",
    ".jpeg": "Images_",
    ".svg": "Images_",
    ".zip": "ZIP files"
}

root = tk.Tk()
root.withdraw()

path = filedialog.askdirectory(title="Sélectionnez le dossier à néttoyer", initialdir=Path.home())

if not path:
    messagebox.showinfo("Nettoyage annulé", "Opération de nettoyage annulée.", icon="warning")
    exit()

folder_to_clean = Path(path)
files_in_folder = [element for element in folder_to_clean.iterdir() if element.is_file()]

for file in files_in_folder:
    output_dir = folder_to_clean / common_file_ext.get(file.suffix, "Others")
    output_dir.mkdir(exist_ok=True)
    file.rename(output_dir / file.name)

messagebox.showinfo("Nettoyage terminé",
                    "L'opération de nettoyage s'est achevée avec succès. Vos fichiers ont été organisés.",
                    icon="info")
