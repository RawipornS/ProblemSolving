print("***Convert BMI***")

wieight = float(input("Enter your wieight (kg): "))
height = float(input("Enter your height (cm): "))

bmi = wieight / (height ** 2)

print(f"Your BMI is {bmi: .5f}")