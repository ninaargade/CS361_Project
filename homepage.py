from tkinter import *
import time
# import matplotlib.pyplot as plt

root = Tk()
root.title("Astrology Generator")

myTitle = Label(root, text="Welcome to the Astrology Generator!")
myTitle.pack()

def click():

    myLabel = Label(root, text="Direct to New Page")
    myLabel.pack()

button = Button(root, text='Click Here to create an account in 1 minute!')
button.config(command=click)
button.pack()

myLabel1 = Label(root, text="Please enter your birth date to discover your astrological sign!")
myLabel1.pack()
# myLabel1.grid(row=0, column=0)

e = Entry(root, bg='grey')
e.pack()

e.insert(0, "MM/DD/YYYY")

def click1():

    myLabel = Label(root, text="Your Astrological Sign is: " + e.get())
    myLabel.pack()
           

myButton1 = Button(root, text='Enter', padx=0, pady=0, command=click1, bg='blue')
# myButton1.config(command=click)
myButton1.pack()

myLabel2 = Label(root, text="Or discover a random astrological sign!")
myLabel2.pack()
# myLabel2.grid(row=1, column=5)

def click2():

    myLabel = Label(root, text="Your randomized sign is: Aries!")
    myLabel.pack()
           

myButton2 = Button(root, text='Surprise Me!', padx=0, pady=0, command=click2, bg='blue')
# myButton1.config(command=click)
myButton2.pack()

root.mainloop()
