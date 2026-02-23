string = input("Enter a string: ")

count = 0

for ch in string:
    if 'A' <= ch <= 'Z':
        count += 1

print("Number of capital letters:", count)
