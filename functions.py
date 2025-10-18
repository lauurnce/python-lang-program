# Python Functions: Definitions, Parameters, Scope, and Modules

# 1. Defining Functions
def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}!")

greet("Alice")  # Calling the function with a positional argument

# 2. Function Parameters and Arguments

# Positional arguments
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add(3, 5)
print("Sum:", result)

# Keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="Bob")  # Using keyword arguments

# Default parameter values
def power(base, exponent=2):
    """Returns base raised to the power of exponent (default is 2)."""
    return base ** exponent

print("Power:", power(4))         # Uses default exponent=2
print("Power:", power(4, 3))      # Overrides default exponent

# 3. The return Statement

def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

product = multiply(6, 7)
print("Product:", product)

# 4. Variable Scope (Local vs. Global)

global_var = "I am global!"

def scope_demo():
    local_var = "I am local!"
    print(global_var)  # Accessing global variable
    print(local_var)   # Accessing local variable

scope_demo()
# print(local_var)  # Uncommenting this will cause an error (local_var is not defined globally)

# Modifying global variables inside functions
counter = 0

def increment():
    global counter
    counter += 1

increment()
print("Counter:", counter)

# 5. Importing Basic Modules

import math
import random

# Using math module
print("Square root of 16:", math.sqrt(16))
print("Pi value:", math.pi)

# Using random module
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from a list:", random.choice(['apple', 'banana', 'cherry']))

# --- Best Practices ---
# - Use descriptive function names and docstrings.
# - Prefer keyword arguments for clarity.
# - Use default parameters to make functions flexible.
# - Limit use of global variables; prefer local scope.
# - Import only necessary modules/functions.
# - Test functions with different arguments.

# --- Try It Yourself ---
# 1. Define your own function with multiple parameters.
# 2. Experiment with local and global variables.
# 3. Use math and random modules in your own functions.