import tkinter as tk
from tkinter import messagebox

def register():
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    
    if username and password and email:
        # Here you would typically handle the registration logic, like saving to a database
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showwarning("Warning", "Please fill all fields.")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry widgets
label_username = tk.Label(root, text="Username")
label_username.pack()

entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Password")
label_password.pack()

entry_password = tk.Entry(root, show="*")
entry_password.pack()

label_email = tk.Label(root, text="Email")
label_email.pack()

entry_email = tk.Entry(root)
entry_email.pack()

# Create a submit button
button_register = tk.Button(root, text="Register", command=register)
button_register.pack()

# Start the GUI event loop
root.mainloop()
