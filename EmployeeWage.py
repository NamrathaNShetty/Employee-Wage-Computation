"""
@Author: Namratha N Shetty
@Date: 2021-09-13 16:36:00 
@Last Modified by: Namratha N Shetty
@Last Modified time: 2021-09-13 16:37:00
@Title : To check employee is present or absent
"""

import random
print("Welcome to employee wage computation")

def calculateHour(attendanceStatus):
    """
    Description:
        This function determine the work hours
    Parameter:
        attendanceStatus is used to determine work hour of employee
    Return:
        the functution return 8 or 4 or 0 value as work hour
    """
    if attendanceStatus == isFullTime:
        day_Hour = 8
    elif attendanceStatus == isPartTime:
        day_Hour = 4 
    else:
        day_Hour = 0
    return day_Hour
    
def getWorkHours(totalWorkingHours):
    '''
    Description:
        this function calculate working hours
    '''
    print("Total working hours:", totalWorkingHours)    

def calculateWage():
    """
    Description:
        this function calculate employee wage
    Return:
        this function return total employee wage of a month
    """
    wage_Per_Hour = 20
    working_Days = 0
    total_Working_Hours = 0
    maximum_Working_Days = 20
    maximum_Working_Hours = 100
    total_Wage = 0
    while working_Days < maximum_Working_Days and total_Working_Hours < maximum_Working_Hours:
        attendance = random.randint(0,2)
        attendanceStatus = switcher.get(attendance)
        working_Hours = calculateHour(attendanceStatus)
        total_Wage += working_Hours * wage_Per_Hour
        total_Working_Hours += working_Hours
        working_Days += 1
        getWorkHours(total_Working_Hours)
    return total_Wage


absent = 0
isFullTime = 1
isPartTime = 2

switcher = {
    0: absent,
    1: isFullTime,
    2: isFullTime,
}

print("Total employee wage for month is:",calculateWage())