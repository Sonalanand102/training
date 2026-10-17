"""
Take n as input and print numbers from:
1 → n

Example:
Input: 5

Output:
1
2
3
4
5

"""

n = int(input("enter the value: "))

for _ in range(1, n + 1):
    print(_)