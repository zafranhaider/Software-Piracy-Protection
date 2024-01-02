import os
import getpass
import tkinter as tk
from tkinter import filedialog

def lock_exe(file_path, password):
    """Locks the specified EXE file by renaming it with a random extension."""
    random_extension = os.urandom(8).hex()
    new_file_path = file_path + "." + random_extension
    os.rename(file_path, new_file_path)
    with open("locked_files.txt", "a") as f:
        f.write(f"{new_file_path} {password}\n")

def unlock_exe(file_path, password):
    """Unlocks the specified EXE file by removing the random extension."""
    with open("locked_files.txt", "r") as f:
        for line in f:
            locked_file, stored_password = line.strip().split(" ")
            if locked_file == file_path and password == stored_password:
                os.rename(locked_file, os.path.splitext(locked_file)[0])
                return True
    return False

class App:
    def __init__(self, master):
        self.master = master
        master.title("EXE File Locker")

        self.label = tk.Label(master, text="Choose an action:")
        self.label.pack()

        self.lock_button = tk.Button(master, text="Lock EXE File", command=self.lock_exe_gui)
        self.lock_button.pack()

        self.unlock_button = tk.Button(master, text="Unlock EXE File", command=self.unlock_exe_gui)
        self.unlock_button.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack()

    def lock_exe_gui(self):
        file_path = filedialog.askopenfilename(title="Select an EXE file to lock", filetypes=[("EXE files", "*.exe")])
        if file_path:
            password = getpass.getpass("Enter a password: ")
            lock_exe(file_path, password)
            tk.messagebox.showinfo("Success", "EXE file locked successfully!")

    def unlock_exe_gui(self):
        file_path = filedialog.askopenfilename(title="Select a locked EXE file", filetypes=[("Locked EXE files", "*.exe.*")])
        if file_path:
            password = getpass.getpass("Enter the password: ")
            if unlock_exe(file_path, password):
                tk.messagebox.showinfo("Success", "EXE file unlocked successfully!")
            else:
                tk.messagebox.showerror("Error", "Incorrect password or file not found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
