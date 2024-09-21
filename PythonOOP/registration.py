import tkinter as tk
from tkinter import messagebox
from mysql.connector import Error
from dbconnect import connect_db
from validate_email import validate_email
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar


# define the function to register the user
def register_user():
    user = userentry.get()
    fName = fnameentry.get()
    sName = snameentry.get()
    password = passentry.get()
    repassword = repassentry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    dob = dob_entry.get_date()  # Fetch the selected date of birth from DateEntry

    if repassword != password:
        messagebox.showerror('Password Error', 'Password Mismatch')
    elif len(password) < 6:
        messagebox.showerror("Password Error", "Password too short (minimum 6 characters)")
    
    # Validate email
    elif validate_email(email) == False:
        messagebox.showinfo("Invalid Email", "Please check email and try again")
    else:
        try:
            db = connect_db()
            # use the cursor class to execute sql code
            cursor = db.cursor()  # use the cursor class to execute our sql code
            sql = "INSERT INTO registration (username, fname, surname, pass, phone, email, dob) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (user, fName, sName, password, phone, email, dob)
            cursor.execute(sql, val)
            db.commit()
            result = messagebox.askquestion('Registration Successful', 'Add Another Record?')
            if result == 'no':
                main_home.destroy()
            else:
                fnameentry.delete(0, tk.END)
                snameentry.delete(0, tk.END)
                passentry.delete(0, tk.END)
                repassentry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                
        except Error as e:
            messagebox.showerror('Database Error', f'Data Could not be saved')
            cursor.close()
        finally:
            db.close()

main_home = tk.Tk()
main_home.title("Registration Form")
main_home.geometry('400x400')
main_home.resizable(False, False)

# username (label) and userentry(textbox) widgets
username = tk.Label(main_home, text="Username")
username.grid(row=0, column=0)

userentry = tk.Entry(main_home)
userentry.grid(row=0, column=1)

# firstname label and textbox
fname = tk.Label(main_home, text="First Name")
fname.grid(row=1, column=0)

fnameentry = tk.Entry(main_home)
fnameentry.grid(row=1, column=1)

# surname label and textbox
sname = tk.Label(main_home, text="Surname")
sname.grid(row=2, column=0)

snameentry = tk.Entry(main_home)
snameentry.grid(row=2, column=1)

# password
password = tk.Label(main_home, text="Password")
password.grid(row=3, column=0)

passentry = tk.Entry(main_home, show="*")
passentry.grid(row=3, column=1)

# password confirmation
repassword = tk.Label(main_home, text="Retype Password")
repassword.grid(row=4, column=0)

repassentry = tk.Entry(main_home, show="*")
repassentry.grid(row=4, column=1)

# phone number
phone = tk.Label(main_home, text="Phone Number")
phone.grid(row=5, column=0)

phone_entry = tk.Entry(main_home)
phone_entry.grid(row=5, column=1)

# email
email = tk.Label(main_home, text="Email")
email.grid(row=6, column=0)

email_entry = tk.Entry(main_home)
email_entry.grid(row=6, column=1)

# Date of Birth (DOB) using tkcalendar DateEntry
dob_label = tk.Label(main_home, text="Date of Birth")
dob_label.grid(row=7, column=0)

dob_entry = DateEntry(main_home, width=15, background='darkblue', foreground='white', borderwidth=2, year=2000, date_pattern='y-mm-dd')
dob_entry.grid(row=7, column=1)

# Buttons for login, register, and exit
login = tk.Button(main_home, text="Login")
login.grid(row=9, column=0)

register = tk.Button(main_home, text="Register", command=register_user)
register.grid(row=9, column=1)

exit = tk.Button(main_home, text="Exit", command=exit)
exit.grid(row=9, column=2)

main_home.mainloop()
