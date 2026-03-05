print("--- Numbers 0-9 ---")
# ASCII for 0 is 48, and 9 is 57. We go up to 58 because the range stops 1 number early.
for i in range(48, 58):
    print(f"Character: {chr(i)} | Value: {i}")

print("\n--- Uppercase A-Z ---")
# ASCII for A is 65, and Z is 90.
for i in range(65, 91):
    print(f"Character: {chr(i)} | Value: {i}")

print("\n--- Lowercase a-z ---")
# ASCII for a is 97, and z is 122.