# Python Sets
# A set is an unordered collection of unique elements.
# It does not allow duplicate values.

# Creating a set
numbers = {1, 2, 3, 4, 5}
print("Set numbers:", numbers)

# Creating a set from a list
fruits = set(["apple", "banana", "mango", "orange"])
print("Set fruits:", fruits)

# Empty set
empty_set = set()
print("Empty set:", empty_set)

# Adding elements
numbers.add(6)
print("After add(6):", numbers)

# Adding multiple elements
numbers.update([7, 8, 9])
print("After update([7, 8, 9]):", numbers)

# Removing an element
numbers.remove(3)
print("After remove(3):", numbers)

# Discard removes without error if item not found
a = {1, 2, 3}
a.discard(5)
print("After discard(5):", a)

# Pop removes a random element
popped = numbers.pop()
print("Popped element:", popped)
print("Set after pop:", numbers)

# Clear all elements
numbers.clear()
print("After clear():", numbers)

# Checking membership
letters = {"a", "b", "c"}
print("'a' in letters:", "a" in letters)
print("'d' in letters:", "d" in letters)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# Most frequently used set methods/functions
# add(): adds one element
# update(): adds multiple elements
# remove(): removes an element, raises error if missing
# discard(): removes an element without error if missing
# pop(): removes and returns a random element
# clear(): removes all elements
# copy(): returns a shallow copy of the set
# union(): returns a set with all unique elements from both sets
# intersection(): returns common elements
# difference(): returns elements in first set not in second
# symmetric_difference(): returns elements in either set but not both
# issubset(): checks if one set is a subset of another
# issuperset(): checks if one set contains another
# isdisjoint(): checks if sets have no common elements

s1 = {1, 2, 3}
s2 = {2, 3}
print("Copy:", s1.copy())
print("Union method:", s1.union({3, 4, 5}))
print("Intersection method:", s1.intersection({2, 3, 4}))
print("Difference method:", s1.difference({2}))
print("Symmetric difference method:", s1.symmetric_difference({2, 4}))
print("Subset:", s2.issubset(s1))
print("Superset:", s1.issuperset(s2))
print("Disjoint:", s1.isdisjoint({7, 8, 9}))

# Example using set comprehension
squares = {x * x for x in range(1, 6)}
print("Set comprehension:", squares)

# Summary:
# Sets are useful for removing duplicates and checking membership efficiently.
