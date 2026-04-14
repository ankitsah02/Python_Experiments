import tkinter as tk

# Function to display input
def show():
    name = entry1.get()
    sap = entry2.get()
    email = entry3.get()

    print("Name:", name)
    print("SAP ID:", sap)
    print("Email:", email)

# Main window
root = tk.Tk()
root.title("Student Details")
root.geometry("300x250")

# Name
tk.Label(root, text="Name:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

# SAP ID
tk.Label(root, text="SAP ID:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Email
tk.Label(root, text="Email:").pack(pady=5)
entry3 = tk.Entry(root)
entry3.pack(pady=5)

# Button
tk.Button(root, text="Submit", command=show).pack(pady=10)

root.mainloop()