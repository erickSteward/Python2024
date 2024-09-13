import tkinter as tk
def button_click(value):
    current_text = display.get() #tk.END refer to the position after the existing text
    display.delete(0, tk.END)
    display.insert(tk.END, current_text + str(value))
def clear_display():
    display.delete(0, tk.END)
def theme_selector(theme):
    if theme == 'dark':
        root.configure(bg = '#000000')
        display.configure(bg = '#55555', fg = 'fffff')
    elif theme =='light'#finalize from here now

def calculate():
    # exception handling. this ensures that our program executes to the ens
    # and does not crash
    try:
        expression = display.get()
        results = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, results)
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")
        

# Create the main window. you can call it anything, for instance main
# The first window
root = tk.Tk()
root.title('Calculator')
root.geometry("400x500")
root.resizable(False, False) #the window will not be resized
root.configure(bg="#ADD8E6") #set background color of the window
# See if you can define a function to allow users to change their background color for line 26
display = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
display.pack(pady=20, padx=20, fill="both")
buttons = [
    '7', '8', '9,' '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# create a new window over  the current window
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

row = 0
col = 0

for button in buttons:
    action = lambda x=button: button_click(x) if x != "=" and x!="C" else calculate() if x == "=" else clear_display()
    # defines an anonymous function (lambda fuction) with a default argument x set to button.
    # This lambda fuction is used to determine what action to take based on the value of x.
    tk.Button(button_frame, text=button, width=9, height=3, bg="#79E5F2", command=action).grid(row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1
        
# define a function to allow users to use the keyboard instead of clicking on the buttons
root.mainloop()
