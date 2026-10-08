## Loops in python 

"""
Types of loops in python:
1. for loop - iterate over a sequence 
2. while loop - repeat while a condition is true

break
 ↓
stop entire loop

continue
 ↓
skip current iteration
 ↓
continue loop

pass does nothing. It's a placeholder where Python expects a statement.

"""

# for i in range(3):
#     for j in range(2):
#         print(i, j)

"""
i j
0 0
0 1
1 0
1 1
2 0
2 1
"""

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

for row in matrix:
    for value in row:
        print(value)