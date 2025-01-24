# BigO = O(N) 
import time

def calculate_sums(N):
    sum_odd = 0
    sum_even = 0
    for i in range(1, N + 1):
        if i % 2 == 0:
            sum_even += i
        else:
            sum_odd += i
    return sum_odd, sum_even

N = int(input("Enter N: "))
start_time = time.time()
sum_odd, sum_even = calculate_sums(N)
end_time = time.time()

print(f"Sum of odd numbers: {sum_odd}")
print(f"Sum of even numbers: {sum_even}")
print(f"Time taken: {end_time - start_time:.5f} seconds")