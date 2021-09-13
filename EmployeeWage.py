"""
@Author: Namratha N Shetty
@Date: 2021-09-13 16:36:00 
@Last Modified by: Namratha N Shetty
@Last Modified time: 2021-09-13 16:37:00
@Title : To check employee is present or absent
"""

import random
print("Welcome to employee wage computation")

def checkAttendance():
    """
    Description:
        This function is to check whether employee is present or absent.
        Employee daily wage is calculated for full day and part time.
    """    

    isFullTime = 1
    isPartTime = 2
    day_Hour=0

    wage_Per_Hour = 20
    
    emp_Check = random.randint(0,2)

    if emp_Check == isFullTime:
        day_Hour = 8
    elif emp_Check == isPartTime:
        day_Hour = 4 
    else:
        print("Employee is absent")
        

    employee_Wage = wage_Per_Hour * day_Hour
    print("Employee wage is:", employee_Wage)

if __name__ == "__main__":
    checkAttendance()