import tkinter as tk
from tkinter import filedialog, messagebox
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
        # Pack File section
        tk.Label(self.root, text="Select a File to Pack:").pack(pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file_to_pack).pack()

        # Pack Button
        tk.Button(self.root, text="Pack into Zip", command=self.pack_file).pack(pady=10)

        # Unpack File section
        tk.Label(self.root, text="Select a Zip File to Unpack:").pack(pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_zip_to_unpack).pack()

        # Unpack Button
        tk.Button(self.root, text="Unpack Zip", command=self.unpack_zip_file).pack(pady=10)

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
