import tkinter as tk
from navigation import NavigationManager
from database import create_database

def main():
    create_database()
    root = tk.Tk()
    root.title("Data Entry App")
    root.geometry("1100x600")

    navigation_manager = NavigationManager(root)
    # navigation_manager.show_login()
    navigation_manager.show_splash_screen()

    root.mainloop()

if __name__ == "__main__":
    main()
