def calculate_gpa(grades):
    """
    ฟังก์ชันคำนวณเกรดเฉลี่ยแบบมีหน่วยกิต
    :param grades: รายการที่เก็บคู่ของ (เกรด, หน่วยกิต) [(grade, credit)]
    :return: เกรดเฉลี่ย (GPA) (float)
    """
    total_points = 0
    total_credits = 0

    for grade, credit in grades:
        total_credits += credit
        total_points += grade_to_point(grade) * credit

    if total_credits == 0:
        return 0  # ถ้าไม่มีหน่วยกิตเลย

    return total_points / total_credits


def grade_to_point(grade):
    """
    แปลงเกรดเป็นค่าคะแนน (Grade Points)
    :param grade: เกรด (A, B, C, D, F)
    :return: ค่าคะแนน (4.0, 3.0, 2.0, 1.0, 0.0)
    """
    grade_mapping = {
        "A": 4.0,
        "B": 3.0,
        "C": 2.0,
        "D": 1.0,
        "F": 0.0
    }
    return grade_mapping.get(grade.upper(), 0)


# รับข้อมูลจากผู้ใช้
grades = []
print("กรุณาใส่เกรดและหน่วยกิตของแต่ละวิชา (พิมพ์ 'done' เมื่อเสร็จ):")

while True:
    grade = input("ใส่เกรด (A, B, C, D, F): ").upper()
    if grade == "DONE":
        break

    if grade not in ["A", "B", "C", "D", "F"]:
        print("กรุณาใส่เกรดที่ถูกต้อง (A, B, C, D, F)")
        continue

    try:
        credit = float(input("ใส่หน่วยกิต: "))
        if credit <= 0:
            print("หน่วยกิตต้องมากกว่า 0")
            continue
        grades.append((grade, credit))
    except ValueError:
        print("กรุณาใส่ตัวเลขสำหรับหน่วยกิต")

# คำนวณเกรดเฉลี่ย
gpa = calculate_gpa(grades)
print(f"เกรดเฉลี่ย (GPA): {gpa:.2f}")
