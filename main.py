import tkinter
from tkinter import ttk 
import tkinter as tk
from pygame import mixer
from tkinter import PhotoImage
import subprocess
from subprocess import Popen
import webbrowser
import os
class MyApp:
    def __init__(self, root):       
        self.root = root
        root.title("Software Protection Application")
        root.geometry("1366x768")
        root.configure(bg="gray")
        self.create_main_menu()
    def play_click_sound():
        mixer.init()
        mixer.music.load("welcome.wav")  # Replace with the path to your click sound file
        mixer.music.play()
        def __init__(self, root):
         self.root = root
         self.root.title("Click Sound App")
         def on_button_click(self):
             print("")
    play_click_sound()

    def execute_locker_dialog(self):
        try:
            # Assuming the LockerDialog.exe is in the EXELocker folder
            locker_dialog_path = os.path.join("EXELocker", "LockerDialog.exe")
            subprocess.run([locker_dialog_path])
        except Exception as e:
            print(f"Error: {e}")
    def execute_scan_dialog(self):
        try:
            # Assuming the LockerDialog.exe is in the EXELocker folder
            locker_dialog_path = os.path.join("scan", "SpyCore.exe")
            subprocess.run([locker_dialog_path])
        except Exception as e:
            print(f"Error: {e}")
 
# this is main page the menuw page Some pages in this Software used multiple times to 
# Save Time Thank you 
    def create_main_menu(self):
        self.clear_screen()
         # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        self.title_label = tk.Label(self.root, text="Welcome", font=("Helvetica", 24), bg="blue", fg="black")
        self.title_label.pack(pady=60)

        self.protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page)
        self.protect_button.pack(pady=10)

        self.help_pagea = ttk.Button(self.root, text="Help", command=self.open_help)
        self.help_pagea.pack(pady=10)

        self.help_pageb = ttk.Button(self.root, text="Bug Report", command=lambda: Popen(["python","bug.pak"]))
        self.help_pageb.pack(pady=10)

        self.about_button = ttk.Button(self.root, text="About Us", command=self.open_about_page)
        self.about_button.pack(pady=10)

        self.visit_button = ttk.Button(self.root, text="Donate", command=self.bug_page)
        self.visit_button.pack(pady=10)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy)
        self.exit_button.pack(pady=10)



