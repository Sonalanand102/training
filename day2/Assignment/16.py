"""
Take a password as input.
Rules:
- At least 8 characters
- Must contain at least one digit
- Must not be empty
Print:
Valid password

or
Invalid password

For now, they can solve the digit requirement using a loop rather than advanced libraries.
"""


password = input("enter password: ")

has_digit = False

for i in password:
    if i.isdigit():
        has_digit = True
        break
if len(password) >= 8 and has_digit == True:
    print("valid password")
else:
    print("Invalid")
  