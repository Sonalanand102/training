"""
Take the user's age.
Rules:
Age < 13       → Child
13–17          → Teenager
18–59          → Adult
60+            → Senior Citizen

Print the appropriate category.
"""
age =int(input("enter your age: "))

if age <13:
    print("child")
elif age <17:
    print("Teenager")
elif age < 59:
    print("Adult")
else:
    print("Senior Citizen")