# The Protect Page 
    def open_protect_page(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        title_label = tk.Label(self.root, text="Protect Piracy Page", font=("Helvetica", 14), bg="yellow", fg="black")
        title_label.pack(pady=(100, 50))  # Adjust the pady values to control vertical spacing

        register_button = ttk.Button(self.root, text="Register Software", command=self.open_link)
        register_button.pack(pady=10)

        lock_button = ttk.Button(self.root, text="Lock Your EXE", command=self.execute_locker_dialog)
        lock_button.pack(pady=10)

        lock_button = ttk.Button(self.root, text="Scan Your EXE", command=self.execute_scan_dialog)
        lock_button.pack(pady=10)

        encrypt_button = ttk.Button(self.root, text="Encrypt-Decrypt", command=lambda: Popen(["python", "enc.pak"]))
        encrypt_button.pack(pady=10)

        lock_button = ttk.Button(self.root, text="Pack into Zip File", command=lambda: Popen(["python", "packer.pak"]))
        lock_button.pack(pady=10)

        encrypt_button = ttk.Button(self.root, text="Backup Folder", command=lambda: Popen(["python", "back.pak"]))
        encrypt_button.pack(pady=10)

        back_button = ttk.Button(self.root, text="Back To Main Menu", command=self.create_main_menu)
        back_button.pack(pady=10)
# The Help Page
    def open_help(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        
        title_label = tk.Label(self.root, text="Help Page", font=("Helvetica", 24), bg="blue", fg="black")
        title_label.pack(pady=20)
        

        about_text = "Register Button will Lead you to register website Of USA gov\n"\
                     "You can Create Account and Register The Product Directly\n"\
                     "________________________________________________________________\n"\
                     "Exe Locker is a powerful tool that enables you to secure your executable files effectively\n"\
                     "It provides a reliable mechanism to lock and restrict access to specific .exe files\n"\
                     "Just Click On Browse-Chose Exe-Enter Pasword And Click Lock Done\n"\
                     "To Unlock Click On your Locked EXE And enter Pasword Done\n"\
                     "_________________________________________________________________\n"\
                     "Scan Your EXE Option Will Scan Your App From Any Dangerous and Harmfull Virus\n"\
                     "First Go To website VirusTool and Sign in then Copy Your API KeY From API In Profile Section\n"\
                     "Then Go Back To App Go to Setting Icon and Paste Your API Key in API Section Done\n"\
                     "Now Go To MAIN And Select EXE File And Click Scan \n"\
                     "_________________________________________________________________\n"\
                     "Pack-Will Lead you to Ziping File In which\n"\
                     "First You Have To Browse The App or File Then you Have To click Pack \n"\
                     "And after Clicking Pack You can also unpack it by Unpack Button \n Or you can Extract\n"\
                     "The File Later By 7Z Archiver Or Winrar\n"\
                     "_________________________________________________________________\n"\
                     "Encrypt-Decrypt-Can Help You to encrypt and Decrypt file \n"\
                     "First You Have To Click Browse then Click Encrypt Done\n"\
                     "Now You can Decrypt it Anytime You want \n"\
                     "Just Browse Again and Click Decrypt Done\n"\
                     "________________________________________________________________________________\n"\
                     "Backup-This Feature can be use for creating extra copy of you software\n"\
                     "Just select the folder and then destination Done\n"\
                     "Your Data Will be copied\n"\

        about_label = tk.Label(self.root, text=about_text, font=("Helvetica", 12), bg="white", fg="black")
        about_label.pack()

        back_button = ttk.Button(self.root, text="Back To Main Menu", command=self.create_main_menu)
        back_button.pack()
# The Report Bug Page
    def bug_page(self):
        self.clear_screen()
        # Load the image
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        title_label = ttk.Label(self.root, text="Donate Us")
        title_label.pack(pady=20)

        register_button = ttk.Button(self.root, text="IBNS", command=self.open_linke)
        register_button.pack()

        global email_label
        email_label = tk.Label(self.root, text="", font=("Helvetica", 10), fg="black")
        email_label.pack()

        back_button = ttk.Button(self.root, text="Back To Main Menu", command=self.create_main_menu)
        back_button.pack()
# The about Page
    def open_about_page(self):
        self.clear_screen()
        img_path = "img.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        title_label = tk.Label(self.root, text="About Us Page", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack(pady=20)

        about_text = "You Can Contact US \n"\
            "Abdul Ahad: gokuahad11@gmail.com \n"\
            "Syed Zafran Haider: zraaeae@gmail.com\n"\
            "Huzaifa Iftikhar: Ph# +92 323 9583860 "
        
        about_label = tk.Label(self.root, text=about_text, font=("Helvetica", 10), bg="white", fg="black")
        about_label.pack()

        back_button = tk.Button(self.root, text="Back To Main Menu", command=self.create_main_menu, font=("Helvetica", 10), fg="black")
        back_button.pack()
#credits Button here
       # ver_button = tk.Button(self.root, text="Credits", command=self.open_linked, font=("Helvetica", 14), fg="black")
        #ver_button.pack()

        #global ver_b
        #ver_b = tk.Label(self.root, text="", font=("Helvetica", 14), fg="black")
        #ver_b.pack()

        back_button = ttk.Button(about_frame, text="Back To Main Menu", command=lambda: self.create_main_menu())
        back_button.pack()

    def visit_link(self):
        webbrowser.open("https://www.linkedin.com/in/syed-zafran-haider/")

    def open_link(self):
        webbrowser.open("https://eservice.eco.loc.gov/siebel/app/eservice/enu?SWECmd=Start")

    def open_linkec(self):
        webbrowser.open("zraaeae@gmail.com")
#Email Us Button Function
    def open_linke(self):
        email_label.config(text="Syed Zafran Haider IBN: PK40TMFB0000000061821888 \n""Abdul AHad IBN: PK31TMFB0000000062769837\n")

#The version button function
    def open_linked(self):
        ver_b.config(text="Syed Zafran Haider \n Abdul ahad \n Huzaifa Iftikhar \n Students of \n Mirpur university Of Science and Technology ")
    
    def open_packer(self):
        os.system("packer.exe")

    def open_encrypt_decrypt(self):
        os.system("enc.exe")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
