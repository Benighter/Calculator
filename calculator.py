import tkinter as tk
from math import *

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_sqrt():
    expression = entry.get()
    try:
        result = sqrt(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_sin():
    expression = entry.get()
    try:
        result = sin(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_cos():
    expression = entry.get()
    try:
        result = cos(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_tan():
    expression = entry.get()
    try:
        result = tan(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_log():
    expression = entry.get()
    try:
        result = log(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_exp():
    expression = entry.get()
    try:
        result = exp(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_pi():
    entry.insert(tk.END, pi)

def button_e():
    entry.insert(tk.END, e)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the numbers and results
entry = tk.Entry(root, width=30, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=5)

# Create number buttons
buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("0", 4, 0),
]

for button in buttons:
    btn_text, row, col = button
    btn = tk.Button(root, text=btn_text, padx=20, pady=10, command=lambda text=btn_text: button_click(text))
    btn.grid(row=row, column=col)

# Create operator buttons
operators = [
    ("+", 1, 3),
    ("-", 2, 3),
    ("*", 3, 3),
    ("/", 4, 3),
    ("=", 4, 2),
    ("C", 4, 1),
    ("√", 4, 0),
    ("sin", 1, 4),
    ("cos", 2, 4),
    ("tan", 3, 4),
    ("log", 4, 4),
    ("exp", 1, 5),
    ("π", 2, 5),
    ("e", 3, 5),
]

for operator in operators:
    opr_text, row, col = operator
    opr = tk.Button(root, text=opr_text, padx=20, pady=10)
    opr.grid(row=row, column=col)
    if opr_text == "=":
        opr.config(command=button_equal)
    elif opr_text == "C":
        opr.config(command=button_clear)
    elif opr_text == "√":
        opr.config(command=button_sqrt)
    elif opr_text == "sin":
        opr.config(command=button_sin)
    elif opr_text == "cos":
        opr.config(command=button_cos)
    elif opr_text == "tan":
        opr.config(command=button_tan)
    elif opr_text == "log":
        opr.config(command=button_log)
    elif opr_text == "exp":
        opr.config(command=button_exp)
    elif opr_text == "π":
        opr.config(command=button_pi)
    elif opr_text == "e":
        opr.config(command=button_e)
    else:
        opr.config(command=lambda text=opr_text: button_click(text))

# Start the main event loop
root.mainloop()
