print("Welcome to the BMI Calculator")
print("-----------------------------")

weight = input("Enter in your weight in kilograms: ")
height = input("Enter in your height in meters: ")

bmi = int(weight) / float(height) ** 2
print("Your BMI is", int(bmi))