import tkinter as tk
from database import connect_db

class SplashScreen:
    def __init__(self, root, navigation_manager):
        self.root = root
        self.navigation_manager = navigation_manager
        self.frame = tk.Frame(root)
        self.frame.pack(pady=200)

        splash_label1 = tk.Label(self.frame, text="Data Collector", font=("Arial",25))
        splash_label1.pack(pady=10)
        splash_label2 = tk.Label(self.frame, text="Version 1.0.0", font=("Arial",12))
        splash_label2.pack(pady=5)
        splash_label3 = tk.Label(self.frame, text="Developed by: Sumit Kumar", font=("Arial",12))
        splash_label3.pack(pady=5)

        self.frame.after(3000, self.open_login_page)

    def open_login_page(self):
        self.frame.destroy()
        self.navigation_manager.show_login()




