import numpy as np

# Function to compute A^m
def matrix_power(matrix, exponent):
    return np.linalg.matrix_power(matrix, exponent)

# Main program
if __name__ == "__main__":
    A = np.array([[2, 1], [1, 2]])
    m = 3
    result = matrix_power(A, m)
    print(f"Matrix A raised to power {m}:{result}")
