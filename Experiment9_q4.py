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

# Window background
root.configure(bg="lightblue")

# First number
tk.Label(root, text="First Number", bg="lightblue").pack()
entry1 = tk.Entry(root, bg="white")
entry1.pack()

# Second number
tk.Label(root, text="Second Number", bg="lightblue").pack()
entry2 = tk.Entry(root, bg="white")
entry2.pack()

# Button
tk.Button(root, text="Add", bg="green", fg="white", command=add_numbers).pack(pady=10)

# Result
result_label = tk.Label(root, text="Result: ", bg="lightblue")
result_label.pack()

root.mainloop()