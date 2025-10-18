# Lists and Tuples in Python

# --- Lists ---

# Creating a list
fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)

# Indexing
print("First fruit:", fruits[0])      # 'apple'
print("Last fruit:", fruits[-1])      # 'cherry'

# Slicing
print("First two fruits:", fruits[:2])    # ['apple', 'banana']
print("All except first:", fruits[1:])    # ['banana', 'cherry']

# List methods
fruits.append('date')        # Adds 'date' to the end
print("After append:", fruits)

fruits.insert(1, 'blueberry') # Inserts 'blueberry' at index 1
print("After insert:", fruits)

fruits.remove('banana')      # Removes 'banana' from the list
print("After remove:", fruits)

# Iteration
print("Iterating over list:")
for fruit in fruits:
    print(fruit)

# Other useful methods
print("Number of fruits:", len(fruits))
print("Is 'apple' in list?", 'apple' in fruits)
fruits.sort()
print("Sorted list:", fruits)

# --- Tuples ---

# Creating a tuple
coordinates = (10, 20)
print("\nTuple:", coordinates)

# Indexing
print("First coordinate:", coordinates[0])

# Slicing
print("All except first:", coordinates[1:])

# Immutability
# Tuples cannot be changed after creation
try:
    coordinates[0] = 99
except TypeError as e:
    print("Tuples are immutable:", e)

# Iteration
print("Iterating over tuple:")
for value in coordinates:
    print(value)

# Tuple unpacking
x, y = coordinates
print("Unpacked:", x, y)

# Creating single-element tuple (note the comma)
single = (42,)
print("Single-element tuple:", single)