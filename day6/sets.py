"""
sets : A set is a mutable collection of unique, hashable elements in Python. It does not support positional indexing and does not guarantee a particular iteration order.

discard() does not raise an error if the element is absent.

Union "|": All unique elements from both sets. 

Intersection "&": Elements present in both sets.

Difference "-": Elements in the first set but not in the second. 

Symmetric difference "^": Elements present in either set, but not in both.
"""

"""skills = {"Python", "SQL"}

skills.add("FastAPI")
skills.discard("Sonal")
skills.remove("Java")

print(skills)"""

frontend = {"React", "JavaScript", "CSS"}
backend = {"Python", "SQL", "JavaScript"}

print(frontend | backend)

print(frontend & backend)

print(frontend - backend)

print(frontend ^ backend)