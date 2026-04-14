import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 + num2
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()
root.title("Addition Calculator")

# Labels and Entries
tk.Label(root, text="First Number").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Second Number").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Button
tk.Button(root, text="Add", command=add_numbers).grid(row=2, column=1, pady=60)

# Result
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=3, column=1)

root.mainloop()