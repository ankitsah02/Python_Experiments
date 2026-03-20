import math  # import math module for pi

# Lambda function to calculate volume of cone
# Formula: (1/3) * pi * r^2 * h
volume = lambda r, h: (1/3) * math.pi * r * r * h

# Take input
r = float(input("Enter radius: "))
h = float(input("Enter height: "))

# Print result
print("Volume of cone:", volume(r, h))