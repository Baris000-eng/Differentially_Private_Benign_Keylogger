import tkinter as tk
import main_screen

import sys

def on_closing():
    sys.exit()

def create_log_in_screen():
    
    log_in_screen = tk.Tk()
    log_in_screen.geometry("600x400")
    label_uname = tk.Label(log_in_screen, text="Please enter your username below:")
    uname_of_user = tk.Entry(log_in_screen)

    label_password = tk.Label(log_in_screen, text="Please enter your password below:")
    pass_of_user = tk.Entry(log_in_screen, show="*")

    log_in_screen.title("Welcome to Log-In Screen")
    label_uname.pack()
    uname_of_user.pack()

    label_password.pack()
    pass_of_user.pack()

    def log_in_command(fname,uname, passw):
        uname_exist = False
        with open(fname, "r") as f:
            for l in f:
                uname_passw_pair = l.split()
                uname_f = uname_passw_pair[0]
                passw_f = uname_passw_pair[1]
                if uname == uname_f:
                    uname_exist = True
                    if passw_f == passw:
                        print("username and password are correct")
                        log_in_screen.withdraw()
                        main_screen.create_main_screen()
                    else:
                        print("you entered an incorrect password")
        if not uname_exist:
            print("The given username does not exist")
        return False




    sign_to_the_application = tk.Button(log_in_screen, text = "Log in to the system.", command = lambda: log_in_command("aa", uname_of_user.get(), pass_of_user.get()))
    sign_to_the_application.pack()
    log_in_screen.protocol("WM_DELETE_WINDOW", on_closing)
    log_in_screen.mainloop()

    # Show the window
    def show():
        log_in_screen.deiconify()
    
    # Hide the window
    def hide():
        log_in_screen.withdraw()


import comp430_main_screen