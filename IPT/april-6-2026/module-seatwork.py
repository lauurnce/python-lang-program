import sys
from types import ModuleType

calc = ModuleType('calc')

# Given from ma'am Alet
def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers - works with integers and real numbers"""
    if isinstance(x, float) or isinstance(y, float):
        return x * y
    else:
        if y < 0:
            return -multiply(x, -y)
        result = 0
        for _ in range(y):
            result = add(result, x)
        return result

def divide_integer(x, y):
    """Division - works with integers and real numbers"""
    if y == 0:
        return "Error: Division by zero"
    if isinstance(x, float) or isinstance(y, float):
        return x / y
    else:
        result = 0
        temp = x
        if x < 0 or y < 0:
            return x // y  
        while temp >= y:
            temp = subtract(temp, y)
            result = add(result, 1)
        return result

def power(x, y):
    """Calculate x to the power of y - works with integers and real numbers"""
    if isinstance(x, float) or isinstance(y, float) or y < 0:
        return x ** y
    elif y == 0:
        return 1
    else:
        result = x
        for _ in range(y - 1):
            result = multiply(result, x)
        return result

def sum_list(numbers):
    """Sum all numbers in a list using add"""
    result = 0
    for num in numbers:
        result = add(result, num)
    return result

def difference_sum(num1, num2, num3):
    """Calculate (num1 + num2) - num3"""
    sum_val = add(num1, num2)
    result = subtract(sum_val, num3)
    return result

# Add all functions to calc module
calc.add = add
calc.subtract = subtract
calc.multiply = multiply
calc.divide_integer = divide_integer
calc.power = power
calc.sum_list = sum_list
calc.difference_sum = difference_sum

# Registered in sys.modules
sys.modules['calc'] = calc

print("✓ calc module created successfully!")
print("  Functions: add, subtract, multiply, divide_integer, power, sum_list, difference_sum")

print("\n" + "="*60)
print("TESTING WITH INTEGERS")
print("="*60)
print(f"add(5, 3) = {calc.add(5, 3)}")
print(f"subtract(10, 4) = {calc.subtract(10, 4)}")
print(f"multiply(4, 5) = {calc.multiply(4, 5)}")
print(f"divide_integer(20, 4) = {calc.divide_integer(20, 4)}")
print(f"power(2, 5) = {calc.power(2, 5)}")
print(f"sum_list([1, 2, 3, 4, 5]) = {calc.sum_list([1, 2, 3, 4, 5])}")
print(f"difference_sum(10, 5, 3) = {calc.difference_sum(10, 5, 3)}")

print("\n" + "="*60)
print("TESTING WITH REAL NUMBERS (FLOATS)")
print("="*60)
print(f"add(5.5, 3.2) = {calc.add(5.5, 3.2)}")
print(f"subtract(10.7, 4.3) = {calc.subtract(10.7, 4.3)}")
print(f"multiply(4.5, 2.5) = {calc.multiply(4.5, 2.5)}")
print(f"divide_integer(20.5, 4.1) = {calc.divide_integer(20.5, 4.1)}")
print(f"power(2.5, 3) = {calc.power(2.5, 3)}")
print(f"power(2, 0.5) = {calc.power(2, 0.5)}")  # Square root of 2
print(f"sum_list([1.5, 2.5, 3.5, 4.5]) = {calc.sum_list([1.5, 2.5, 3.5, 4.5])}")
print(f"difference_sum(10.5, 5.5, 3.2) = {calc.difference_sum(10.5, 5.5, 3.2)}")

print("\n" + "="*60)
print("TESTING WITH MIXED INTEGERS AND FLOATS")
print("="*60)
print(f"add(5, 3.5) = {calc.add(5, 3.5)}")
print(f"subtract(10.5, 4) = {calc.subtract(10.5, 4)}")
print(f"multiply(4, 2.5) = {calc.multiply(4, 2.5)}")
print(f"divide_integer(20, 4.5) = {calc.divide_integer(20, 4.5)}")
print(f"power(3, 2.5) = {calc.power(3, 2.5)}")
print(f"sum_list([1, 2.5, 3, 4.5, 5]) = {calc.sum_list([1, 2.5, 3, 4.5, 5])}")