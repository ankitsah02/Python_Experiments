import numpy as np   # Import NumPy

# Create a 3x3 array
arr = np.array([[1, 5, 3],
                [8, 2, 7],
                [4, 9, 6]])

# Print array
print("Array:\n", arr)

# Sum of each row (axis=1 means row-wise)
row_sum = np.sum(arr, axis=1)
print("Row sums:", row_sum)

# Sum of each column (axis=0 means column-wise)
col_sum = np.sum(arr, axis=0)
print("Column sums:", col_sum)

# Find second maximum element
flat = arr.flatten()   # Convert 2D array to 1D
flat.sort()            # Sort array in ascending order
second_max = flat[-2]  # Second largest element

print("Second maximum element:", second_max)