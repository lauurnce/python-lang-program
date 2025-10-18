# File Handling in Python

# 1. Opening and Writing to a Text File
file = open('example.txt', 'w')  # Open for writing (creates file if not exists)
file.write('Hello, world!\n')
file.write('This is a second line.\n')
file.close()  # Always close the file when done

# 2. Reading from a Text File
file = open('example.txt', 'r')  # Open for reading
content = file.read()  # Read entire file
print('File content using read():')
print(content)
file.close()

# 3. Using the with statement (Context Manager)
# This automatically closes the file after the block
with open('example.txt', 'a') as file:  # Open for appending
    file.write('A third line added with "with".\n')

with open('example.txt', 'r') as file:
    print('File content after appending:')
    for line in file:  # Read line by line
        print(line.strip())

# Summary:
# - open() is used to open a file (modes: 'r', 'w', 'a', etc.)
# - read(), write() are used for reading/writing
# - close() closes the file (important for resource management)
# - with statement is preferred for automatic closing