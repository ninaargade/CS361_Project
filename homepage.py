from tkinter import *
import time
# import matplotlib.pyplot as plt
from PIL import ImageTk, Image

root = Tk()
root.title("Astrology Generator")

myTitle = Label(root, text="Welcome to the Astrology Generator!")
myTitle.pack()

def click():

    top = Toplevel()
    top.title("Create Account")
    Label(top, text="Fill out the form below to create a new account!").pack()

    e = Entry(top, bg='grey')
    e.insert(0, "First Name")
    e.pack()

    e = Entry(top, text='Last Name: ', bg='grey')
    e.insert(0, "Last Name")
    e.pack()

    e = Entry(top, text="Birth Date: ", bg='grey')
    e.insert(0, "MM/DD/YYYY")
    e.pack()

    button = Button(top, text='Submit', bg='blue')
    button.config(command=top.destroy)
    button.pack()

button = Button(root, text='Click Here to create an account in 1 minute!')
button.config(command=click)
button.pack()

myLabel1 = Label(root, text="Please enter your birth date to discover your astrological sign!")
myLabel1.pack()
# myLabel1.grid(row=0, column=0)

global e
e = Entry(root, bg='grey')
e.pack()
e.insert(0, "MM/DD/YYYY")

def learnMore1():

    top = Toplevel()
    top.title("Learn More about your sign!")
    Label(top, text="Learn More about your sign!").pack()

    button = Button(top, text='Exit', bg='blue')
    button.config(command=top.destroy)
    button.pack()


def click1():

    global my_img
    my_img = ImageTk.PhotoImage(Image.open("images/Taurus.png"))

    top = Toplevel()
    top.title("Your Astrological Sign")
    sign = e.get()
    Label(top, text="Your Astrological Sign is: " + sign).pack()

    global my_sign
    my_sign = Label(top, image=my_img)
    my_sign.pack()

    myDescription = Label(top, text="Description: -------------------")
    myDescription.pack()

    learnMore = Button(top, text='Learn More', padx=0, pady=0, command=learnMore1, bg='blue')
    learnMore.pack()

    button = Button(top, text='Back to main page', bg='blue')
    button.config(command=top.destroy)
    button.pack()

    e.delete(0, END)
    e.insert(0, "MM/DD/YYYY")
           

myButton1 = Button(root, text='Enter', padx=0, pady=0, command=click1, bg='blue')
myButton1.pack()

myLabel2 = Label(root, text="Or discover a random astrological sign!")
myLabel2.pack()
# myLabel2.grid(row=1, column=5)

def learnMore2():

    top = Toplevel()
    top.title("Learn More about this sign!")
    Label(top, text="Learn More about this sign!").pack()

    button = Button(top, text='Exit', bg='blue')
    button.config(command=top.destroy)
    button.pack()

def click2():

    global my_random_img
    my_random_img = ImageTk.PhotoImage(Image.open("images/Aries.png"))

    
    top = Toplevel()
    top.title("Random Astrological Sign")
    Label(top, text="Your Randomized Sign is: Aries").pack()

    global my_random_sign
    my_random_sign = Label(top, image=my_random_img)
    my_random_sign.pack()

    myDescription = Label(top, text="Description: -------------------")
    myDescription.pack()

    
    learnMore = Button(top, text='Learn More', padx=0, pady=0, command=learnMore2, bg='blue')
    learnMore.pack()

    button = Button(top, text='Back to main page', bg='blue')
    button.config(command=top.destroy)
    button.pack()

myButton2 = Button(root, text='Surprise Me!', padx=0, pady=0, command=click2, bg='blue')
myButton2.pack()

root.mainloop()
