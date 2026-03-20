# Take list input from user
l = list(map(int, input("Enter elements: ").split()))

# Lambda function returns tuple (max, min)
result = lambda x: (max(x), min(x))

# Print result
print("Max and Min:", result(l))