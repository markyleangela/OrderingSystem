import tkinter as tk
from tkinter import *
import Product as p
import sys
import mysql.connector
import PIL as pl
from PIL import Image, ImageTk


class Kain(tk.Tk):
    def __init__(self):
        super().__init__()

sys.path.insert(0, './src') #set the path for the other folder

app = Kain()
app.title("Kain")
app.geometry("1000x700")
app.resizable(False, False)
app.configure(bg="#FFE8C8")




user = "default"
greeting = Label(text=f"Hi! {user}",anchor=CENTER,font=('Constantia', 12), bg="#FFE8C8")
#main frame of the menu
frame = Frame(app, bg="#FFC96F")
frame.place(x=20, y=70, height=500, width=500)
#
my_canvas = Canvas(frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

#scroll bar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=my_canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


menu = [p.Product("Burger", 75.00, 1, "Sliders", PhotoImage(file='./assets/images/Burger.png')), p.Product("Fries", 55.00, 1, "Fries", PhotoImage(file='./assets/images/Fries.png'))]



def my_command():
    print(f"button clicked")

def display():
    greeting.place(x=20, y=10, height=50)
    
    for btn in range(len(menu)):
        
        Button(second_frame, text=f"Button {btn}", image= menu[btn].getImage() ,command= my_command).grid(row=btn, column=0, padx=10, pady=10)
        


   

display()
app.mainloop()



