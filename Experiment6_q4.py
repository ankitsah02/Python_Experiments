# EXPERIMENT 6 (ii)

# Entering all the course marks in a semester and add all the marks to get total and average.
# Get the subject in which you score highest marks.

# Take input from user, split it by space, convert each value to integer
# and store all marks in a tuple
marks = tuple(int(x) for x in input("Enter marks separated by space: ").split())

# Calculate the total of all marks using built-in sum() function
total_marks = sum(marks)

# Calculate the average marks
# len(marks) gives the total number of subjects
average_marks = total_marks / len(marks)

# Find the highest marks using built-in max() function
highest_marks = max(marks)

# Display the total marks
print("Total Marks:", total_marks)

# Display the average marks
print("Average Marks:", average_marks)

# Display the highest marks
print("Highest Marks:", highest_marks)