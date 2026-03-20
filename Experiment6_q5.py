# Create a dictionary of n persons where key is name and value is city.
# a) Display all names
# b) Display all city names
# c) Display SAP ID, student name and city
# d) Count number of students in each city

# Take number of students
n = int(input("Enter number of students: "))

# Create an empty dictionary
# Key = student number (1, 2, 3...)
# Value = dictionary containing sap id, name, and city
students = {}

# Taking input for each student
for i in range(1, n + 1):
    sap_id = input("Enter SAP ID: ")
    name = input("Enter student name: ")
    city = input("Enter city: ")

    # Store details in dictionary
    students[i] = {"sap id": sap_id, "name": name, "city": city}

# a) Display all names
print("\nAll Student Names:")
for details in students.values():   # built-in function values() to access student details
    print(details["name"])

# b) Display all city names
print("\nAll City Names:")
for details in students.values():
    print(details["city"])

# c) Display SAP ID, student name and city
print("\nSAP ID, Student Name and City:")
for details in students.values():
    print(details["sap id"], "-", details["name"], "-", details["city"])

# d) Count number of students in each city
city_count = {}

for details in students.values():
    city = details["city"]
    city_count[city] = city_count.get(city, 0) + 1   # built-in function get() to count students in each city

print("\nNumber of Students in Each City:")
for city, count in city_count.items():
    print(city, ":", count)