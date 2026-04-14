import numpy as np   # Import NumPy

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Perform matrix multiplication
result = np.dot(A, B)

# Display matrices and result
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Multiplication Result:\n", result)