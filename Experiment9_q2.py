import tkinter as tk
# Function to add numbers
def addition():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        result_label.config(text="Sum: " + str(x + y))
    except:
        result_label.config(text="Enter valid integers")
# Main window
root = tk.Tk()
root.title("Addition")
root.geometry("300x250")

# Input X
tk.Label(root, text="Enter X:").pack(pady=5)
entry_x = tk.Entry(root)
entry_x.pack(pady=5)

# Input Y
tk.Label(root, text="Enter Y:").pack(pady=5)
entry_y = tk.Entry(root)
entry_y.pack(pady=5)

# Button
tk.Button(root, text="ADD", command=addition).pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()