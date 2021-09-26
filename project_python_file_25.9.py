# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 09:49:14 2021

@author: user
"""
# %% Imports

import csv
from datetime import datetime#, date, time, timedelta (delete if unused)

# %% Def functions

def get_date(msg, str_format, dte_format):
    result = None
    while result is None:
        try:
            my_string = str(input(msg))
            result = datetime.strptime(my_string, dte_format)
        except ValueError:
            print(f"Please enter the right format ({str_format})")
    return result

def format_amount(amount):
    raw_result = None
    while True:
        try:
            raw_result = float(input(amount))
        except ValueError:
            print("Please enter a valid number again.")
        else:
            if isinstance(raw_result, float):
                return "${:,.2f}".format(raw_result)

def expense_records():
    filename = "expense_records.csv"

    project_code_list = ["11111", "11112", "11113", "11114",
                         "11115", "11116", "11117", "11118", "11119", "11120", "11121"]
    status_tuple = ("Pending", "Approved", "Denied")

    employee_id = input("ID: ")

    employee_name = input("What's your name: ")

    department = input("Department: ")

    expense_category = input("Category: ")

    project_code = input("Project Code: ")
    
    while project_code not in project_code_list:
        print("You have entered an invalid code. Please enter again.")
        project_code = input("Project Code: ")

    project_remarks = input("Remarks: ")

    amount_spent = format_amount("Enter spending amount (eg. 1000)")

    status = status_tuple[0]

    my_date = get_date("Enter spending date (yyyy-mm-dd)",
                       "yyyy-mm-dd", "%Y-%m-%d")
    spending_date = my_date.strftime("%Y-%m-%d")

    datenow = datetime.now()
    date_submitted = datenow.strftime("%d-%m-%y")
    
#confirmation stage

    with open(filename, "a", newline="") as file_pointer:
        csv_pointer = csv.writer(file_pointer)
        row = [employee_id, employee_name, department, expense_category, project_code,
               project_remarks, amount_spent, status, spending_date, date_submitted]
        csv_pointer.writerow(row)

    print("Expense record has been updated.")
    
    return exit_page()


def homepage():

    employee_name = ("Enter your name: ") #change this to extract name from employeedetails
    
    menu = f"""welcome {employee_name}!
    ------------------------------------------
    Please choose what you want to do:
        Key in 1 to update expense record 
        Key in 2 to retrieve personal records
        
    For managers only:
        Key in 3 to verify submitted records
        Key in 4 to retrieve department data
        Key in 5 for company data
        
    Press e to exit
    """

    print(menu)

    choice_list = ["1", "2", "3", "4", "5","e"]

    choice = input("Enter your choice: ")

    if choice == "1":
        return expense_records()
    elif choice == "2":
        print("2")
    elif choice == "3":
        print("3")
    elif choice == "4":
        print("4")
    elif choice == "5":
        print("5")
    elif choice =="e":
        return("Good bye!")

    while choice not in choice_list:
        print("You have entered an invalid choice. Please enter again.")
        choice = input("Enter your choice: ")
        
def exit_page():
    choice_list = ["e","r"]
    choice = input("Enter e to exit or r to return to homepage")
    if choice == "e":
        return "Good bye!"
    elif choice == "r":
        return homepage()
    while choice not in choice_list:
        print("You have entered an invalid choice. Please enter again.")
        choice = input("Enter your choice: ")
        
def login():
    # Open CSV file
    employee_details_list = []
    password_dict = {}
    with open("employee_details.csv","r") as csvfile:
        employee_details_list = [row.split(",") for row in csvfile]
        employee_details_list = employee_details_list[1:] 
        for row in employee_details_list:
            password_dict[row[0]] = row[5].strip()
    
    # Login Details
    
    print("Welcome To Expense Tracker. Please input your Username and Password to enter")
    # employee_id = input("Enter Employee ID here:")
    # login_password = input("Enter your password here:")
    
    # Login Details Error Checking
    
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    while username not in password_dict.keys() or password != password_dict[username]:
        print("Invalid username or password. Please enter again: ")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
    # while login_password != employee_pw[employee_id]:
    #     print("Incorrect password.")
    #     login_password= input("Please enter your password again:")
    print("Logged in successfully.")
    print(homepage())
    
#%%MAiN scope

login()


# Employee’s input to store into a list (to_check)
# -> if manager approve = true then append another list (manager_true) first, then after the for loop is complete, then append into csv file. Manager_true is only a temporary variable that will be erased after appending to csv
# -> if false, then store all the unverified ones into a separate list (manager_false), then ask employee to input agn (manager_false must append back into to_check eventually to run the loop of verification again)
# Removes the need to extract information from csv file since it is all within python itself



#%%
# from pathlib import Path
# Path('data.db').touch()
# import sqlite3
# conn = sqlite3.connect('data.db')
# c = conn.cursor()

# import pandas as pd
# # load the data into a Pandas DataFrame
# users = pd.read_csv('expense_records.csv')
# # write the data to a sqlite table
# users.to_sql('expense_records', conn, if_exists='append', index = False)




















