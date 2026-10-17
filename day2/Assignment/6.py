"""
Take the user's age.
Rules:
Age < 13       → Child
13–17          → Teenager
18–59          → Adult
60+            → Senior Citizen

Print the appropriate category.
"""

user_age = int(input("enter the age: "))

if user_age < 0:
    print("Invalid")
elif user_age < 13:
    print("child")
elif user_age <= 17:
    print("teenager")
elif user_age <= 59:
    print("adult")
else:
    print("Senior citizen")