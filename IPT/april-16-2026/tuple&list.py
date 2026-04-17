# Lesson: Lists vs Tuples in Python
# Introductory Part:
# This lesson introduces two fundamental Python data structures:
# lists and tuples. You will learn what they are, how they differ,
# and when to use each one.
# 
# Learning goals:
#  - Understand the basic definitions of lists and tuples
#  - See how lists are mutable and tuples are immutable
#  - Compare list and tuple syntax
#  - Practice simple examples for both types

# 1) What is a list?
# - A list is an ordered collection of items.
# - Lists are mutable: you can change, add, or remove elements.
# - Lists use square brackets: [ ]

fruits = ["apple", "banana", "cherry"]
print("List example:", fruits)

# Modify a list item
fruits[1] = "blueberry"
print("After change:", fruits)

# Add a new item
fruits.append("date")
print("After append:", fruits)

# Remove an item
fruits.remove("apple")
print("After remove:", fruits)

print()

# 2) What is a tuple?
# - A tuple is an ordered collection of items.
# - Tuples are immutable: once created, you cannot change the items.
# - Tuples use parentheses: ( )

coordinates = (10, 20, 30)
print("Tuple example:", coordinates)

# Accessing tuple values works the same as lists
print("First coordinate:", coordinates[0])
print("Slice of tuple:", coordinates[1:3])

print()

# 3) Side-by-side differences
print("Differences:")
print("- List is mutable")
print("- Tuple is immutable")
print("- List uses [ ]")
print("- Tuple uses ( )")
print("- Lists are best when you need to change items")
print("- Tuples are best when the data should stay constant")

print()

# 4) Practical examples
scores = [85, 90, 78]
print("Original scores list:", scores)
scores[2] = 82
print("Updated scores list:", scores)

race_info = ("Hamilton", "Mercedes", 44)
print("Race info tuple:", race_info)

# 5) Summary
print()
print("Summary:")
print("Use a list when you need a changeable collection.")
print("Use a tuple when the values should remain fixed.")

