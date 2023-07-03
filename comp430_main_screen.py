
import tkinter as tk
import log_in_screen
import sign_in_screen
import sys

def on_closing():
    sys.exit()
    
def main():
    root = tk.Tk()
    root.geometry("600x400")


    # Create the main window

    root.title("Welcome to Missing Keys Project")
    def x():
        root.withdraw()
        log_in_screen.create_log_in_screen()


    def y():
        root.withdraw()
        sign_in_screen.create_sign_in_screen()


    # Create the button
    login_button = tk.Button(root, text="Open login window", command=x)
    login_button.pack()


    sign_in_button = tk.Button(root, text="Open sign in window", command=y)
    sign_in_button.pack()
    # Run the main loop
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

main()




