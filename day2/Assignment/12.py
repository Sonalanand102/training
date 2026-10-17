"""
Take a number and print its multiplication table from 1 to 10.
Example:
Input: 5

5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

"""

num = int(input("enter the num: "))

for i in range(1, 11):
   print(f"{num} * {1} = {i * num}")