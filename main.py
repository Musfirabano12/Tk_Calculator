import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if entry2.get() else 0

        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        elif operation == 'Square':
            result = num1 ** 2
        elif operation == 'SquareRoot':
            if num1 < 0:
                raise ValueError("Cannot take square root of negative number.")
            result = math.sqrt(num1)

        result_var.set(f"Result: {round(result, 2)}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Cannot divide by zero.")

root = tk.Tk()
root.title("TK Calculator")
root.geometry("420x420")
root.configure(bg="#f0f8ff")

tk.Label(root, text="TK Calculator", font=('Arial', 16, 'bold'), bg="#f0f8ff").pack(pady=10)

tk.Label(root, text="First Number:", font=('Arial', 13), bg="#f0f8ff").pack()
entry1 = tk.Entry(root, font=('Arial', 13), width=25, justify='center')
entry1.pack()

tk.Label(root, text="Second Number (optional):", font=('Arial', 13), bg="#f0f8ff").pack(pady=5)
entry2 = tk.Entry(root, font=('Arial', 13), width=25, justify='center')
entry2.pack()

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack(pady=20)

btn_style = {
    'width': 12,
    'height': 2,
    'font': ('Arial', 12),
    'relief': 'raised',
    'bd': 3
}

tk.Button(button_frame, text='Add', bg='#90ee90', command=lambda: calculate('Add'), **btn_style).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text='Subtract', bg='#ffcccb', command=lambda: calculate('Subtract'), **btn_style).grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text='Multiply', bg='#add8e6', command=lambda: calculate('Multiply'), **btn_style).grid(row=1, column=0, padx=10, pady=5)
tk.Button(button_frame, text='Divide', bg='#f4a460', command=lambda: calculate('Divide'), **btn_style).grid(row=1, column=1, padx=10, pady=5)

tk.Button(button_frame, text='Square', bg='#d9edf7', command=lambda: calculate('Square'), **btn_style).grid(row=2, column=0, padx=10, pady=5)
tk.Button(button_frame, text='Square Root', bg='#d0e9c6', command=lambda: calculate('SquareRoot'), **btn_style).grid(row=2, column=1, padx=10, pady=5)

result_var = tk.StringVar()
result_var.set("Result: ")
tk.Label(root, textvariable=result_var, font=('Arial', 15, 'bold'), bg="#f0f8ff").pack(pady=15)

root.mainloop()
