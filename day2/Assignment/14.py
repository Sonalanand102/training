"""
Given:
user_ids = [101, 205, 309, 412, 518]


Take a user ID as input and print:
User found

or
User not found

Don't use list.index().
"""

user_ids = [101, 205, 309, 412, 518]

user_id = int(input("enter ID: "))

found = False

for i in user_ids:
    if i == user_id:
        found = True
        break

if found:
    print("user found")
else:
    print("User not found")
