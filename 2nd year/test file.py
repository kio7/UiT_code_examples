#This is a test, if i can use this keyboard or not. So far it looks like it will be a challenge since i'm so used to the one i have at home

#BMI
height = float(input("Enter your height in centimeters: "))
weight = float(input("Enter your weight in kilograms: "))

height = height/100
bmi = weight/(height**2)

print(f"your bmi is: {bmi:.1f}")