import tkinter as tk
from tkinter import messagebox
from database import connect_db

class LoginPage:
    def __init__(self, root, navigation_manager):
        self.root = root
        self.navigation_manager = navigation_manager
        self.frame = tk.Frame(root)
        self.frame.pack(pady=150)

        self.login_header = tk.Label(self.frame, text="Login", font=("Arial",25))
        self.login_header.grid(row=0, columnspan=2, pady=20)

        self.username_label = tk.Label(self.frame, text="Username:").grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.frame, text="Password:").grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(self.frame, text="Login", command=self.login).grid(row=3, columnspan=2, pady=10)
        tk.Button(self.frame, text="Register", command=self.open_register).grid(row=4, columnspan=2, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            if cursor.fetchone():
                messagebox.showinfo("Success", "Login successful!")
                # self.frame.destroy()
                self.open_data_entry()
            else:
                messagebox.showerror("Error", "Invalid username or password!")
            db.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def open_register(self):
        self.frame.destroy()
        self.navigation_manager.show_register()

    def open_data_entry(self):
        self.frame.destroy()
        self.navigation_manager.show_data_entry()

