"""
@Author: Namratha N Shetty
@Date: 2021-09-13 23:36:00 
@Last Modified by: Namratha N Shetty
@Last Modified time: 2021-09-14 1:37:00
@Title : To check employee is present or absent
"""

import random
print("Welcome to employee wage computation")

def calculateHour(attendance_Status):
    """
    Description:
        This function determine the work hours
    Parameter:
        attendanceStatus is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if attendance_Status == isFullTime:
        day_Hour = 8
    elif attendance_Status == isPartTime:
        day_Hour = 4 
    else:
        day_Hour = 0
    return day_Hour

def getWorkHours(total_Working_Hours):
    """
    Description:
        this function calculate working hours
    """
    print("Total working hours:", total_Working_Hours)     

def calculateWage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    daily_Wage_List = []
    wage_Per_Hour = 20
    working_Days = 0
    total_Working_Hours = 0
    maximum_Working_Days = 20
    maximum_Working_Hours = 100
    total_Wage = 0
    wage_Dict = {}

    while working_Days < maximum_Working_Days and total_Working_Hours < maximum_Working_Hours:
        attendance = random.randint(0,2)
        attendance_Status = switcher.get(attendance)
        working_Hours = calculateHour(attendance_Status)
        daily_Wage = working_Hours * wage_Per_Hour
        daily_Wage_List.append(daily_Wage)
        total_Wage += daily_Wage
        total_Working_Hours += working_Hours
        working_Days += 1
        wage_Dict[working_Days] = {
            "Daily Wage:" : daily_Wage,
            "Total Wage:" : total_Wage
        }
    return wage_Dict

absent = 0
isFullTime = 1
isPartTime = 2

switcher = {
    0: absent,
    1: isFullTime,
    2: isPartTime,
}

print("Total employee wage for month is:",calculateWage())    