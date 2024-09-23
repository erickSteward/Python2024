# main.py
import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from database_module import DatabaseConnection, CRUDOperation
from transaction_module import Transaction, TransactionManager
from reporting_module import ReportGenerator

# Database setup
db_conn = DatabaseConnection(host="localhost", user="root", password='', database="finance_tracker")
connection = db_conn.connect()
crud_operation = CRUDOperation(connection)

transaction_manager = TransactionManager(crud_operation)
report_generator = ReportGenerator(crud_operation)

def add_transaction():
    date = entry_date.get_date().strftime("%Y-%m-%d")
    type = entry_type.get()
    category = entry_category.get()
    amount = entry_amount.get()
    description = entry_description.get()

    if not all([date, type, category, amount]):
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")
        return
    
    transaction = Transaction(None, date, type, category, amount, description)
    transaction_manager.add_transaction(transaction)
    messagebox.showinfo("Success", "Transaction added successfully")
    clear_entries()

def clear_entries():
    entry_date.set_date(datetime.date.today())  # Set to today's date
    entry_type.set('')
    entry_category.set('')
    entry_amount.delete(0, tk.END)
    entry_description.delete(0, tk.END)

def show_report():
    report = report_generator.generate_summary_report()
    formatted_report = "\n".join([f"{row['type']}: {row['total_amount']}" for row in report])
    messagebox.showinfo("Summary Report", formatted_report)

# Initialize the main application window
app = tk.Tk()
app.title("Personal Finance Tracker")

# Set the geometry size
window_width = 400
window_height = 400

# Get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# calculate x and y coodinates for the TK root window
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

# Set the geometry of the widow
app.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

# Configure the grid layout
app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

frame = ttk.Frame(app, padding="10 10 10 10")
frame.grid(row=0, column=0, sticky="NSEW")

frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

# Create and place widgets using grid
tk.Label(app, text="Date:").grid(row=0, column=0, padx=5, pady=5)
entry_date = DateEntry(app, width=12, background='darkblue', foreground='white', year=2024)
entry_date.grid(row=0, column=1, padx=0, pady=0)

tk.Label(app, text="Type (Income/Expense):").grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
entry_type = ttk.Combobox(app, values=["Income", "Expense"], state="readonly")
entry_type.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

tk.Label(app, text="Category:").grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)
category_options = ["Salary", "Business", "Investments", "Groceries", "Bills", "Rent", "Entertainment", "Miscellaneous"]
entry_category = ttk.Combobox(app, values=category_options, state="readonly")
entry_category.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

tk.Label(app, text="Amount:").grid(row=3, column=0, sticky=tk.E, padx=5, pady=5)
entry_amount = tk.Entry(app)
entry_amount.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

tk.Label(app, text="Description:").grid(row=4, column=0, sticky=tk.E, padx=5, pady=5)
entry_description = tk.Entry(app)
entry_description.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

tk.Button(app, text="Add Transaction", command=add_transaction).grid(row=5, column=0, padx=5, pady=10, columnspan=2)
tk.Button(app, text="Show Report", command=show_report).grid(row=6, column=0, padx=5, pady=10, columnspan=2)

# Run the application
app.mainloop()
