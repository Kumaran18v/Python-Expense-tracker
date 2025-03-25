# Python-Expense-tracker

Project Overview

The Expense Tracker is a Python-based application designed to help users manage their daily expenses. It allows users to add expenses, categorize them, and view summaries of their total and category-wise expenditure. The expense data is stored in a JSON file, ensuring data persistence between sessions.


Features:

1. User Input:

Add expenses by entering the amount, category (e.g., food, transport, etc.), and a brief description.


2. Data Storage:

Expenses are stored in a JSON file (expenses.json) for later retrieval.


3. Expense Categories:

Categorize expenses for better organization (e.g., food, transport, entertainment).


4. Data Analysis:

View total expenses and a category-wise breakdown of expenditure.


5. User-Friendly Menu:

Simple menu-based interaction with options to add expenses, view summaries, or exit.


6. Error Handling:

Handles invalid inputs gracefully, such as non-numeric amounts.

Installation and Setup:

1. Prerequisites:

Python 3.x (Install from Python Official Website).

2. Steps to Run the Program:

Clone or download this repository.

Open the terminal or command prompt and navigate to the project folder.

Run the program using the command:

python expense_tracker.py

Usage Instructions:

Main Menu Options:

1. Add Expense: Enter the expense amount, category, and description.


2. View Expense Summary: View the total expenses and category-wise breakdown.


3. Exit: Exit the application.
Sample Output:

Expense Tracker

Options:
1. Add Expense
2. View Expense Summary
3. Exit

Enter your choice (1-3): 1
Enter amount spent: 100  
Enter category (e.g., food, transport, entertainment): food  
Enter a brief description: Grocery shopping  
Expense added successfully!

File Structure:

expense_tracker.py: Main Python script containing the application logic.

expenses.json: JSON file where expense data is stored.

Future Enhancements:

Add graphical user interface (GUI) using Tkinter or PyQt.

Implement monthly filters and advanced reporting.

Add charts to visualize spending trends.

License:

This project is licensed under the MIT License.
