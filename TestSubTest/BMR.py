print("คำนวณอัตราการเผาผลาญแคลอรี")

weight = int(input("กรุณาป้อนน้ำหนัก (กิโลกรัม): "))
height = int(input("กรุณาป้อนส่วนสูง (เซนติเมตร): "))
age = int(input("กรุณาป้อนอายุ (ปี): "))
sex = input("เลือกเพศ (ชาย/หญิง): ").lower()

if sex == "ชาย":
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    print(f"อัตราการเผาผลาญแคลอรีต่ำสุดต่อวัน (BMR): {bmr:.2f}")
elif sex == "หญิง":
    bmr = 10 * weight + 6.25 * height - 5 * age - 161
    print(f"อัตราการเผาผลาญแคลอรีต่ำสุดต่อวัน (BMR): {bmr:.2f}")
