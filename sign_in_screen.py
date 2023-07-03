import tkinter as tk
import main_screen
import sys
def on_closing():
    sys.exit()

def create_sign_in_screen():
    new_window = tk.Tk()
    label_uname = tk.Label(new_window, text="Please enter your username below:")
    uname_of_user = tk.Entry(new_window)

    label_password = tk.Label(new_window, text="Please enter your password below:")
    pass_of_user = tk.Entry(new_window, show="*")

    new_window.title("Welcome to Sign-Up Screen")
    label_uname.pack()
    uname_of_user.pack()

    label_password.pack()
    pass_of_user.pack()

    def sign_in_command(fname,uname, passw):
        text_to_write = uname + " " + passw + "\n"
        with open(fname, "a") as f:
            f.write(text_to_write)
        print("done")
        new_window.withdraw()
        main_screen.create_main_screen()


            


    sign_to_the_application = tk.Button(new_window, text = "Sign in to the system.", command = lambda: sign_in_command("aa", uname_of_user.get(), pass_of_user.get()))
    sign_to_the_application.pack()
    new_window.protocol("WM_DELETE_WINDOW", on_closing)
    new_window.mainloop()

    def show():
        new_window.deiconify()
    
    # Hide the window
    def hide():
        new_window.withdraw()
