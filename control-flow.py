# Control Flow in Python

# 1. Conditional Statements: if, elif, else

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

print("\n--- For Loop with range() ---")
# 2. For Loop with range()
for i in range(1, 6):  # Loops from 1 to 5
    print(f"Iteration {i}")

print("\n--- While Loop ---")
# 3. While Loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

print("\n--- break Statement Example ---")
# 4. break Statement
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print("i =", i)

print("\n--- continue Statement Example ---")
# 5. continue Statement
for i in range(1, 6):
    if i == 3:
        print("Skipping i =", i)
        continue
    print("i =", i)

# Summary:
# - 'if', 'elif', 'else' are used for conditional branching.
# - 'for' loops iterate over a sequence (like range()).
# - 'while' loops repeat as long as a condition is True.
# - 'break' exits the loop immediately.
# - 'continue' skips the current iteration and continues with the next.