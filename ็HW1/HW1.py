# รับข้อมูลจากผู้ใช้
price = int(input("กรุณาใส่ราคา: "))
paid = int(input("กรุณาใส่จำนวนเงินที่จ่าย: "))

# ตรวจสอบว่าจ่ายเงินพอหรือไม่
if paid < price:
    print("Error: เงินที่จ่ายไม่เพียงพอ")
else:
    # คำนวณเงินทอน
    change = paid - price
    denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
    
    print("เงินทอน:")
    for denom in denominations:
        count = change // denom
        if count > 0:
            unit = "ใบ" if denom >= 10 else "เหรียญ"
            print(f"{count} {unit} {denom} บาท")
        change %= denom
