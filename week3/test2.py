while True:
    start = int(input("ป้อนตัวเลขเริ่มต้น: "))
    end = int(input("ป้อนตัวเลขสิ้นสุด: "))
    divisor = int(input("ป้อนตัวเลขที่ต้องการหารลงตัว: "))

    print(f"\nตัวเลขที่อยู่ระหว่าง {start} ถึง {end} ที่หาร {divisor} ลงตัว ได้แก่:")
    for num in range(start + 1, end):
        if num % divisor == 0:
            print(num)

    stop = input("\nพิมพ์ 0 เพื่อหยุดการทำงาน หรือกด Enter เพื่อทำงานต่อ: ")
    if stop == "0":
        print("จบการทำงาน")
        break