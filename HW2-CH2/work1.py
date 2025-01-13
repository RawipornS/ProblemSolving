# รับจำนวน N (จำนวนนักศึกษา)
N = int(input("ป้อนจำนวนนักศึกษา: "))

# สร้างลิสต์สำหรับเก็บคะแนนและเกรด
grades = []

# วนลูปรับคะแนนและแปลงเกรด
for i in range(N):
    score = float(input(f"ป้อนคะแนนของนักศึกษาคนที่ {i+1}: "))
    
    # ตรวจสอบช่วงคะแนนและกำหนดเกรด
    if score >= 80:
        grade = "A"
    elif score >= 75:
        grade = "B+"
    elif score >= 70:
        grade = "B"
    elif score >= 65:
        grade = "C+"
    elif score >= 60:
        grade = "C"
    elif score >= 55:
        grade = "D+"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    
    # เก็บเกรดในลิสต์
    grades.append((score, grade))

# แสดงผลคะแนนและเกรด
print("\nผลลัพธ์คะแนนและเกรดของนักศึกษา:")
for i, (score, grade) in enumerate(grades):
    print(f"นักศึกษาคนที่ {i+1}: คะแนน = {score}, เกรด = {grade}")
