from tkinter import *
import time
import random
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

    sign_learnMore =    {"Capricorn" : "Capricorn is an Earth sign, known to be ambitious and disciplined!",
                        "Aquarius" : "Aquarius is an Air sign, known to be independent and intellectual!",
                        "Pisces" : "Pisces is a Water sign, known to be thoughtful and creative!",
                        "Aries" : "Aries is a Fire sign, known to be passionate and courageous!", 
                        "Taurus" : "Taurus is an Earth sign, known to be stubborn and clever!",
                        "Gemini" : "Gemini is an Air sign, known to be outgoing and curious!",
                        "Cancer" : "Cancer is a Water sign, known to be adaptable and nurturing!",
                        "Leo" : "Leo is a Fire sign, known to be loyal and generous!",
                        "Virgo" : "Virgo is an Earth sign, known to be logical and kind-hearted!",
                        "Libra" : "Libra is an Air sign, known to be charming and balanced!",
                        "Scorpio" : "Scorpio is a Water sign, known to be ambitious and brave!",
                        "Sagittarius" : "Sagittarius is a Fire sign, known to be honest and passionate!"}

    Label(top, text=sign_learnMore[sign[0]]).pack()

    button = Button(top, text='Exit', bg='blue')
    button.config(command=top.destroy)
    button.pack()


def click1():

    top = Toplevel()
    top.title("Your Astrological Sign")
    date = e.get()

    wfile = open("date.txt", "w") 
    wfile.write(date)
    wfile.close()

    time.sleep(3.0)

    rfile = open("sign.txt", "r") 
    global sign
    sign = rfile.readlines()
    rfile.close()
    print(sign)


    Label(top, text="Your Astrological Sign is: " + sign[0]).pack()

    global my_img
    my_img = ImageTk.PhotoImage(Image.open("images/" + sign[0] + ".png"))

    global my_sign
    my_sign = Label(top, image=my_img)
    my_sign.pack()

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

def learnMore2():

    top = Toplevel()
    top.title("Learn More about this sign!")

    sign_learnMore =    {"Capricorn" : "Capricorn is an Earth sign, known to be ambitious and disciplined!",
                        "Aquarius" : "Aquarius is an Air sign, known to be independent and intellectual!",
                        "Pisces" : "Pisces is a Water sign, known to be thoughtful and creative!",
                        "Aries" : "Aries is a Fire sign, known to be passionate and courageous!", 
                        "Taurus" : "Taurus is an Earth sign, known to be stubborn and clever!",
                        "Gemini" : "Gemini is an Air sign, known to be outgoing and curious!",
                        "Cancer" : "Cancer is a Water sign, known to be adaptable and nurturing!",
                        "Leo" : "Leo is a Fire sign, known to be loyal and generous!",
                        "Virgo" : "Virgo is an Earth sign, known to be logical and kind-hearted!",
                        "Libra" : "Libra is an Air sign, known to be charming and balanced!",
                        "Scorpio" : "Scorpio is a Water sign, known to be ambitious and brave!",
                        "Sagittarius" : "Sagittarius is a Fire sign, known to be honest and passionate!"}

    Label(top, text=sign_learnMore[random_sign]).pack()

    button = Button(top, text='Exit', bg='blue')
    button.config(command=top.destroy)
    button.pack()

def click2():

    
    top = Toplevel()
    top.title("Random Astrological Sign")

    random_index = random.randint(0,11)
    random_sign_list = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

    global random_sign 
    random_sign = random_sign_list[random_index]

    Label(top, text="Your Randomized Sign is: " + random_sign).pack()

    global my_random_img
    my_random_img = ImageTk.PhotoImage(Image.open("images/" + random_sign + ".png"))

    global my_random_sign
    my_random_sign = Label(top, image=my_random_img)
    my_random_sign.pack()

    learnMore = Button(top, text='Learn More', padx=0, pady=0, command=learnMore2, bg='blue')
    learnMore.pack()

    button = Button(top, text='Back to main page', bg='blue')
    button.config(command=top.destroy)
    button.pack()

myButton2 = Button(root, text='Surprise Me!', padx=0, pady=0, command=click2, bg='blue')
myButton2.pack()

root.mainloop()
