# รับจำนวน N (จำนวนพนักงาน)
N = int(input("ป้อนจำนวนพนักงาน: "))

# สร้างลิสต์สำหรับเก็บข้อมูลเงินเดือน
salaries = []

# วนลูปคำนวณเงินเดือนพนักงานแต่ละคน
for i in range(N):
    hours = float(input(f"ป้อนจำนวนชั่วโมงการทำงานของพนักงานคนที่ {i+1}: "))
    rate = float(input(f"ป้อนอัตราค่าแรงต่อชั่วโมงของพนักงานคนที่ {i+1}: "))
    
    # คำนวณเงินเดือน
    if hours <= 160:
        salary = hours * rate
    else:
        # ชั่วโมงเกิน 160 คิด OT ที่อัตรา 1.5 เท่า
        overtime_hours = hours - 160
        salary = (160 * rate) + (overtime_hours * rate * 1.5)
    
    # เก็บเงินเดือนในลิสต์
    salaries.append((hours, salary))

# แสดงผลจำนวนชั่วโมงและเงินเดือน
print("\nผลลัพธ์ชั่วโมงการทำงานและเงินเดือนของพนักงาน:")
for i, (hours, salary) in enumerate(salaries):
    print(f"พนักงานคนที่ {i+1}: ชั่วโมง = {hours}, เงินเดือน = {salary:.2f}")
