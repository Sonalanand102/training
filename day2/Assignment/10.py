"""
Take n as input and calculate:
1 + 2 + 3 + ... + n

Example:
Input: 5
Output: 15

"""

n = int(input("enter the num: "))

total = 0

for i in range(1, n + 1):
    total += i
print(total)