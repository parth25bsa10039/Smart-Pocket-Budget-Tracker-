import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.filename = os.path.join(script_dir, 'expenses.csv')
        
        self.columns = ['Date', 'Category', 'Description', 'Amount']
        
        
        if not os.path.exists(self.filename):
            try:
                df = pd.DataFrame(columns=self.columns)
                df.to_csv(self.filename, index=False)
                print(f"Created new database at: {self.filename}")
            except PermissionError:
                print(f"Error: Could not create file. Check permissions for {script_dir}")

    def add_expense(self):
        print("\n--- Add New Expense ---")
        date = datetime.now().strftime("%Y-%m-%d")
        category = input("Enter Category (Food, Transport, Bills, etc.): ")
        description = input("Enter Description: ")
        
        while True:
            try:
                amount_input = input("Enter Amount: ")
                amount = float(amount_input)
                if amount < 0:
                    print("Amount cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number (e.g., 10.50).")

        new_data = pd.DataFrame([[date, category, description, amount]], columns=self.columns)
        
        try:
            
            new_data.to_csv(self.filename, mode='a', header=False, index=False)
            print("Expense added successfully!")
        except PermissionError:
            print("\nERROR: The file 'expenses.csv' is open in another program (like Excel).")
            print("Please close it and try again.")

    def view_expenses(self):
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) == 0:
            print("\nNo expenses recorded yet.")
            return

        try:
            df = pd.read_csv(self.filename)
            print("\n--- Expense History ---")
            if df.empty:
                print("No data found.")
            else:
                print(df.to_string(index=False))
                print(f"\nTotal Spent: ${df['Amount'].sum():.2f}")
        except pd.errors.EmptyDataError:
            print("\nFile is empty.")

    def analyze_expenses(self):
        try:
            df = pd.read_csv(self.filename)
            if df.empty:
                print("Not enough data to visualize.")
                return
            
            
            if df['Amount'].sum() == 0:
                print("Total expenses are 0. Cannot create chart.")
                return

            
            summary = df.groupby('Category')['Amount'].sum()
            
            
            plt.figure(figsize=(8, 6))
            summary.plot(kind='pie', autopct='%1.1f%%', startangle=140)
            plt.title('Expense Distribution by Category')
            plt.ylabel('') 
            
            print("\nDisplaying chart... (Check the popup window)")
            plt.show()
            
        except Exception as e:
            print(f"Error generating chart: {e}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\n=== PERSONAL FINANCE TRACKER ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Visualize Spending (Chart)")
        print("4. Exit")
        
        choice = input("Enter choice (1-4): ")
        
        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.analyze_expenses()
        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()


git remote add origin https://github.com/parth25bsa10039/Smart-Pocket-Budget-Tracker-.git
git branch -M main
git push -u origin main
