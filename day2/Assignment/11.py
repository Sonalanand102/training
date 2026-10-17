"""
Take n as input and print how many even numbers exist between 1 and n.
Example:
Input: 10
Output: 5

"""

n = int(input("enter the number: "))

count = 0

for i in range(1, n+1):
    if i % 2 == 0:
        count += 1
print(count)


