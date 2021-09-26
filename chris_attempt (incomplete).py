# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 22:23:43 2021

@author: chris
"""

import csv
from datetime import datetime#, date, time, timedelta (delete if unused)

status_tuple = ("Pending", "Approved", "Denied")
verify_list = ("A", "D", "S")

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
        

#%%
def retrieve_personal():
    
    employee_id = input("Enter ID") #retrieve instead

    with open("expense_records.csv",'r') as filepointer:
        for row in csv.reader(filepointer):
            if row[0] == employee_id:
                print(row) #print the f string here instead, may use as function but kiv; in this case do row[] index based on csv file
retrieve_personal()

#problem w this, does not update the expense record file 
def verify_expense():  #may need to import pandas to replace a specific value   
    employee_id = input("Enter employeee ID:")
    
    #filter whetehr manager first based on id + find out dept using the employee details file
    with open("employee_details.csv",'r') as filepointer:
        for row in csv.reader(filepointer):
            if row[0] == employee_id and row[2] == "Manager":
                print("Access granted.")
                department = row[3]
                #manager check successful: open expense records (only by dept)
        
                with open("expense_records.csv",'r+') as filepointer:
    
                    for line in csv.reader(filepointer):
                
                            if department == line[2] and line[7] == status_tuple[0]: #from exp records only check those pending
                                print(line) #format this to print as a f string if possible
                                verify = input("Enter A to approve claim, D to deny claim, or S to skip claim: ")
                                if verify.upper() == "A":
                                    print("Claim approved.")
                                    line[7] = status_tuple[1]
                                    print(line) # FIND A WAY TO REPLACE THIS IN THE EXP RECORDS, (Needed for indv records) also need as function keeps referring to the exp records
                                    
                                elif verify.upper() == "D":
                                    print("Claim denied.")
                                    line[7] = status_tuple[2]
                                    
                                elif verify.upper() == "S": #go back to the for loop n carry on to next line
                                    line[7] = status_tuple[0]
                                    
                                while verify.upper() not in verify_list:
                                    print("You have entered an invalid choice. Please enter again.")
                                    verify = input("Enter A to approve claim, D to deny claim, or S to skip claim")

                                        
                   
                       # print("No claims to verify.")
                            
                    print(exit_page())
                        
            elif row[0] == employee_id and row[2] == "Employee":
                print("Access denied.")
                print(exit_page())
verify_expense()

# #%%
# df = pd.read_csv("expense_records.csv")


# def verify_expense():
    
#     employee_id = input("Enter employeee ID:")
    
#     #filter whetehr manager first based on id + find out dept using the employee details file
#     with open("employee_details.csv",'r') as filepointer:
#         for row in csv.reader(filepointer):
#             if row[0] == employee_id and row[2] == "Manager":
#                 print("Access granted.")
#                 department = row[3]
#                 #manager check successful: open expense records (only by dept)
                
#                 df = pd.read_csv("expense_records.csv")
                
#                 for line in df:
#                     if department == line[2] and line[7] == status_tuple[0]: #from exp records only check those pending
#                         print(line) #format this to print as a f string if possible
#                         verify = input("Enter A to approve claim, D to deny claim, or S to skip claim")
#                         if verify.upper() == "A":
#                             print("Claim approved.")
#                             df.replace(to_replace = line[7], value = status_tuple[1])
#                         elif verify.upper() == "D":
#                             print("Claim denied.")
#                             df.replace(to_replace = line[7], value = status_tuple[2])
#                         elif verify.upper() == "S": #go back to the for loop n carry on to next line
#                             df.replace(to_replace = line[7], value = status_tuple[0])
#                         while verify.upper() not in verify_list:
#                             print("You have entered an invalid choice. Please enter again.")
#                             verify = input("Enter A to approve claim, D to deny claim, or S to skip claim")
#                     else:
#                         df
                        
                        
#                 df.to_csv('outputfile.csv')
                
#                     # #if no claims to verify
#                     #     if department == line[2] and line[7] != status_tuple[0]:
#                     #         count += 0
#                     #     if count == 0:
#                     #         print("No claims to verify.")
                            
#                 exit_page()
#                     #if no exiisting records to check...
                    
                
#                     # df = pd.read_csv("expense_records.csv")
#                     # status_column_data = df['Status'].tolist()
#                     # x = status_column_data[0]
#                     # check = False
#                     # for i in status_column_data:
#                     #     if x == i:
#                     #         True
#                     # if check == True:
#                     #     print("No claims to verify.")
                        
#             elif row[0] == employee_id and row[2] == "Employee":
#                 print("Access denied.")
#                 print(homepage())
# verify_expense()


























