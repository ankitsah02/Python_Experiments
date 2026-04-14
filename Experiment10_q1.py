class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.phy = phy
        self.chem = chem
        self.maths = maths

    # Display student details
    def display(self):
        print("\nName:", self.name)
        print("SAP ID:", self.sap_id)
        print("Physics:", self.phy)
        print("Chemistry:", self.chem)
        print("Maths:", self.maths)

    # Calculate percentage
    def marks_percentage(self):
        total = self.phy + self.chem + self.maths
        percentage = total / 3
        return percentage

    # Display result
    def result(self):
        if self.phy > 40 and self.chem > 40 and self.maths > 40:
            print("Result: PASS")
        else:
            print("Result: FAIL")


# Function to calculate class average
def class_average(students):
    total = 0
    for s in students:
        total += s.marks_percentage()
    return total / len(students)


# Main program
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of student", i+1)
    name = input("Enter name: ")
    sap_id = input("Enter SAP ID: ")
    phy = float(input("Enter Physics marks: "))
    chem = float(input("Enter Chemistry marks: "))
    maths = float(input("Enter Maths marks: "))

    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)

# Display all student details
for s in students:
    s.display()
    print("Percentage:", s.marks_percentage())
    s.result()

# Class average
avg = class_average(students)
print("\nClass Average Percentage:", avg)