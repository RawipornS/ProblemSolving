def calculate_change(price, paid): 
    if paid < price:
        return "Error: เงินที่จ่ายไม่เพียงพอ"
    
    change = paid - price
    denominations = [1000, 500, 100, 50, 20, 10, 5, 1]
    denomination_names = {1000: 'แบงค์ 1000', 500: 'แบงค์ 500', 100: 'แบงค์ 100', 50: 'แบงค์ 50', 
                          20: 'แบงค์ 20', 10: 'เหรียญ 10', 5: 'เหรียญ 5', 1: 'เหรียญ 1'}
    
    result = {}
    total_change = 0

    for denom in denominations:
        count = change // denom
        if count > 0:
            if denom >= 10:
                result[denomination_names[denom]] = f"{count} ใบ"
            else:
                result[denomination_names[denom]] = f"{count} เหรียญ"
            total_change += count * denom
        change %= denom
    
    return result, total_change

# รับข้อมูลจากผู้ใช้
price = int(input("กรุณาใส่ราคา: "))
paid = int(input("กรุณาใส่จำนวนเงินที่จ่าย: "))

# คำนวณการทอนเงิน
result = calculate_change(price, paid)

# ตรวจสอบผลลัพธ์ที่ได้รับ
if isinstance(result, tuple) and len(result) == 2:
    result, total_change = result
    print(f"ผลรวมเงินทอน: {total_change} บาท")
    for denomination, count in result.items():
        print(f"{denomination}: {count}")
else:
    print(result)  # แสดงข้อความผิดพลาด
