import tkinter
from tkinter import ttk 
import tkinter as tk
from pygame import mixer
from tkinter import PhotoImage
import subprocess
from subprocess import Popen
import webbrowser
import os
from PIL import Image, ImageTk
class MyApp:
    def __init__(self, root):       
        self.root = root
        root.title("Software Protection Application")
        root.geometry("1366x768")
        self.root.attributes('-fullscreen', True)
        self.create_main_menu()
    def play_click_sound():
        pass
        mixer.init()
        mixer.music.load("welcome.wav")  # Replace with the path to your click sound file
        mixer.music.play()
        def __init__(self, root):
         self.root = root
         self.root.title("Click Sound App")
         def on_button_click(self):
            print("")
    play_click_sound()
    
    

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
        # Create a transparent image
        transparent_image = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
        transparent_photo = ImageTk.PhotoImage(transparent_image)

        self.title_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 0),
            fg="white",
            bg="blue",
            image=transparent_photo,
        )

        img_path = "img.png"
        self.bg_image = tk.PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        
        self.bg_label.place(relwidth=1, relheight=1)
        self.title_label.image = transparent_photo

        self.title_label.pack(pady=110)
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 13))
        style.configure("Tpad", pady=100)

        style = ttk.Style()

        # Configure TButton style for green background and red border
        style.configure("TButton",
                        
                        foreground="black")
        style.map("TButton",
              background=[("active", "blue")]) # Border style

        self.protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25,)
        self.protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        self.about_button = ttk.Button(self.root, text="About Us", command=self.open_about_page, width=25, style="TButton")
        self.about_button.place(y=440, anchor='w', relx=0, rely=0, x=15)

        self.visit_button = ttk.Button(self.root, text="Donate", command=self.bug_page, width=25, style="TButton")
        self.visit_button.place(y=490, anchor='w', relx=0, rely=0, x=15)

        self.help_pagea = ttk.Button(self.root, text="Help", command=self.open_help, width=25, style="TButton")
        self.help_pagea.place(y=390, anchor='w', relx=0, rely=0, x=15)

        self.help_pageb = ttk.Button(self.root, text="Bug Report", command=lambda: Popen(["python", "bug.pak"]), width=25, style="TButton")
        self.help_pageb.place(y=540, anchor='w', relx=0, rely=0, x=15)

        self.exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy, width=25, style="TButton")
        self.exit_button.place(y=590, anchor='w', relx=0, rely=0, x=15)
# The Protect Page 
    def open_protect_page(self):
        self.clear_screen()
        # Load the image

        title_label = tk.Label(self.root, text="Protect Piracy Page", font=("Helvetica", 14), bg="yellow", fg="black")
        title_label.pack(pady=(100, 50))  # Adjust the pady values to control vertical spacing

        img_path = "p.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        register_button = ttk.Button(self.root, text="Reg-Domain", command=self.open_link, width=14)
        register_button.place(x=300, y=490)

        scan_button = ttk.Button(self.root, text="Scan Your EXE", command=self.execute_scan_dialog, width=14)
        scan_button.place(x=300, y=370)

        encrypt_button = ttk.Button(self.root, text="Encrypt-Decrypt", command=lambda: Popen(["python", "enc.pak"]), width=14)
        encrypt_button.place(x=300, y=330)

        pack_button = ttk.Button(self.root, text="Pack into Zip File", command=lambda: Popen(["python", "packer.pak"]), width=14)
        pack_button.place(x=300, y=410)

        backup_button = ttk.Button(self.root, text="Backup Folder", command=lambda: Popen(["python", "back.pak"]), width=14)
        backup_button.place(x=300, y=450)

        back_button = ttk.Button(self.root,text="<", command=self.create_main_menu, width=0)
        back_button.place(x=250, y=326)

#Toggale Work
        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        about_button = ttk.Button(self.root, text="About Us", command=self.open_about_page, width=25, style="TButton")
        about_button.place(y=440, anchor='w', relx=0, rely=0, x=15)

        visit_button = ttk.Button(self.root, text="Donate", command=self.bug_page, width=25, style="TButton")
        visit_button.place(y=490, anchor='w', relx=0, rely=0, x=15)

        help_pagea = ttk.Button(self.root, text="Help", command=self.open_help, width=25, style="TButton")
        help_pagea.place(y=390, anchor='w', relx=0, rely=0, x=15)

        help_pageb = ttk.Button(self.root, text="Bug Report", command=lambda: Popen(["python", "bug.pak"]), width=25, style="TButton")
        help_pageb.place(y=540, anchor='w', relx=0, rely=0, x=15)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy, width=25, style="TButton")
        exit_button.place(y=590, anchor='w', relx=0, rely=0, x=15)
# The Help Page
    def open_help(self):
        self.clear_screen()
        # Load the image
       
        img_path = "help.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)
        back_button = ttk.Button(self.root,width=0,text="<", command=self.create_main_menu)
        back_button.place(y=376,x=250)
#toggale work
        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        about_button = ttk.Button(self.root, text="About Us", command=self.open_about_page, width=25, style="TButton")
        about_button.place(y=440, anchor='w', relx=0, rely=0, x=15)

        visit_button = ttk.Button(self.root, text="Donate", command=self.bug_page, width=25, style="TButton")
        visit_button.place(y=490, anchor='w', relx=0, rely=0, x=15)

        help_pagea = ttk.Button(self.root, text="Help", command=self.open_help, width=25, style="TButton")
        help_pagea.place(y=390, anchor='w', relx=0, rely=0, x=15)

        help_pageb = ttk.Button(self.root, text="Bug Report", command=lambda: Popen(["python", "bug.pak"]), width=25, style="TButton")
        help_pageb.place(y=540, anchor='w', relx=0, rely=0, x=15)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy, width=25, style="TButton")
        exit_button.place(y=590, anchor='w', relx=0, rely=0, x=15)
