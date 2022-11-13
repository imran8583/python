from tkinter import *
import pyperclip
import random
import string 


root = Tk()

# setting the width and height of the GUI
root.geometry("600x400")

# variable of string type to store the password generated
passstr = StringVar()

# variable of integer type to store length of the password entered by the user
passlen = IntVar()

# setting the length of the password to zero initially
passlen.set(0)

# function to generate the password
def generate():

    # alphabetical letters to generate password from
    pass1 = list(string.ascii_lowercase + string.ascii_uppercase + string.punctuation)

    password = ""

    # loop to generate the random password of the length entered by the user
    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    # setting the password to the entry widget
    passstr.set(password)

# function to copy the password to the clipboard
def copytoclipboard():
    random_password = passstr.get()
    pyperclip.copy(random_password)

# Creating a text label widget
Label(root, text="Password Generator Application", font="calibri 20 bold").pack()

# Creating a text label widget
Label(root, text="Enter password length").pack(pady=9)

# Creating a entry widget to take password length entered by the user
Entry(root, textvariable=passlen).pack(pady=3)

# button to call the generate function to generate password
Button(root, text="Generate Password", command=generate).pack(pady=7)

# entry widget to show the generated password
Entry(root, textvariable=passstr).pack(pady=3)

# button to call the copytoclipboard function to copy password
Button(root, text="Copy to clipboard", command=copytoclipboard).pack()

# mainloop() is an infinite loop used to run the application when 
# it's in ready state 
root.mainloop()
