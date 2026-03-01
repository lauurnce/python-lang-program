num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Use an 'if' statement to find the larger number to start checking from
if num1 > num2:
    greater = num1
else:
    greater = num2

# Use a while loop to keep checking numbers infinitely
while True:
    
    # Check if 'greater' can be divided evenly by BOTH num1 and num2
    if (greater % num1 == 0) and (greater % num2 == 0):
        lcm = greater
        # Once we find it, 'break' stops the while loop immediately
        break 
    
    # If it wasn't the LCM, increase the number by 1 and loop again
    greater += 1

print(f"The LCM of your numbers is {lcm}")