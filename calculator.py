

import tkinter as tk

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=15, font=('Arial', 20), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

first_num = None
operator = None

def click_num(num):
    entry.insert(tk.END, str(num))

def click_op(op):
    global first_num, operator
    first_num= float(entry.get())
    operator = op
    entry.delete(0, tk.END)

def calculate():
    global first_num, operator
    second_num= float(entry.get())
    result = 0

    if operator == '+':
        result = first_num + second_num
    elif operator == '-':
        result = first_num - second_num
    elif operator == '*':
        result = first_num * second_num
    elif operator == '/':
        if second_num!= 0:
            result = first_num/ second_num
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
            return

    entry.delete(0, tk.END)
    entry.insert(tk.END, str(result))

def clear():
    entry.delete(0, tk.END)

#Row 1
tk.Button(root, text='7', width=5, height=2, command=lambda: click_num(7)).grid(row=1, column=0, padx=5, pady=5)
tk.Button(root, text='8', width=5, height=2, command=lambda: click_num(8)).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text='9', width=5, height=2, command=lambda: click_num(9)).grid(row=1, column=2, padx=5, pady=5)
tk.Button(root, text='/', width=5, height=2, command=lambda: click_op('/')).grid(row=1, column=3, padx=5, pady=5)

#Row 2
tk.Button(root, text='4', width=5, height=2, command=lambda: click_num(4)).grid(row=2, column=0, padx=5, pady=5)
tk.Button(root, text='5', width=5, height=2, command=lambda: click_num(5)).grid(row=2, column=1, padx=5, pady=5)
tk.Button(root, text='6', width=5, height=2, command=lambda: click_num(6)).grid(row=2, column=2, padx=5, pady=5)
tk.Button(root, text='*', width=5, height=2, command=lambda: click_op('*')).grid(row=2, column=3, padx=5, pady=5)

#Row 3
tk.Button(root, text='1', width=5, height=2, command=lambda: click_num(1)).grid(row=3, column=0, padx=5, pady=5)
tk.Button(root, text='2', width=5, height=2, command=lambda: click_num(2)).grid(row=3, column=1, padx=5, pady=5)
tk.Button(root, text='3', width=5, height=2, command=lambda: click_num(3)).grid(row=3, column=2, padx=5, pady=5)
tk.Button(root, text='-', width=5, height=2, command=lambda: click_op('-')).grid(row=3, column=3, padx=5, pady=5)

#Row 4
tk.Button(root, text='0', width=5, height=2, command=lambda: click_num(0)).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text='C', width=5, height=2, command=clear).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text='=', width=5, height=2, command=calculate).grid(row=4, column=2, padx=5, pady=5)
tk.Button(root, text='+', width=5, height=2, command=lambda: click_op('+')).grid(row=4, column=3, padx=5, pady=5)

root.mainloop()