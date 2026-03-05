num = int(input("Enter a number to find its factors: "))

# Start checking from 1
divisor = 1

print(f"The factors of {num} are:")

# Keep looping as long as the divisor is less than or equal to the number
while divisor <= num:
    
    # If the remainder is 0 (meaning it divides evenly), it is a factor
    if num % divisor == 0:
        print(divisor)
    
    # Increase the divisor by 1 to check the next number
    divisor += 1