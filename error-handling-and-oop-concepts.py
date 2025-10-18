# Error Handling & OOP Intro in Python

# --- Exception Handling ---

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    except TypeError:
        print("Error: Invalid input type.")
        result = None
    finally:
        print("Execution completed.")
    return result

print(divide(10, 2))    # Output: 5.0
print(divide(10, 0))    # Output: Error message
print(divide(10, "a"))  # Output: Error message

# --- Introduction to Object-Oriented Programming (OOP) ---

# Class definition
class Animal:
    # Constructor method
    def __init__(self, name, species):
        self.name = name        # Attribute
        self.species = species  # Attribute

    # Method
    def speak(self):
        print(f"{self.name} says hello!")

# Creating objects (instances)
dog = Animal("Buddy", "Dog")
cat = Animal("Whiskers", "Cat")

# Accessing attributes and methods
print(dog.name)        # Output: Buddy
print(cat.species)     # Output: Cat
dog.speak()            # Output: Buddy says hello!
cat.speak()            # Output: Whiskers says hello!

# --- Summary ---
# Exception handling uses try, except, and finally to manage errors gracefully.
# OOP uses classes to define blueprints, objects as instances, and methods for behavior.