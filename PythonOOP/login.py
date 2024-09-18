# create the login page containing the username and password feilds
# add the login, register and exit buttons

import tkinter as tk


main_home = tk.Tk()
main_home.title("Login Form")
main_home.geometry("400x300")
main_home.resizable(False, False)

# function to exit
def exit():
    main_home.destroy()

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

loginbutton = tk.Button(main_home, text="Login")
loginbutton.grid(row=3, column=1)

register = tk.Button(main_home, text="Register")
register.grid(row=4, column=1)

exit = tk.Button(main_home, text="Exit",  command=exit)
exit.grid(row=5, column=1)



main_home.mainloop()
