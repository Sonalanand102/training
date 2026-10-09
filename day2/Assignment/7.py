"""
Take an employee's monthly salary.

Classify:
< 25,000        → Junior
25,000–50,000   → Mid-level
50,001–100,000  → Senior
> 100,000       → Lead

"""
salary = int(input("Enter salary: "))

if salary <25000:
    print("junior")
elif salary < 50000:
    print("mid-level")
elif salary < 100000:
    print("senior")
else:
    print("Lead")
    