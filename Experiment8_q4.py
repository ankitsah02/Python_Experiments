# Step 1: Write names into file
file = open("name.txt", "w")
file.write("Aman\nRiya\nEkta\nOm\nIshita\nRahul")
file.close()

# Step 2: Read names from file
file = open("name.txt", "r")
names = file.readlines()
file.close()

# Remove newline characters
names = [name.strip() for name in names]

# Count total names
total_names = len(names)

# Count names starting with vowel
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_count = 0

for name in names:
    if name.lower().startswith(vowels):
        vowel_count += 1

# Find longest name
longest_name = max(names, key=len)

# Display results
print("Total names:", total_names)
print("Names starting with vowel:", vowel_count)
print("Longest name:", longest_name)