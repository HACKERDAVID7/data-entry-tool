import tkinter as tk
from tkinter import messagebox, ttk
from database import connect_db

class ViewDataPage:
    def __init__(self, root, navigation_manager):
        self.root = root
        self.navigation_manager = navigation_manager
        self.frame = tk.Frame(root)
        self.frame.pack(fill="both", expand=True, pady=20)

        # Title
        tk.Label(self.frame, text="View Data", font=("Arial",25)).pack(pady=15)

        # Filter Section
        self.filter_var = tk.StringVar()
        self.column_var = tk.StringVar()
        filter_frame = tk.Frame(self.frame)
        filter_frame.pack(pady=5)

        # Dropdown to select column
        tk.Label(filter_frame, text="Filter by:").grid(row=0, column=0, padx=5)
        self.column_dropdown = ttk.Combobox(filter_frame, textvariable=self.column_var, state="readonly", width=12)
        self.column_dropdown["values"] = ("Name", "Gender", "Age", "Height", "Weight", "Workout Duration")
        self.column_dropdown.grid(row=0, column=1, padx=50)
        self.column_dropdown.current(0)  # Default to "Name"

        # Entry for filter value
        tk.Label(filter_frame, text="Value:").grid(row=0, column=2, padx=5)
        self.filter_entry = tk.Entry(filter_frame, textvariable=self.filter_var)
        self.filter_entry.grid(row=0, column=3, padx=5)

        # Buttons for filtering
        tk.Button(filter_frame, text="Apply Filter", command=self.apply_filter).grid(row=0, column=4, padx=5)
        tk.Button(filter_frame, text="Clear Filter", command=self.load_data).grid(row=0, column=5, padx=5)

        # Table Section
        self.tree = ttk.Treeview(self.frame, columns=("ID", "Name", "Gender", "Age", "Height", "Weight", "Workout Duration"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Height", text="Height")
        self.tree.heading("Weight", text="Weight")
        self.tree.heading("Workout Duration", text="Workout Duration")
        self.tree.column("ID", width=50)
        self.tree.column("Name", width=150)
        self.tree.column("Gender", width=150)
        self.tree.column("Age", width=150)
        self.tree.column("Height", width=150)
        self.tree.column("Weight", width=150)
        self.tree.column("Workout Duration", width=150)
        self.tree.pack(fill="both", expand=True, pady=10)

        # Back Button
        # tk.Button(self.frame, text="Back", command=self.back).pack(pady=5)
        self.button_frame = tk.Frame(self.frame)
        self.button_frame.pack(pady=5)
        tk.Label(self.button_frame, text="Data Visualization: ",).grid(row=1, column=0 , padx=5, pady=5)
        tk.Button(self.button_frame, text="Workout Intensity", command=self.visualize_WI).grid(row=1, column=1 , padx=5, pady=5)
        tk.Button(self.button_frame, text="Weight VS Calories", command=self.visualize_WeightCal).grid(row=1, column=2 , padx=5, pady=5)
        tk.Button(self.button_frame, text="Duration VS Calories", command=self.visualize_DurationCal).grid(row=1, column=3 , padx=5, pady=5)
        tk.Button(self.button_frame, text="BMR VS Calories", command=self.visualize_BMRCal).grid(row=1, column=4, padx=5, pady=5)
        tk.Button(self.button_frame, text="BMR VS AGE", command=self.visualize_BMR_AGE).grid(row=1, column=5, padx=5, pady=5)
        tk.Button(self.button_frame, text="Correlation Matrix", command=self.heatmap).grid(row=1, column=6, padx=5, pady=5)
        # tk.Button(self.button_frame, text="Back", command=self.back).grid(row=2, column=3 , padx=5, pady=5)
        tk.Button(self.frame, text="Back", command=self.back).pack()

        # Load all data initially
        self.load_data()

    def load_data(self):
        """Load all data from the database into the tree view."""
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT * FROM data_table")
            rows = cursor.fetchall()
            db.close()

            self.update_tree(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def apply_filter(self):
        """Apply filter based on user input and selected column."""
        filter_value = self.filter_var.get().strip()
        column = self.column_var.get().lower().replace(" ", "_")  # Convert to column name format

        if not filter_value:
            messagebox.showerror("Error", "Please enter a filter value!")
            return

        try:

            db = connect_db()
            cursor = db.cursor()
            query = f"SELECT * FROM data_table WHERE {column} LIKE %s"
            cursor.execute(query, (f"%{filter_value}%",))
            rows = cursor.fetchall()
            db.close()

            self.update_tree(rows)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply filter: {e}")

    def update_tree(self, rows):
        """Update the tree view with new data."""
        # Clear existing rows
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insert new rows
        for row in rows:
            self.tree.insert("", "end", values=row)

    def back(self):
        """Go back to the previous page."""
        self.frame.destroy()
        self.navigation_manager.show_data_entry()

    def visualize_WI(self):
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = pd.read_csv("/Users/sumit/Desktop/VSCode/LPU/SEM3/CAP776/ca4/Project/calories.csv")

            plt.figure(figsize=(10,8))
            sns.countplot(data=df, x="duration_per_day", hue="duration_per_day")
            plt.title("Count plot for workout intensity")
            plt.show()

        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", f"Failed to export data: {e}")

    
    def visualize_WeightCal(self):
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = pd.read_csv("/Users/sumit/Desktop/VSCode/LPU/SEM3/CAP776/ca4/Project/calories.csv")

            # calories burned vs weight
            plt.figure(figsize=(10, 8))
            sns.scatterplot(data=df, x="Weight", y="calories_burned", hue='Gender')
            plt.title("Weight vs Calories Burned with respect to Gender")
            plt.show()
            
        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", f"Failed to export data: {e}")

    def visualize_DurationCal(self):
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = pd.read_csv("/Users/sumit/Desktop/VSCode/LPU/SEM3/CAP776/ca4/Project/calories.csv")

            plt.figure(figsize=(10, 8))
            sns.scatterplot(df,x='Duration', y='calories_burned',hue='Gender')
            plt.xlabel('Duration')
            plt.ylabel('Calories Burned')
            plt.title('Calories Burned vs Duration')
            plt.show()
            
        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", f"Failed to export data: {e}")
    
    def visualize_BMRCal(self):
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = pd.read_csv("/Users/sumit/Desktop/VSCode/LPU/SEM3/CAP776/ca4/Project/calories.csv")

            plt.figure(figsize=(10, 8))
            sns.scatterplot(data=df, x="bmr", y="calories_burned", hue='Gender')
            plt.title('BMR vs Calories Burned')
            plt.show()
            
        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", f"Failed to export data: {e}")
    
    def visualize_BMR_AGE(self):
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = pd.read_csv("/Users/sumit/Desktop/VSCode/LPU/SEM3/CAP776/ca4/Project/calories.csv")

            plt.figure(figsize=(10, 8))
            sns.scatterplot(data=df, x="Age", y="bmr", hue='Gender')
            plt.title('BMR vs Age')
            plt.show()
            
        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", f"Failed to export data: {e}")


    def heatmap(self):
        try:
            import numpy as np
            import pandas as pd
            import matplotlib.pyplot as plt
            import seaborn as sns

            df = pd.read_csv("/Users/sumit/Desktop/VSCode/LPU/SEM3/CAP776/ca4/Project/calories.csv")

            data = df[['Gender', 'Age', 'Height', 'Weight', 'Duration', 'bmr', 'duration_per_day', 'calories_burned']]

            # correlation matrix
            plt.figure(figsize=(10, 8))
            sns.heatmap(data.corr(), annot=True)
            plt.title("Correlation Matrix")
            plt.show()
            
        except Exception as e:
            # Handle errors
            messagebox.showerror("Error", f"Failed to export data: {e}")
        






    
            
