# Pyramid pattern in Python

rows = 6  # you can change this number to make it bigger

for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
