import tkinter as tk
from tkinter import messagebox
from database import connect_db

class DataEntryPage:
    def __init__(self, root, navigation_manager):
        self.root = root
        self.navigation_manager = navigation_manager
        self.frame = tk.Frame(root)
        self.frame.pack(pady=50)

        self.dataCollector_header = tk.Label(self.frame, text="Data Collector", font=("Arial",25))
        self.dataCollector_header.grid(row=0, columnspan=2, pady=20)

        self.name_label = tk.Label(self.frame, text="Name: ").grid(row=1, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)


        self.gender_label = tk.Label(self.frame, text="Gender:").grid(row=2, column=0, padx=10, pady=5)
        self.gender_var = tk.StringVar()
        self.gender_frame = tk.Frame(self.frame)
        self.gender_frame.grid(row=2, column=1, sticky="w", padx=10)
        tk.Radiobutton(self.gender_frame, text="Male", variable=self.gender_var, value="male").pack(side="left", padx=5)
        tk.Radiobutton(self.gender_frame, text="Female", variable=self.gender_var, value="female").pack(side="left", padx=5)

        self.age_label = tk.Label(self.frame, text="Age: ").grid(row=3, column=0, pady=5)
        self.age_entry = tk.Entry(self.frame)
        self.age_entry.grid(row=3, column=1, pady=5)

        self.height_label = tk.Label(self.frame, text="Height (cm):").grid(row=4, column=0, padx=10, pady=5)
        self.height_entry = tk.Entry(self.frame)
        self.height_entry.grid(row=4, column=1, padx=10, pady=5)

        self.weight_label = tk.Label(self.frame, text="Weight (kg):").grid(row=5, column=0, padx=10, pady=5)
        self.weight_entry = tk.Entry(self.frame)
        self.weight_entry.grid(row=5, column=1, padx=10, pady=5)

        self.workout_label = tk.Label(self.frame, text="Workout Duration (hours/week):").grid(row=6, column=0, padx=10, pady=5)
        self.workout_entry = tk.Entry(self.frame)
        self.workout_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Button(self.frame, text="Submit", command=self.add_data).grid(row=7, columnspan=2, pady=10)
        tk.Button(self.frame, text="View Data", command=self.view_data).grid(row=8, columnspan=2, pady=5)
        

    def add_data(self):

        name = self.name_entry.get()
        gender = self.gender_var.get()
        age = self.age_entry.get()
        height = self.height_entry.get()
        weight = self.weight_entry.get()
        workout_duration = self.workout_entry.get()

        age = int(age)
        height = int(height)
        weight = int(weight)
        workout_duration = int(workout_duration)
        
        if not all([name, gender, age, height, weight, workout_duration]):
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            age = int(age)
            height = int(height)
            weight = int(weight)
            workout_duration = int(workout_duration)

            db = connect_db()
            cursor = db.cursor()

            sql_query = "INSERT INTO data_table (name, gender, age, height, weight, workout_duration) VALUES (%s, %s, %s, %s, %s, %s)"
            data = (name, gender, age, height, weight, workout_duration)
            
            cursor.execute(sql_query, data)
            db.commit()
            db.close()
            messagebox.showinfo("Success", "Data added successfully!")

            #After insertion Deleting Form Data
            self.name_entry.delete(0, tk.END)
            self.gender_var.set("")
            self.age_entry.delete(0, tk.END)
            self.height_entry.delete(0, tk.END)
            self.weight_entry.delete(0, tk.END)
            self.workout_entry.delete(0, tk.END)


        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_data(self):
        """Navigate to the View Data page."""
        self.frame.destroy()
        self.navigation_manager.show_view_data()
