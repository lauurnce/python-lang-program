num = int(input("Enter a number to find its factorial: "))

factorial = 1
counter = 1

# First, check if the number is negative or zero using 'if'
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # If it's a positive number, use a while loop to multiply
    while counter <= num:
        factorial = factorial * counter
        # Move to the next number
        counter += 1
        
    print(f"The factorial of {num} is {factorial}")