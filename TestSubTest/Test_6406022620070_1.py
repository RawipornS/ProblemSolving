total_calories = 0

while True:
    activity = input("กิจกรรม \n1.วิ่ง \n2.ปั่นจักรยาน \n3.ว่ายน้ำ \n4.จบการทำงาน \nป้อนกิจกรรม: ")
    
    if activity == '4':
        break

    try:
        duration = int(input("ป้อนระยะเวลาในการทำกิจกรรม (นาที): "))
    except ValueError:
        print("กรุณาป้อนตัวเลขสำหรับระยะเวลา!")
        continue

    if activity == '1' or 'วิ่ง':
        calories = duration * 10
    elif activity == '2' or 'ปั่นจักรยาน':
        calories = duration * 8
    elif activity == '3' or 'ว่ายน้ำ':
        calories = duration * 5
    else:
        print("\nกิจกรรมที่ป้อนไม่ถูกต้อง กรุณาลองอีกครั้ง!\n")
        continue

    total_calories += calories
    print(f"\nคุณเผาผลาญแคลอรีไป {calories} แคลอรีจากกิจกรรม: {activity}")
    print(f"แคลอรีที่สะสมทั้งหมด: {total_calories} แคลอรี\n")
    print("------------------------------------------------------------")

print("\n============= สรุปผลรวม ==================")
print(f"แคลอรีที่เผาผลาญรวมทั้งหมด: {total_calories} แคลอรี")
print("=========================================")
