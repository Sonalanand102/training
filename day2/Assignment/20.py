"""
Build a small program that processes multiple users.
For each user, take:
Name
Age
Email

Validate:
- Name should not be empty
- Age should be 18 or above
- Email should contain @

For each user print:
User accepted

or
User rejected

At the end print:
Total users
Accepted users
Rejected users
"""

total_users = int(input("enter the total number: "))

accept = 0
rejected = 0

for i in range(total_users):

    name = input("enter the name: ")
    age = int(input("enter the age: "))
    email = input("enter the email: ")

    if len(name.strip()) >= 1 and age >= 18 and "@" in email:
     print("user accepted")
     accept += 1

    else:
       print("user rejected")
       rejected += 1

print("total users: ", total_users)
print(accept)
print(rejected)

print("name", name)
print("age", age)
print("email", email)

