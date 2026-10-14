"""

Data Structure : A data structure is a way of organizing and storing data so that it can be accessed, modified, and processed efficiently.

Python has four commonly used built-in data structures:

1. List - [] - A list is an ordered, mutable collection in Python that can store duplicate values and elements of different data types.

2. Tuple - () - A tuple is an ordered, immutable collection in Python that can contain duplicate values and elements of different data types.
3. Set - {} or set()
4. Dictionary = {key : value}
"""
 
## LIST 
skills = ["Python", "FastAPI", "SQL"]


skills[1] = "Django"
 
## append(x) - Adds one item at the end

skills.append("Git")

print("Skill Append \n", skills)

## extend(items) - Adds multiple items

skills.extend(["AWS", "Docker", "SQL", "LLM", "LLM", "RAG"])

print("Skill Extend \n", skills)

## insert(index, value) - Inserts at an index

skills.insert(1, True)

print("Skill Insert \n", skills)

## remove(value) - Removes the first matching value

skills.remove("SQL")

print("Skill Remove \n", skills)

## pop(index) - Removes and returns an item

print("Skill POP \n")

poppedElement = skills.pop(1)

print(poppedElement)

print(skills)

## sort() - Sorts the list in place

skills.sort()

print("Skill Sort \n", skills)

## reverse() - Reverses the current order

skills.reverse()

print("Skill Reverse \n", skills)

## index(value) - Returns the first matching index

print("Skill Index \n")

indexValue = skills.index("Git")

print(indexValue)

print(skills)

## count(value) - Counts occurrences

print("Skill Count \n")

count = skills.count("LLM")

print(count)

print(skills)

## clear() - Removes all elements

# print("Skill Clear \n")

# skills.clear()

# print(skills)

## slicing - list_name[start:stop:step]

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::2])
print(numbers[::-1])

## Iteration through list 

skills = ["Python", "FastAPI", "PostgreSQL"]

for skill in skills:
    print(skill)

## enumerate()

for index, skill in enumerate(skills):
    print(index, skill)

## nested List 

students = [
    ["Rahul", 85],
    ["Priya", 92],
    ["Aman", 78]
]

print(students[0])
print(students[0][0])
print(students[1][1])

## List Comprehension - List comprehension is useful for readable, compact transformations. Complex logic is often clearer in a normal loop.

## Traditional approach:

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

## Using List Comprehension

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers if number % 2 == 0]

print(squares)

