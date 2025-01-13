# โปรแกรมคำนวณเงินออม
print("โปรแกรมคำนวณเงินออม")

# รับข้อมูลจากผู้ใช้
goal = float(input("กรุณากรอกเป้าหมายเงินออม (บาท): "))
years = int(input("กรุณากรอกระยะเวลา (ปี): "))
frequency = input("เลือกความถี่การออม (วัน/เดือน): ").lower()

# คำนวณเงินออม
if frequency == "วัน":
    savings = goal / (years * 365)
    print(f"คุณต้องออมเงิน {savings:.2f} บาทต่อวัน")
elif frequency == "เดือน":
    savings = goal / (years * 12)
    print(f"คุณต้องออมเงิน {savings:.2f} บาทต่อเดือน")
else:
    print("ความถี่ที่กรอกไม่ถูกต้อง กรุณาเลือก วัน หรือ เดือน")
