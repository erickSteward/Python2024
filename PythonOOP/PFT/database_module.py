import mysql.connector
from mysql.connector import Error
from tkinter import messagebox

class DatabaseConnect():
    def db_connect():
        try:
            return mysql.connector.connect(
                host = 'localhost',
                user = 'root'
                database = 'finance_tracker'
            )
        except Error as e:
            messagebox.showerror("Database Error", f'Database Connection Failed {e}')
            return None