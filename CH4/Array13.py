import array as arr

# สร้าง array ชนิด int
a = arr.array('i', [1, 2, 3])

# แสดงผล array ก่อนการเพิ่มข้อมูล
print("Array before operations: ", end=" ")
for i in a:
    print(i, end=" ")
print()

# เพิ่มค่า 4 ในตำแหน่งที่ 1
a.insert(1, 4)  # เพิ่ม 4 ที่ตำแหน่ง index 1

# เพิ่มค่า 5 ลงใน array (ท้ายสุด)
a.append(5)

# ลบค่า 2 ออกจาก array
a.remove(2)

# แสดงผล array หลังการเพิ่มและลบข้อมูล
print("Array after adding 4 and 5 and removing 2: ", end=" ")
for i in a:
    print(i, end=" ")
print()
