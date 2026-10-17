"""
Function : A function is a reusable block of code designed to perform a specific task.

def - initialize a function.
parameters - the values that you pass to a function.
arguments - the values that you pass to a function when you call it.
return - the value that a function gives back after it has finished executing.

note : when we don't return any value inside a function it returns "None" by default.

note : when we return multiple values from a function it will return a tuple.

note: Positional argument cannot appear after keyword arguments.

*args : It allows a function to accept a variable number of positional arguments. Inside the function, they're available as a tuple.

**kwargs : It allows a function to accept a variable number of keyword arguments, which are available as a dictionary.

"""

def greet(name: str | None = None) -> str:
    if name is None:
        return "Hello User"

    return f"Hello {name}"

print(greet("sonal"))