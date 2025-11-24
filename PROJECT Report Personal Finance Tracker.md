## PROJECT TITLE: Personal Finance Tracker

NAME: Parth Agarwal SUBJECT: Python Essentials (1st Semester)



**1. ABSTRACT**

This project is a Python-based application designed to help users manage their personal finances. It allows users to log daily expenses, view a history of transactions, and visualize their spending habits through graphical charts. The system ensures data persistence using CSV files.



**2. PROBLEM \& OBJECTIVE**

Problem: Manual expense tracking on paper is difficult to maintain and analyze.



Objective: To create an automated system that stores expense data permanently and provides visual insights (Pie Charts) using Python.



**3. METHODOLOGY**

The project is built using the following Python libraries:



Pandas: Used to create a DataFrame for easy data manipulation and to read/write data to a CSV file (expenses.csv).



Matplotlib: Used to generate a Pie Chart that groups expenses by category (e.g., Food, Travel).



OS Module: Handles file paths to ensure the database is created automatically if missing.



Logic Flow:



Start: Check if database exists.



Menu: User chooses to Add, View, or Visualize.



Process:



Add: Append inputs (Date, Category, Amount) to CSV.



View: Print the CSV data as a table.



Visualize: Group data by 'Category' and show a Pie Chart.



Loop: Continue until "Exit".



**4. RESULTS**

The system was successfully tested with the following outputs:



Data Entry: Expenses are saved immediately to expenses.csv.



Visualization: A Pie Chart is generated showing the percentage distribution of spending (e.g., 50% Food, 30% Travel).

**5. CONCLUSION**

The Personal Finance Tracker successfully demonstrates file handling and data visualization in Python. It provides a simple, offline solution for budget management, replacing manual calculation methods.



**6. FUTURE SCOPE**

Add a GUI (Graphical User Interface).



Add monthly budget limits and warnings.

