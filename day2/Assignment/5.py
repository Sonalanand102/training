"""
Take an integer from the user and determine whether it is:
- Even
- Odd

"""

integer = int(input("enter your number: "))

if integer % 2 == 0:
    print("even:", integer)
else:
    print("odd", integer)