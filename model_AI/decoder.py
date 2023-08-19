import torch
import torch.nn as nn
import random

# Define a simple character-level decoder model using PyTorch
class CharacterDecoder(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(CharacterDecoder, self).__init__()
        self.hidden_size = hidden_size
        self.embedding = nn.Embedding(input_size, hidden_size)
        self.gru = nn.GRU(hidden_size, hidden_size)
        self.out = nn.Linear(hidden_size, output_size)

    def forward(self, input_char, hidden):
        embedded = self.embedding(input_char.view(1, -1))
        output, hidden = self.gru(embedded.view(1, 1, -1), hidden)
        output = self.out(output.view(1, -1))
        return output, hidden

    def init_hidden(self):
        return torch.zeros(1, 1, self.hidden_size)

# Define the characters and their mapping to indices
characters = "abcdefghijklmnopqrstuvwxyz"
char_to_index = {char: i for i, char in enumerate(characters)}
index_to_char = {i: char for i, char in enumerate(characters)}

# Create the decoder model
decoder_model = CharacterDecoder(len(characters), 128, len(characters))

# Initialize the hidden state
hidden = decoder_model.init_hidden()

# Generate a sequence of characters starting with "user"
input_char = char_to_index['u']  # Start with 'u'
decoded_sequence = ['u']

# Generate 10 random characters
for _ in range(10):
    output, hidden = decoder_model(torch.tensor([input_char]), hidden)
    # Sample the next character from the output probabilities
    topv, topi = output.topk(1)
    next_char_index = topi.squeeze().item()
    next_char = index_to_char[next_char_index]
    decoded_sequence.append(next_char)
    input_char = char_to_index[next_char]

# Convert the decoded sequence to a string
decoded_string = ''.join(decoded_sequence)

# Print the generated string
print(decoded_string)
