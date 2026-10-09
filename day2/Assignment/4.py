"""
Take a username and password as input.
Print:
Login successful

if:
username == "admin"
password == "python123"

Otherwise print:
Invalid credentials

"""

username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "python123":
   print("login successful")
else:
   print("Invalid credentials")