# Program 3: Cities

with open("city.txt", "r") as file:
    lines = file.readlines()

print("All Cities:")
for line in lines:
    name, pop, area = line.split()
    print(name, pop, area)

print("\nCities with population > 10 lakhs:")
for line in lines:
    name, pop, area = line.split()
    if float(pop) > 10:
        print(name)

# Sum of areas
total_area = 0
for line in lines:
    name, pop, area = line.split()
    total_area += float(area)

print("\nTotal area:", total_area)