from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog, messagebox
import os

class EncryptionUtility:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryptor/Decryptor")

        # File path variable
        self.file_path = tk.StringVar()

        # Key file path
        self.key_file_path = "secret.key"

        # Generate or load the key
        self.load_or_generate_key()

        # Create Fernet cipher object
        self.cipher = Fernet(self.cipher_key)

        # Create UI
        self.create_ui()

    def create_ui(self):
        # File selection
        tk.Label(self.root, text="Select a File:").pack(pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).pack()

        # Encrypt Button
        tk.Button(self.root, text="Encrypt", command=self.encrypt_file).pack(pady=10)

        # Decrypt Button
        tk.Button(self.root, text="Decrypt", command=self.decrypt_file).pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)

    def encrypt_file(self):
        file_path = self.file_path.get()

        if not file_path:
            self.show_error("Please select a file.")
            return

        with open(file_path, 'rb') as file:
            data = file.read()
            encrypted_data = self.cipher.encrypt(data)

        encrypted_file_path = file_path + ".enc"
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        self.show_message(f"File encrypted successfully: {encrypted_file_path}")

    def decrypt_file(self):
        file_path = self.file_path.get()

        if not file_path:
            self.show_error("Please select a file.")
            return

        with open(file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        try:
            decrypted_data = self.cipher.decrypt(encrypted_data)
        except Exception as e:
            self.show_error("Incorrect key or corrupted data. Decryption failed.")
            return

        decrypted_file_path = file_path + "_decrypted"
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        self.show_message(f"File decrypted successfully: {decrypted_file_path}")

    def load_or_generate_key(self):
        if os.path.exists(self.key_file_path):
            # Key exists, load it
            with open(self.key_file_path, 'rb') as key_file:
                self.cipher_key = key_file.read()
        else:
            # Key does not exist, generate and save it
            self.cipher_key = Fernet.generate_key()
            with open(self.key_file_path, 'wb') as key_file:
                key_file.write(self.cipher_key)

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def show_message(self, message):
        messagebox.showinfo("Success", message)

if __name__ == "__main__":
    root = tk.Tk()
    encryption_utility = EncryptionUtility(root)
    root.mainloop()
