n = int(input("Enter number of values:"))

values = []

for i in range(n):
    num=int (input("Enter value (0-3):"))
if 0 <=num <= 3:
    values.append(num)
else:
    print("Invalid input! Please enter a number between 0 and 3 .")
    values.append(0) # Optional: Append 0 for invalid input 
     
t= tuple(values) #Convert list to tuple

count0=t.count(0)
count1=t.count(1)
count2=t.count(2)
count3=t.count(3)

average= sum(t)/len(t)/len(t) #Find average

print("Tuple values:",t)
print("Count of 0s:",count0)
print("Count of 1s:",count1)
print("Count of 2s:",count2)
print("Count of 3s:",count3)
print("Average of values:",average)