# รับข้อมูลจากผู้ใช้
hours = float(input("กรอกจำนวนชั่วโมงการทำงาน: "))
rate = float(input("กรอกอัตราค่าจ้างรายชั่วโมง: "))

# คำนวณเงินเดือน
if hours <= 160:
    total_salary = hours * rate
    ot_hours = 0
    ot_salary = 0
else:
    normal_salary = 160 * rate
    ot_hours = hours - 160
    ot_salary = ot_hours * rate * 1.5
    total_salary = normal_salary + ot_salary

# แสดงผลลัพธ์
print(f"เงินเดือนรวม: {total_salary:.2f} บาท")
print(f"ชั่วโมง OT: {ot_hours} ชั่วโมง")
print(f"เงิน OT: {ot_salary:.2f} บาท")
