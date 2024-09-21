# create the login page containing the username and password feilds
# add the login, register and exit buttons

import tkinter as tk
from tkinter import messagebox
from dbconnect import connect_db
from registration import Error

main_home = tk.Tk()
main_home.title("Login Form")
main_home.geometry("400x300")
main_home.resizable(False, False)

# function to exit
def exit():
    main_home.destroy()
    

def login():
    username = userentry.get()
    password = passwordentry.get()
    
    try:
        # Setup connection to db
        db = connect_db()
        if db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM registration WHERE username = %s AND pass = %s', (username, password))
            result = cursor.fetchone()
            
            if result:
                messagebox.showinfo('Login success', 'Welcome {}'.format(username))
            else:
                messagebox.showerror('Login Failed', 'Invalid Username or password')
    except Error as e:
        messagebox.showerror('Database Error', f"Database Connection Failed!! {e}")
    finally:
        db.close()
            
        
username = tk.Label(main_home, text="Please enter username and password to login")
username.grid(row=0, column=0, columnspan=2)

# username and password
username = tk.Label(main_home, text="Username")
username.grid(row=1, column=0)

userentry = tk.Entry(main_home)
userentry.grid(row=1, column=1)

password = tk.Label(main_home, text="password")
password.grid(row=2, column=0)

passwordentry = tk.Entry(main_home)
passwordentry.grid(row=2, column=1)

loginbutton = tk.Button(main_home, text="Login",command=login)
loginbutton.grid(row=3, column=1)

register = tk.Button(main_home, text="Register")
register.grid(row=4, column=1)

exit = tk.Button(main_home, text="Exit",  command=exit)
exit.grid(row=5, column=1)



main_home.mainloop()
