import Student_Resistresion
import Display_Records
import Search_Student
import datetime
import Sliptime
import Writelogs

path=r"D:\Indixpert 2025\Student_Record_Management_System\Umang\Studentdeta.json"

def chioceoption():
    
    while True:
        try:
            data = int(input("Please select an option (0-3): "))
            if data in [0, 1, 2, 3]:
                break
            else:
                print("\nInvalid option! Please select a valid number (0-3).\n")
        except Exception as a :
            print("\nInvalid input! Please enter a digits\n")
            data={"error":str(a) ,"date":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
            Writelogs.writelogs(str(data))
    
    if data == 0:
        print("\nExiting... Goodbye!\n")
        exit()
    
    if data == 1:
        Student_Resistresion.studentresistresion(path)
        Sliptime.sliptime(data)
    
    if data == 2:
        Sliptime.sliptime(data)
        Display_Records.displayrecords(path)
    
    if data == 3:
        Sliptime.sliptime(data)
        Search_Student.searchstudent(path)