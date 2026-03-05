num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Keep looping while the two numbers are not equal
while num1 != num2:
    
    # Check which number is bigger, and subtract the smaller one from it
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1

# When the loop finishes, num1 and num2 will be the same. That is the HCF.
print(f"The HCF (GCD) is {num1}")