# The Report Bug Page
    def bug_page(self):
        self.clear_screen()
        # Load the image

        title_label = ttk.Label(self.root, text="Donate Us")
        title_label.pack(pady=20)
        img_path = "don.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        about_text = "Syed Zafran Haider IBN: PK40TMFB0000000061821888 \n\n""Abdul AHad IBN: PK31TMFB0000000062769837\n"

        about_label = tk.Label(self.root,text=about_text, font=("Helvetica", 12), bg="black", fg="white", anchor="center", justify="center")
        about_label.place(x=526,y=330)
        
        back_button = ttk.Button(self.root, text="<",width=0, command=self.create_main_menu)
        back_button.place(y=476,x=250)
#Toggle work
        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        about_button = ttk.Button(self.root, text="About Us", command=self.open_about_page, width=25, style="TButton")
        about_button.place(y=440, anchor='w', relx=0, rely=0, x=15)

        visit_button = ttk.Button(self.root, text="Donate", command=self.bug_page, width=25, style="TButton")
        visit_button.place(y=490, anchor='w', relx=0, rely=0, x=15)

        help_pagea = ttk.Button(self.root, text="Help", command=self.open_help, width=25, style="TButton")
        help_pagea.place(y=390, anchor='w', relx=0, rely=0, x=15)

        help_pageb = ttk.Button(self.root, text="Bug Report", command=lambda: Popen(["python", "bug.pak"]), width=25, style="TButton")
        help_pageb.place(y=540, anchor='w', relx=0, rely=0, x=15)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy, width=25, style="TButton")
        exit_button.place(y=590, anchor='w', relx=0, rely=0, x=15)
# The about Page
    def open_about_page(self):
        

        title_label = tk.Label(self.root, text="About Us Page", font=("Helvetica", 24), bg="green", fg="black")
        title_label.pack(pady=20)
        self.clear_screen()
        img_path = "don.png"
        self.bg_image = PhotoImage(file=img_path)
        # Create a label to display the background image
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)

        about_text = "You Can Contact US \n"\
            "Abdul Ahad: gokuahad11@gmail.com \n"\
            "Syed Zafran Haider: zraaeae@gmail.com\n"\
            "Huzaifa Iftikhar: Ph# +92 323 9583860 "
        
        about_label = tk.Label(self.root, text=about_text, font=("Helvetica", 12), bg="black", fg="white", anchor="center", justify="center")
        about_label.place(x=580,y=320)

        back_button = tk.Button(self.root,text="<", command=self.create_main_menu, font=("Helvetica", 10), fg="black")
        back_button.place(y=427,x=250)
#toggle work
        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        protect_button = ttk.Button(self.root, text="Protect Piracy", command=self.open_protect_page, style="TButton",width=25)
        protect_button.place(y=340, anchor='w', relx=0, rely=0, x=15)

        about_button = ttk.Button(self.root, text="About Us", command=self.open_about_page, width=25, style="TButton")
        about_button.place(y=440, anchor='w', relx=0, rely=0, x=15)

        visit_button = ttk.Button(self.root, text="Donate", command=self.bug_page, width=25, style="TButton")
        visit_button.place(y=490, anchor='w', relx=0, rely=0, x=15)

        help_pagea = ttk.Button(self.root, text="Help", command=self.open_help, width=25, style="TButton")
        help_pagea.place(y=390, anchor='w', relx=0, rely=0, x=15)

        help_pageb = ttk.Button(self.root, text="Bug Report", command=lambda: Popen(["python", "bug.pak"]), width=25, style="TButton")
        help_pageb.place(y=540, anchor='w', relx=0, rely=0, x=15)

        exit_button = ttk.Button(self.root, text="Exit", command=self.root.destroy, width=25, style="TButton")
        exit_button.place(y=590, anchor='w', relx=0, rely=0, x=15)
#credits Button here
       # ver_button = tk.Button(self.root, text="Credits", command=self.open_linked, font=("Helvetica", 14), fg="black")
        #ver_button.pack()

        #global ver_b
        #ver_b = tk.Label(self.root, text="", font=("Helvetica", 14), fg="black")
        #ver_b.pack()

        back_button = ttk.Button(about_frame, text="Back To Main Menu", command=lambda: self.create_main_menu())
        back_button.pack()

    def visit_link(self):
        pass
        webbrowser.open("https://www.linkedin.com/in/syed-zafran-haider/")

    def open_link(self):
        webbrowser.open("https://www.domain.com/domains")

    def open_linkec(self):
        webbrowser.open("zraaeae@gmail.com")
#Email Us Button Function
    def open_linke(self):
        email_label.config(text="Syed Zafran Haider IBN: PK40TMFB0000000061821888 \n""Abdul AHad IBN: PK31TMFB0000000062769837\n")

#The version button function
    def open_linked(self):
        pass
        ver_b = tk.Label(root, text="Syed Zafran Haider \n Abdul ahad \n Huzaifa Iftikhar \n Students of \n Mirpur university Of Science and Technology ")
# Set the position using the place method
        ver_b.place(x=276, y=280)
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
