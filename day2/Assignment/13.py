"""
Take 5 numbers from the user and find the largest number without using max().
This tests whether they understand loops and comparisons.

"""



largest = int(input("enter number 1: "))

for i in range(2,6):
    num = int(input(f"enter number {i}: "))

    if num > largest:
        largest = num

print("largest number", largest)
