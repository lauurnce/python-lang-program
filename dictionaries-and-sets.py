# Dictionaries and Sets in Python

# --- Dictionaries ---

# Creating a dictionary
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"])      # Output: Alice
print(person.get("age"))   # Output: 30

# Modifying values
person["age"] = 31
person["email"] = "alice@example.com"  # Adding a new key-value pair

# Iterating over dictionary
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key} -> {value}")

# Removing a key-value pair
del person["city"]

# Checking if a key exists
if "email" in person:
    print("Email is present.")

# Dictionary methods
keys = person.keys()      # Returns all keys
values = person.values()  # Returns all values
items = person.items()    # Returns all key-value pairs

# --- Sets ---

# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Adding elements
fruits.add("orange")

# Removing elements
fruits.remove("banana")   # Raises error if not present
fruits.discard("pear")    # Does nothing if not present

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a | set_b         # {1, 2, 3, 4, 5, 6}
intersection = set_a & set_b  # {3, 4}
difference = set_a - set_b    # {1, 2}
symmetric_diff = set_a ^ set_b # {1, 2, 5, 6}

print("Union:", union)
print("Intersection:", intersection)
print("Difference:", difference)
print("Symmetric Difference:", symmetric_diff)

# Iterating over a set
for fruit in fruits:
    print(fruit)

# --- List Comprehensions ---

# Basic list comprehension
squares = [x*x for x in range(10)]  # [0, 1, 4, ..., 81]

# Filtering with list comprehension
even_squares = [x*x for x in range(10) if x % 2 == 0]  # [0, 4, 16, 36, 64]

# Dictionary comprehension
square_dict = {x: x*x for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# Set comprehension
unique_lengths = {len(fruit) for fruit in fruits}  # e.g., {5, 6}

# --- Summary ---
# - Dictionaries store key-value pairs, allow fast lookup, and are mutable.
# - Sets store unique elements, support mathematical set operations, and are unordered.
# - Comprehensions provide concise ways to create lists, dictionaries, and sets.

# Practice: Try modifying, iterating, and performing operations on your own dictionaries and sets!