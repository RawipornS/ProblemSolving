activity = input("ป้อนกิจกรรม (วิ่ง, ปั่นจักรยาน, ว่ายน้ำ): ")
duration = int(input("ป้อนระยะเวลาในการทำกิจกรรม (นาที): "))

if activity == 'วิ่ง':
    calories = duration * 10
elif activity == 'ปั่นจักรยาน':
    calories = duration * 8
elif activity == 'ว่ายน้ำ':
    calories = duration * 5
else:
    calories = 0
    print("กิจกรรมที่ป้อนไม่ถูกต้อง")

print(f"แคลอรีที่เผาผลาญรวม: {calories} แคลอรี")