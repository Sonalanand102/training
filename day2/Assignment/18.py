"""
Given:
attendance = ["P", "P", "A", "P", "A", "P", "P"]


Calculate:
- Total working days
- Present days
- Absent days
- Attendance percentage
Expected:
Working Days: 7
Present: 5
Absent: 2
Attendance: 71.43%
"""

attendance = ["P", "P", "A", "P", "A", "P", "P"]

Total_working_days = len(attendance)

present = 0
absent = 0

for i in attendance:
    if i == "P":
        present += 1
    elif i == "A":
        if i == "A":
         absent += 1

percentage = present/Total_working_days * 100

print(Total_working_days)
print("present", present)
print("absent", absent)
print(percentage)
       


       