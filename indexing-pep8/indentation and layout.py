# EXAMPLE 1: FUNCTION
# BAD LAYOUT
# Too long (over 79 chars) and no indentation logic.
def train_ai_model(input_data, target_data, learning_rate, epochs, batch_size, optimizer, loss_function): print("Training started...")

# GOOD LAYOUT
# Broken into lines, aligned vertically, 4-space indentation.
def train_ai_model(input_data, target_data, learning_rate,
                   epochs, batch_size, optimizer):
  print("Training started...")


# EXAMPLE 2: IF-STATEMENT
# BAD LAYOUT
if (one_boolean_thing and other_boolean_thing): print("Done")

# GOOD LAYOUT
if (one_boolean_thing and
    other_boolean_thing):
    print("Done")

if (one_boolean_thing
        and other_boolean_thing):
    print("Done")


# EXAMPLE 3: LONG LIST
# BAD LAYOUT
long_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# GOOD LAYOUT
long_list = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
]