"""
Dictionary : A dictionary is a mutable mapping that stores key-value pairs, where keys are unique and hashable.

The .get() method lets you supply a default value when the key is absent. The default value of get() method will be None.

keys() returns a view of the keys.

values() returns a view of the values.

items() returns a view of the key-value pairs.

"""

candidate = {
    "id": 1,
    "name": "Rahul",
    "experience": 2,
    "skills": ["Python", "FastAPI"]
}

"""

candidate["email"] = "rahul@example.com"

candidate["experience"] = 3

print(candidate.keys())
print(candidate.values())
print(candidate.items())"""

candidates = {
    1: {
        "name": "Rahul",
        "skills": ["Python", "FastAPI"]
    },
    2: {
        "name": "Priya",
        "skills": ["React", "Node.js"]
    }
}

print(candidates[1]["name"])
print(candidates[2]["skills"])

