weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height * height)

print("BMI =", round(bmi, 2))

if bmi < 15:
    print("Category: Starvation")
elif 15.1 <= bmi <= 17.5:
    print("Category: Anorexic")
elif 17.6 <= bmi <= 18.5:
    print("Category: Underweight")
elif 18.6 <= bmi <= 24.9:
    print("Category: Ideal")
elif 25 <= bmi <= 29.9:
    print("Category: Overweight")
elif 30 <= bmi <= 39.9:
    print("Category: Obese")
else:
    print("Category: Morbidly Obese")
