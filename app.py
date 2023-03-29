from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from PIL import ImageTk
import os
import subprocess




bg_Color = "#000000"


def load_frame1():
    frame1.pack_propagate(False)
    #Add your image/logo
    yourImage = ImageTk.PhotoImage(file="NET2.png") #This imports the image
    #This next comand add the image to the Frame Widget
    yourImage_Widget = tk.Label(frame1, image=yourImage, bg=bg_Color)
    yourImage_Widget.image = yourImage # you must assign the image to the label
    yourImage_Widget.pack()

    #Adding text to the logo
    text1 =tk.Label(
    frame1,
    text = "Please chose the program you would like to run: ",
    bg=bg_Color,
    fg="white",
    font=("TkFixedFont", 14),
    ).pack()


    #Adding button Widget
    btn = tk.Button(
    frame1,
    text ="Network Search Tool",
    font =("TkFixedFont", 20),
    bg="black",
    fg="white",
    cursor="hand2",
    activebackground = "white",
    activeforeground = "black",
    command= lambda:newSearhtool()).pack(pady=40)


    #OPTION 2
    btn2 = tk.Button(
    frame1,
    text ="Bitocker Search Tool ",
    font =("TkFixedFont", 20),
    bg="black",
    fg="white",
    cursor="hand2",
    activebackground = "white",
    activeforeground = "black",
    command= lambda:bitLocekr1()).pack(pady= 20)


    #OPTION 3
    btn3 = tk.Button(
    frame1,
    text ="Open System Updates",
    font =("TkFixedFont", 20),
    bg="black",
    fg="white",
    cursor="hand2",
    activebackground = "white",
    activeforeground = "black",
    command= lambda:openSystemUpdtes()).pack(pady=20)


    #OPTION 4
    btn4 = tk.Button(
    frame1,
    text ="Bitlocker Search Tool | In a different domain",
    font =("TkFixedFont", 20),
    bg="black",
    fg="white",
    cursor="hand2",
    activebackground = "white",
    activeforeground = "black",
    command= lambda:bitLocker2()).pack(pady=20)
def load_frame2():
    print("FRAME 2")
def bitLocekr1():
    print("Bitlocker Search Tool")
    subprocess.call([r'C:\Network Search Tool\BITLOCKER RECOVERY.bat'])
def newSearhtool():
    print("Network Search Tool")
    subprocess.call([r'C:\Network Search Tool\Network search tool.bat'])
def openSystemUpdtes():
    print("System Updates")
    subprocess.call([r'C:\Network Search Tool\OPEN SYSTEM UPDATES.bat'])
def bitLocker2():
    print("Bitlocker search tool for devices in different domains")
    subprocess.call([r'C:\Network Search Tool\BITLOCKER.bat'])

#initiallize the app
mainWindow = tk.Tk() #This creates the window, The name can be anything
mainWindow.title("Network Search Tool")

#Sieze and place the app
mainWindow.geometry("1000x900+0+0")
mainWindow.eval("tk::PlaceWindow . center")


#Create the Frame Widgets and ad it to the main window
frame1 = tk.Frame(mainWindow, width=1000, height=900, bg=bg_Color)
frame2 = tk.Frame(mainWindow, width=1000, height=900, bg=bg_Color)
frame1.grid(row=0, column=0)
# for frame in (frame1,frame2):
#     frame.grid(row=0, column=0)

load_frame1()

#comand = lambda:load_frame2()).pack(20)
#This terminiates the window
mainWindow.mainloop()
