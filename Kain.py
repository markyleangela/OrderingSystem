import tkinter as tk
from tkinter import *
from src import Product as p
import sys
import mysql.connector

class Kain(tk.Tk):
    def __init__(self):
        super().__init__()

sys.path.insert(0, './src') #set the path for the other folder

app = Kain()
app.title("Kain")
app.geometry("1000x700")
