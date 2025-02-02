# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# Input number of terms
num_terms = int(input("Enter the number of terms: "))

# Generate Fibonacci sequence
fib_sequence = fibonacci(num_terms)

# Print result
print("Fibonacci sequence:", fib_sequence)
