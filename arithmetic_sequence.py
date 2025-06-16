# arithmetic_sequence.py
# Program to generate an arithmetic sequence

# Define starting number, common difference, and number of terms
start = 5
difference = 3
terms = 8

# Generate the sequence using list comprehension
sequence = [start + i * difference for i in range(terms)]

# Output the result
print("Arithmetic Sequence:", sequence)