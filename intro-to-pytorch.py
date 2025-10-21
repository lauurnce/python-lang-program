# PyTorch is a popular deep learning library for Python.
# It provides tools for building neural networks and running computations on GPUs.

import torch
import torch.nn as nn
import torch.optim as optim

# 1. Tensors: PyTorch's basic data structure (like NumPy arrays, but with GPU support)
x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print("Tensor x:\n", x)

# 2. Simple Neural Network Definition
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        # Linear layer: input size 2, output size 1
        self.fc = nn.Linear(2, 1)
    
    def forward(self, x):
        # Forward pass: apply linear layer
        return self.fc(x)

# Instantiate the network
model = SimpleNet()
print("Model structure:\n", model)

# 3. Example input data (batch of 3 samples, each with 2 features)
inputs = torch.tensor([[0.5, 1.5], [2.0, 3.0], [1.0, 2.0]])
# Example target outputs
targets = torch.tensor([[1.0], [2.0], [1.5]])

# 4. Forward pass: get predictions
outputs = model(inputs)
print("Model outputs:\n", outputs)

# 5. Loss function: measures prediction error
criterion = nn.MSELoss()
loss = criterion(outputs, targets)
print("Loss value:", loss.item())

# 6. Optimizer: updates model weights to minimize loss
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 7. Training step: backward pass and weight update
optimizer.zero_grad()   # Clear previous gradients
loss.backward()         # Compute gradients
optimizer.step()        # Update weights

# PyTorch is used for:
# - Building neural networks (like above)
# - Training models with automatic differentiation
# - Running computations on GPUs for speed
# - Research and production in deep learning

# This code shows a simple workflow: define a model, compute outputs, calculate loss, and update weights.