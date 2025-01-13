#Big O = O(N)
import time

def sum_even_and_odd(N):
    # การหาผลรวมเลขคู่และเลขคี่ในช่วง 1 ถึง N
    sum_even = 0
    sum_odd = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_even, sum_odd

# รับค่า N จากผู้ใช้
N = int(input("Enter a value for N: "))

# เริ่มจับเวลา
start_time = time.time()

# คำนวณผลรวม
sum_even, sum_odd = sum_even_and_odd(N)

# สิ้นสุดการจับเวลา
end_time = time.time()

# แสดงผลลัพธ์
print(f"Sum of even numbers = {sum_even}")
print(f"Sum of odd numbers = {sum_odd}")

# คำนวณเวลาที่ใช้และแปลงให้เป็นจำนวนเต็ม
time_taken = int((end_time - start_time) * 1000)
print(f"Time taken = {time_taken} ms")

