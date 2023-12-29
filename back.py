import tkinter as tk
from tkinter import filedialog
import shutil
import os

def backup_folder():
    source_folder = filedialog.askdirectory(title="Select Folder to Backup")
    if not source_folder:
        return  # User canceled the folder selection

    destination_folder = filedialog.askdirectory(title="Select Backup Destination")
    if not destination_folder:
        return  # User canceled the destination folder selection

    try:
        # Construct the destination path
        backup_folder_name = os.path.basename(source_folder) + "_backup"
        destination_path = os.path.join(destination_folder, backup_folder_name)

        # Copy the folder
        shutil.copytree(source_folder, destination_path)

        # Display success message
        success_message = f"Backup successful! {source_folder} backed up to {destination_path}"
        tk.messagebox.showinfo("Backup Successful", success_message)
    except Exception as e:
        # Display error message if an exception occurs
        error_message = f"Error during backup: {str(e)}"
        tk.messagebox.showerror("Backup Error", error_message)

# Create the main window
root = tk.Tk()
root.title("Folder Backup Tool")

# Create a button to trigger the backup process
backup_button = tk.Button(root, text="Backup Folder", command=backup_folder)
backup_button.pack(pady=20)

# Start the main loop
root.mainloop()
