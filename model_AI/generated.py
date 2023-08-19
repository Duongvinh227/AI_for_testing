import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random

# Define a simple sequence-to-sequence model using PyTorch
class Seq2SeqGenerator(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Seq2SeqGenerator, self).__init__()
        self.hidden_size = hidden_size
        self.encoder = nn.Linear(input_size, hidden_size)
        self.decoder = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.encoder(x))
        x = torch.softmax(self.decoder(x), dim=1)
        return x

# Create a seq2seq generator model
gen_model = Seq2SeqGenerator(100, 128, 26)

# Generate a random noise vector
noise = torch.randn(1, 100)

# Generate user_data using the seq2seq generator model
generated_user_data = gen_model(noise).detach().numpy()

# Decode the generated user_data
generated_username = ''.join([chr(ord('a') + np.argmax(generated_user_data))])
generated_password = ''.join([chr(ord('a') + np.argmax(generated_user_data))])

user_data = {"username": generated_username, "password": generated_password}

# Print the generated user_data
print(user_data)
