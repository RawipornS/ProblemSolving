start = int(input("ป้อนตัวเลขเริ่มต้น: "))
end = int(input("ป้อนตัวเลขเริ่มต้น: "))

print("ตัวเลขที่หาร 3 ลงตัวได้แก่: ")

for num in range(start + 1,end):
    if num % 3 == 0:
        print(num)

