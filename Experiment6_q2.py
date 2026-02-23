# Input
n = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))

# Remove duplicates
unique_scores = list(set(scores))

# Sort the list
unique_scores.sort()

# Runner-up score
print("Runner-up score is:", unique_scores[-2])