import tkinter as tk
from tkinter import *
import sys

import mysql.connector
from mysql.connector import *

import dotenv
import os

dotenv.load_dotenv()

HOST = os.getenv('HOST')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DATABASE = os.getenv('DATABASE')




class LogIn(tk.Tk):
    def __init__(self):
        super().__init__()



def checkUser(username, password):
    try:
        conn = mysql.connector.connect( #CONNECT TO MYSQL
        host = HOST,
        user = USER,
        password = PASSWORD,
        database = DATABASE
    )
        if conn.is_connected():
            print("Connected to MySQL Database");
        
        cursor = conn.cursor()   
        check_query = f"SELECT * FROM users where username = '{username}' and password = '{password}'" 

        cursor.execute(check_query)

        result = cursor.fetchall()
        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error: {e}")

    finally:
        if(result):
            print("Successful")
            return True
        else:
            print("UnSuccessful")
            return False



def display():
    l1.place(x = 120, y = 50, height=30)
    usernameLabel.place(x = 120, y = 150, height=30)
    usernameTextField.place(x = 120, y = 180, height=30, width=250)
    passwordLabel.place(x = 120, y = 210, height=30)
    passwordTextField.place(x = 120, y = 240, height=30, width=250)
    LogInButton.place(x=170, y= 300, height=30, width=150)


def getInfo():
    if(checkUser(usernameTextField.get(), passwordTextField.get())):
        import Kain as kn
        login.withdraw()
        kn.mainloop()
    else:
        errorlabel = Label(text="Incorrect username or password", bg="#FFE8C8", font=('Constantia', 10))
        errorlabel.place(x = 160, y = 350, height= 15)

    


       


login = LogIn()
login.geometry("500x450")
login.configure(bg="#FFE8C8")
login.resizable(False, False)
login.title("Log In")

    
l1 = Label(text="WELCOME TO CHIBOG", anchor=CENTER,font=('Constantia', 20),bg="#FFE8C8")
usernameLabel = Label(text="Username", font=('Constantia', 12),bg="#FFE8C8")
usernameTextField = Entry(login)
passwordLabel = Label(text="Password", font=('Constantia', 12),bg="#FFE8C8")
passwordTextField = Entry(login)
LogInButton = Button(text="LOG IN",font=('Constantia', 10), bg= "#ACD793", command=getInfo)


display()
login.mainloop()











    

