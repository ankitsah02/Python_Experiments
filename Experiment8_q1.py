# Program 1: Names

with open("name.txt", "r") as file:
    names = [line.strip() for line in file]

# Total names
print("Total names:", len(names))

# Names starting with vowel
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_count = 0

for name in names:
    if name.lower().startswith(vowels):
        vowel_count += 1

print("Names starting with vowel:", vowel_count)

# Longest name
longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name

print("Longest name:", longest)
