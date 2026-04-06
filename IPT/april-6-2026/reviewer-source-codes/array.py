# ARRAY EXAMPLE 
from array import * # Must import the array module first 
# Create an array of signed integers ('i' is the typecode) 
array1 = array('i', [10,20,30,40,50]) 

array1.insert(1,60) # Insert the number 60 at index position 1 
array1.remove(40) # Remove the existing element '40' from the array 
array1[2] = 80 # Update the element at index 2 to be 80 

print(array1) # Output the final state of the array after modifications