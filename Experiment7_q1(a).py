# Function to print numbers from 1 to n using recursion
def print_n(n):
    # Base case: stop when n becomes 0
    if n == 0:
        return
    
    # Recursive call: call function with n-1
    print_n(n - 1)
    
    # Print current value after recursive call
    print(n)

# Take input from user
n = int(input("Enter n: "))

# Function call
print_n(n)