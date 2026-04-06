def absolute_value(num): # 'num' is the parameter passed into the function
    """This function returns the absolute value of the entered number""" # Docstring
    if num >= 0: # Checks if the number is positive
        return num # Sends the positive number back to where it was called
    else: 
        return -num # Flips a negative number to positive and sends it back 

print(absolute_value(-4)) # Calling the function and printing the returned result 

