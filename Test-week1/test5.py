print("***Convert BMI***")

# รับข้อมูลน้ำหนักและส่วนสูง
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (cm): "))

# แปลงความสูงจากเซนติเมตรเป็นเมตร
height = height / 100

# คำนวณ BMI
bmi = weight / (height ** 2)

# แสดงผลลัพธ์ BMI
print(f"Your BMI is {bmi:.2f}")
