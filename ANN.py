import torch
import torch.nn as nn

# Assign inputs to the neuron
inputs = torch.tensor([3.0, 2.0, -1.0])

# Create neuron with 3 feature and 1 output
neuron = nn.Linear(in_features=3, out_features=1)
output = neuron(inputs)

# Print output
print(output)