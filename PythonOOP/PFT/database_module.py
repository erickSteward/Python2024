# import mysql.connector
# from mysql.connector import Error
# from tkinter import messagebox

# class DatabaseConnect():
#     def db_connect():
#         try:
#             return mysql.connector.connect(
#                 host = 'localhost',
#                 user = 'root'
#                 database = 'finance_tracker'
#             )
#         except Error as e:
#             messagebox.showerror("Database Error", f'Database Connection Failed {e}')
#             return None

# database_module.py
import mysql.connector

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,  # Include password here
                database=self.database
            )
            return self.connection
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()


class CRUDOperation:
    def __init__(self, db_connection):
        if db_connection is None:
            raise ValueError("Database connection is not established.")
        self.connection = db_connection

    def create(self, query, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)  # Fixed typo from excute to execute
            self.connection.commit()
            print("Data inserted successfully")
        except mysql.connector.Error as e:
            print(f"Error in CREATE operation: {e}")
        finally:
            cursor.close()

    def read(self, query, data=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, data)
            results = cursor.fetchall()
            return results
        except mysql.connector.Error as e:
            print(f"Error in READ operation: {e}")
            return []
        finally:
            cursor.close()

    def update(self, query, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()
            print("Data updated successfully")
        except mysql.connector.Error as e:
            print(f"Error in UPDATE operation: {e}")
        finally:
            cursor.close()

    def delete(self, query, data):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, data)
            self.connection.commit()
            print("Data deleted successfully")
        except mysql.connector.Error as e:
            print(f"Error in DELETE operation: {e}")
        finally:
            cursor.close()
