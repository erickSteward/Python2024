import tkinter as tk
from tkinter import ttk

def submit_form():
    # Here you can define what happens when the form is submitted.
    print("Form Submitted")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Set the size of the window
root.geometry("700x600")

# Create the form label
label_title = tk.Label(root, text="Registration Form", font=("Arial", 16))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# First Name and Last Name (on the same line)
label_firstname = tk.Label(root, text="First Name:")
label_firstname.grid(row=1, column=0, padx=10, pady=5)
entry_firstname = tk.Entry(root)
entry_firstname.grid(row=1, column=1, padx=10, pady=5)

label_lastname = tk.Label(root, text="Last Name:")
label_lastname.grid(row=1, column=2, padx=10, pady=5)
entry_lastname = tk.Entry(root)
entry_lastname.grid(row=1, column=3, padx=10, pady=5)

# Email
label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Mobile with country code dropdown
label_mobile = tk.Label(root, text="Mobile:")
label_mobile.grid(row=3, column=0, padx=10, pady=5)

# Country Code dropdown
country_code = tk.StringVar(value="+254")
dropdown_country_code = ttk.Combobox(root, textvariable=country_code, values=["+1", "+44", "+91", "+254", "+61"])
dropdown_country_code.grid(row=3, column=1, padx=10, pady=5)

# Mobile entry field
entry_mobile = tk.Entry(root)
entry_mobile.grid(row=3, column=2, columnspan=2, padx=10, pady=5)

# Gender
label_gender = tk.Label(root, text="Gender:")
label_gender.grid(row=4, column=0, padx=10, pady=5)

gender = tk.StringVar()
radio_male = tk.Radiobutton(root, text="Male", variable=gender, value="Male")
radio_male.grid(row=4, column=1, padx=10, pady=5)

radio_female = tk.Radiobutton(root, text="Female", variable=gender, value="Female")
radio_female.grid(row=4, column=2, padx=10, pady=5)

# Date of Birth (Dropdowns for Day, Month, Year)
label_dob = tk.Label(root, text="Date of Birth:")
label_dob.grid(row=5, column=0, padx=10, pady=5)

dob_day = ttk.Combobox(root, values=[str(i) for i in range(1, 32)], width=5)
dob_day.grid(row=5, column=1, padx=10, pady=5)

dob_month = ttk.Combobox(root, values=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], width=5)
dob_month.grid(row=5, column=2, padx=10, pady=5)

dob_year = ttk.Combobox(root, values=[str(i) for i in range(1950, 2025)], width=7)
dob_year.grid(row=5, column=3, padx=10, pady=5)

# Password
label_password = tk.Label(root, text="Password:")
label_password.grid(row=6, column=0, padx=10, pady=5)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=6, column=1, columnspan=3, padx=10, pady=5)

# Confirm Password
label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.grid(row=7, column=0, padx=10, pady=5)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.grid(row=7, column=1, columnspan=3, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=8, column=0, columnspan=4, pady=20)

# Run the main loop
root.mainloop()
