import os
import json
import datetime
import Writelogs
import Get_valid

def searchstudent(path):
    if not os.path.exists(path):
        return "File not found."

    with open(path, "r") as file:
        students = json.load(file)
    while True:
        print("----- Search by -----")
        print("press 1. Id")
        print("press 2. Name")
        print("press 3. Contact")
        print("press 4. Address")
        print("press 5. Email Id")
        print("press 0. Exit Searching Area")
        print("=" * 30)

        try:
            data = int(input("Please select an option (0-5): "))
            if data in [0, 1, 2, 3, 4, 5]:
                break
            else:
                print("\nInvalid option! Please select a valid number (0-5).\n")
        except Exception as c :
            print("Invalid input! Please enter a digits")
            data={"error":str(c) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            Writelogs.writelogs(str(data))
    
    if data == 0:
        print("\nExiting for Searching!")
        return True
    if data == 1:
        user="id"
        uservalue = str(Get_valid.get_valid_number("Enter your ID:- "))
    if data == 2:
        user="name"
        uservalue = Get_valid.get_valid_name("Enter your Name:- ")
    if data == 3:
        user="contact"
        uservalue = Get_valid.get_valid_contact("Enter your Contect:- ")
    if data == 4:
        user="address"
        uservalue = input("Enter Your Address:- ")
    if data == 5:
        user="email Id"
        uservalue = input("Enter your Email Id:- ")
    
    found=False

    for listdata in students:
        for key,value in listdata.items():
            if str(value).lower()== str(uservalue).lower():
                print(json.dumps(listdata,indent=4))
                found=True
    if not found:
        print(f"\n No student found with {user} = '{uservalue}'. Please try again.\n")