# Get the base and exponent from the user
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Start with a result of 1 (since multiplying by 1 changes nothing)
result = 1

# The loop runs 'exponent' amount of times
for i in range(exponent):
    # Multiply the current result by the base
    result *= base

print(f"{base} to the power of {exponent} is {result}")