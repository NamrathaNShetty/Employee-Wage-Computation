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

    """    

    emp_Check = random.randint(0,1)

    if emp_Check == 0:
        print("Employee is present")
    else:
        print("Employee is absent")

if __name__ == "__main__":
    checkAttendance()