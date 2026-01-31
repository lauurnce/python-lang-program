# BAD LAYOUT
# Too long (over 79 chars) and no indentation logic.
def train_ai_model(input_data, target_data, learning_rate, epochs, batch_size, optimizer, loss_function): print("Training started...")

# GOOD LAYOUT (PEP 8 Compliant)
# Broken into lines, aligned vertically, 4-space indentation.
def train_ai_model(input_data, target_data, 
                   learning_rate, epochs, 
                   batch_size, optimizer):
    print("Training started...") 