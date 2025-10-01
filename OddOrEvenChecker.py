def check_even_odd():
    """
    Prompts the user for a whole number and determines if it is even or odd.
    """
    while True:
        # Get input from the user
        user_input = input("Enter a whole number (integer): ")

        try:
            # Convert the input to an integer
            number = int(user_input)

            # The modulo operator (%) returns the remainder of a division.
            # If a number is divisible by 2 (remainder is 0), it's even.
            if number % 2 == 0:
                print(f"The number {number} is **Even**.")
            else:
                print(f"The number {number} is **Odd**.")

            # Exit the loop once a valid number is processed
            break

        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a valid whole number (integer) only.")

# Call the function to run the code
check_even_odd()