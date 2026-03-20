# Function with two parameters
def student(name, age):
    print("Name:", name)
    print("Age:", age)

# Calling function using keyword arguments (order does not matter)
student(age=20, name="Ankit")

# Function with default value for b
def add(a, b=10):
    print("Sum:", a + b)

# Call with both arguments
add(5, 20)

# Call with one argument (b takes default value)
add(5)

# Function that can take multiple values
def total(*numbers):
    sum = 0
    
    # Loop through all values
    for n in numbers:
        sum += n
    
    print("Total:", sum)

# Function call with multiple arguments
total(10, 20, 30, 40)