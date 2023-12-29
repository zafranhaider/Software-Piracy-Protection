import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import zipfile
import os

class ZipUtilityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zip Utility App")

        # File path variables
        self.file_to_pack_path = tk.StringVar()
        self.zip_to_unpack_path = tk.StringVar()

        # Create UI
        self.create_ui()

    def create_ui(self):
        # Notebook for multiple tabs
        notebook = ttk.Notebook(self.root)
        notebook.pack(padx=10, pady=10, fill='both', expand=True)

        # Pack Tab
        pack_tab = ttk.Frame(notebook)
        notebook.add(pack_tab, text='Pack')

        self.create_pack_tab(pack_tab)

        # Unpack Tab
        unpack_tab = ttk.Frame(notebook)
        notebook.add(unpack_tab, text='Unpack')

        self.create_unpack_tab(unpack_tab)

    def create_pack_tab(self, pack_tab):
        # Pack File section
        ttk.Label(pack_tab, text="Select a File to Pack:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        file_entry = ttk.Entry(pack_tab, textvariable=self.file_to_pack_path, width=40)
        file_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        ttk.Button(pack_tab, text="Browse", command=self.browse_file_to_pack).grid(row=0, column=2, padx=10, pady=10, sticky='w')

        # Pack Button
        ttk.Button(pack_tab, text="Pack into Zip", command=self.pack_file).grid(row=1, column=0, columnspan=3, pady=10)

    def create_unpack_tab(self, unpack_tab):
        # Unpack File section
        ttk.Label(unpack_tab, text="Select a Zip File to Unpack:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
        zip_entry = ttk.Entry(unpack_tab, textvariable=self.zip_to_unpack_path, width=40)
        zip_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')
        ttk.Button(unpack_tab, text="Browse", command=self.browse_zip_to_unpack).grid(row=0, column=2, padx=10, pady=10, sticky='w')

        # Unpack Button
        ttk.Button(unpack_tab, text="Unpack Zip", command=self.unpack_zip_file).grid(row=1, column=0, columnspan=3, pady=10)

    def browse_file_to_pack(self):
        file_to_pack_path = filedialog.askopenfilename()
        self.file_to_pack_path.set(file_to_pack_path)

    def pack_file(self):
        file_to_pack_path = self.file_to_pack_path.get()

        if not file_to_pack_path:
            self.show_error("Please select a file to pack.")
            return

        try:
            with zipfile.ZipFile(file_to_pack_path + ".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_to_pack_path, os.path.basename(file_to_pack_path))

            self.show_message(f"File packed into zip successfully: {file_to_pack_path}.zip")
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")

    def browse_zip_to_unpack(self):
        zip_to_unpack_path = filedialog.askopenfilename(filetypes=[("Zip Files", "*.zip")])
        self.zip_to_unpack_path.set(zip_to_unpack_path)

    def unpack_zip_file(self):
        zip_to_unpack_path = self.zip_to_unpack_path.get()

        if not zip_to_unpack_path:
            self.show_error("Please select a zip file to unpack.")
            return

        try:
            with zipfile.ZipFile(zip_to_unpack_path, 'r') as zipf:
                extract_directory = os.path.splitext(zip_to_unpack_path)[0]
                os.makedirs(extract_directory, exist_ok=True)
                zipf.extractall(extract_directory)

            self.show_message(f"Zip file unpacked successfully to: {extract_directory}")
        except zipfile.BadZipFile:
            self.show_error("Invalid zip file. Please select a valid zip file.")
        except Exception as e:
            self.show_error(f"An error occurred: {str(e)}")

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_message(self, message):
        messagebox.showinfo("Success", message)

if __name__ == "__main__":
    root = tk.Tk()
    app = ZipUtilityApp(root)
    root.mainloop()
