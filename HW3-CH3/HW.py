import time

# รับค่าจากผู้ใช้
N = int(input("กรุณาใส่ค่า N: "))

# เริ่มจับเวลา
start_time = time.time()

# ผลรวมของเลขคู่และเลขคี่
sum_even = 0
sum_odd = 0

# วนลูปตั้งแต่ 1 ถึง N
for i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i  # เลขคู่
    else:
        sum_odd += i   # เลขคี่

# แสดงผลลัพธ์
print(f"Sum of odd numbers = {sum_odd}")
print(f"Sum of even numbers = {sum_even}")

# จับเวลาสิ้นสุด
end_time = time.time()

# แสดงเวลา
print(f"Time taken: {end_time - start_time:.6f} seconds")

# Big O Analysis:
# การวนลูปทั้งหมดเป็น O(N) เพราะเราเดินลูปจาก 1 ถึง N เพียงครั้งเดียว
# ดังนั้น Big O ของโปรแกรมนี้คือ O(N)
