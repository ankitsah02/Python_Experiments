# Program 2: Numbers

with open("numbers.txt", "r") as file:
    numbers = list(map(int, file.read().split()))

# Maximum number
print("Maximum number:", max(numbers))

# Average
avg = sum(numbers) / len(numbers)
print("Average:", avg)

# Count numbers > 100
count = 0
for num in numbers:
    if num > 100:
        count += 1

print("Numbers greater than 100:", count)