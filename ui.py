from tkinter import *
import csv_operations


HEIGHT = 600  # Height variable
WIDTH = 100  # Width variable
BUTTON_HEIGHT = 2  # Standard button height
BUTTON_WIDTH = 2  # Standard button width
PAD_X = 5  # Standard padding
PAD_Y = 5
window = Tk()  # Declare the window


def main():
    setup()
    window.mainloop()



def setup():
    """
    Set up and initialize window elements.
    Number, operation, and function buttons (20 total at base)
    """
    password = StringVar()

    window.title("Password Manager")  # Set window title
    # StringVar() is the variable class 
    # we create an instance of this class 
    site = StringVar() 

    # Just a text label to tell the user what the entry box is for
    site_label = Label(text="Site:")
    # The entry box where the user enters the site-password they're looking for
    site_entry = Entry(fg="black", bg="white", width=50)
    password_label = Label(textvariable=password)
    # When enter is pressed, find the password of the site given in the password_label field
    enter_button = Button(window, text='Enter', fg='black', bg='white', 
                     command=lambda: password.set(get_site_pass(site_entry.get())), height=1, width=7) 
    window.configure(bg='lightgray')  # Set window background color

    site_label.pack()
    site_entry.pack()
    password_label.pack()
    enter_button.pack()

    window.configure(width=WIDTH, height=HEIGHT)  # Set window width and height


def get_site_pass(site):
    password = csv_operations.read_password(site)
    return password


if __name__ == '__main__':
    main()
