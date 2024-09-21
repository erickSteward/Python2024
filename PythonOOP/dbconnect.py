import tkinter as tk
from tkinter import messagebox
import mysql.connector #this is for connection to the database
from mysql.connector import Error

# set up the database connection
def connect_db():
    # to prevent the system form crashing, embrace exception handling
    # enclose in a try finally block
    try:
        return mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            database = 'retail'
        )
    except Error as e:
        messagebox.showerror('Database Error', f'Database Connection Failed!!: {e}')
        return None


