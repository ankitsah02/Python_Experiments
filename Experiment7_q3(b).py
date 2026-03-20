# Take input for first list (keys)
list1 = input("Enter keys: ").split()

# Take input for second list (values)
list2 = input("Enter values: ").split()

# Create dictionary using zip()
# zip() pairs elements of both lists
d = dict(zip(list1, list2))

# Print dictionary
print("Dictionary:", d)