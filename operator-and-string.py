# Untitled-1
# Short interactive guide: Operators and Strings in Python
# Notes on learning: read docs, try examples in REPL, modify them, build tiny programs, use print() to inspect values.

# ------------------------
# ARITHMETIC OPERATORS
# ------------------------
# +, -, *, /, // (floor div), % (mod), ** (power)
a = 10
b = 3
print("Arithmetic examples:")
print("a =", a, "b =", b)
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)      # float division
print("a // b =", a // b)    # integer division (floor)
print("a % b =", a % b)      # remainder
print("a ** b =", a ** b)    # exponent

# Tip: experiment with negative numbers and floats to understand // and %

print()

# ------------------------
# COMPARISON OPERATORS
# ------------------------
# ==, !=, <, <=, >, >=
print("Comparison examples:")
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a > b ->", a > b)
print("a <= b ->", a <= b)

# Use comparisons in conditionals
if a > b:
    print("a is greater than b")

print()

# ------------------------
# LOGICAL OPERATORS
# ------------------------
# and, or, not — combine boolean expressions
x = True
y = False
print("Logical examples:")
print("x and y ->", x and y)
print("x or y ->", x or y)
print("not x ->", not x)

# Short-circuiting: "and" stops if left is False, "or" stops if left is True.
# Useful for safe expressions like: value = config_value or default_value

print()

# ------------------------
# STRINGS: BASICS
# ------------------------
s = "Hello, World!"
print("String s:", s)
# length
print("len(s) ->", len(s))
# indexing (0-based). Negative indices count from the end.
print("s[0] ->", s[0])
print("s[-1] ->", s[-1])

# slicing: s[start:end] -> includes start, excludes end
print("s[0:5] ->", s[0:5])   # "Hello"
print("s[7:] ->", s[7:])     # "World!"
print("s[:5] ->", s[:5])     # also "Hello"
print("s[::2] ->", s[::2])   # step slicing: every 2nd character

# concatenation and repetition
a = "Hi"
b = "there"
print("Concatenate:", a + " " + b)
print("Repeat:", "ha" * 3)

print()

# ------------------------
# USEFUL STRING METHODS
# ------------------------
t = "  python is FUN  "
print("Original t repr:", repr(t))
print("t.strip() ->", t.strip())         # remove surrounding whitespace
print("t.upper() ->", t.upper())
print("t.lower() ->", t.lower())
print("t.capitalize() ->", t.capitalize())
print("t.title() ->", t.title())
print("t.split() ->", t.split())         # split on whitespace into list
print("t.split(' ') ->", t.split(" "))   # split on exact delimiter
print("t.replace('FUN','fun') ->", t.replace("FUN", "fun"))

# membership test
print("'py' in t ->", "py" in t.lower())

print()

# ------------------------
# USER INPUT (input())
# ------------------------
# Note: input() returns a string. Convert to int/float if you need numbers.
# Simple calculator demo
try:
    x_str = input("Enter first number (or press Enter to skip demo): ").strip()
    if x_str:
        y_str = input("Enter second number: ").strip()
        x_num = float(x_str)
        y_num = float(y_str)
        print(f"{x_num} + {y_num} = {x_num + y_num}")
        print(f"{x_num} / {y_num} = {x_num / y_num if y_num != 0 else 'Infinity (divide by zero)'}")
        print("Comparison x > y ->", x_num > y_num)
    else:
        print("Skipped number demo.")
except ValueError:
    print("Could not parse numbers. Try entering numeric values like 3.5 or -2.")

print()

# String input demo
name = input("Type your name: ").strip()
greeting = "Nice to meet you, " + name.capitalize() + "!"
print(greeting)
sentence = input("Type a short sentence: ").strip()
print("Words in your sentence:", sentence.split())
print("Uppercased:", sentence.upper())

print()

# ------------------------
# PRACTICE SUGGESTIONS (short)
# ------------------------
# 1) Use Python REPL (python or ipython) and type examples line by line.
# 2) Modify values and observe outputs (change indices, slicing steps).
# 3) Write small programs: calculator, word counter, simple input validation.
# 4) Read docs: built-in functions (len, input), string methods, and operators.
# 5) When stuck, use print() to inspect intermediate values.

# Small exercise for you to implement:
# - Count vowels in the input sentence.
# - Reverse the input sentence using slicing.
# - Build a tiny menu that applies transformations (upper, lower, strip) based on user choice.

# End of file.