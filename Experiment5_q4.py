# Write a program to enter a string and a substring.
# You have to print the number of times that the substring occurs in the given string.

string = input("Enter the main string: ")
substring = input("Enter the substring: ")

count = 0
start = 0

# Traverse string from left to right
while True:
    pos = string.find(substring, start)

    if pos != -1:
        count += 1
        start = pos + 1
    else:
        break

print(count)