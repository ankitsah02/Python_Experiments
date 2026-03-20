# Function to calculate sum of cubes of numbers less than n
def sum_cubes(n):
    s = 0  # initialize sum
    
    # Loop from 1 to n-1
    for i in range(1, n):
        s += i ** 3  # add cube of each number
    
    return s  # return result

# Take input
n = int(input("Enter number: "))

# Print result
print("Sum of cubes:", sum_cubes(n))