# Taking input and converting it to an integer 
n = int(input('Enter a number: ')) # Prompts the user and converts their string input to an integer
print(n + 100) # Adds 100 to the user's number and prints the result 

# Output Formatting using f-strings (Python 3.6+) 
print(f"I love {'Geeks'} for \"{'Geeks'}!\"") # Directly embeds values into the string

# Output Formatting using the .format() method [cite: 389]
print('{0} and {1}'.format('Geeks', 'Portal')) # Uses index positions to place words
