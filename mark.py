import tkinter as tk

def on_button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Custom Button Example")

# Create a custom-styled button
custom_button = tk.Button(
    root,
    text="Click me",
    command=on_button_click,
    relief=tk.FLAT,  # No border
    bg="#3498db",    # Background color
    fg="#ffffff",    # Text color
    font=("Helvetica", 12),  # Font
    padx=10,         # Horizontal padding
    pady=5           # Vertical padding
)

# Pack the button into the window
custom_button.pack(pady=20)

# Start the main event loop
root.mainloop()
