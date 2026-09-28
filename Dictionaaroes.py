# Python Dictionaries
# A dictionary stores data as key-value pairs.
# Keys must be unique and immutable, while values can be any type.

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python",
    "marks": 95
}

print("Student dictionary:", student)

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))

# Adding or updating values
student["city"] = "Lahore"
student["age"] = 21
print("Updated dictionary:", student)

# Removing items
student.pop("marks")
print("After pop:", student)

# Using del
del student["city"]
print("After del:", student)

# Copying a dictionary
copy_student = student.copy()
print("Copied dictionary:", copy_student)

# Dictionary methods/functions most frequently used

# 1. dict.clear() - removes all items
student.clear()
print("After clear:", student)

# Recreate dictionary for more examples
student = {
    "name": "Bob",
    "age": 22,
    "course": "Java",
    "city": "Karachi"
}

# 2. dict.get(key, default) - returns value or default if key not found
print("Get name:", student.get("name"))
print("Get phone:", student.get("phone", "Not Found"))

# 3. dict.keys() - returns all keys
print("Keys:", student.keys())

# 4. dict.values() - returns all values
print("Values:", student.values())

# 5. dict.items() - returns key-value pairs
print("Items:", student.items())

# 6. dict.update() - adds or updates items from another dictionary
new_data = {"marks": 88, "country": "Pakistan"}
student.update(new_data)
print("After update:", student)

# 7. dict.pop(key) - removes and returns the value of key
removed_value = student.pop("city")
print("Removed value:", removed_value)
print("Dictionary after pop:", student)

# 8. dict.popitem() - removes the last inserted key-value pair
last_item = student.popitem()
print("Removed last item:", last_item)
print("Dictionary after popitem:", student)

# 9. dict.setdefault(key, default) - inserts key if not exists
student.setdefault("grade", "A")
print("After setdefault:", student)

# 10. dict.fromkeys(keys, value) - creates dictionary from keys
subjects = ["Math", "Physics", "Chemistry"]
subject_dict = dict.fromkeys(subjects, "Not Started")
print("Fromkeys example:", subject_dict)

# 11. len(dict) - returns number of key-value pairs
print("Length:", len(student))

# 12. in operator - checks if a key exists
print("Does 'name' exist?", "name" in student)

# 13. dict.copy() - copies dictionary
student_copy = student.copy()
print("Copy:", student_copy)

# 14. dict.clear() - empties dictionary
student.clear()
print("Final empty dictionary:", student)

# Example of nested dictionary
employee = {
    "name": "Rahim",
    "details": {
        "age": 25,
        "department": "IT"
    }
}
print("Nested dictionary:", employee)
print("Employee age:", employee["details"]["age"])

# Summary:
# Dictionaries are used to store data in key-value pairs.
# They are very useful for fast lookup and storing structured information.
