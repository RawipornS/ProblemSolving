sum_even = 0 
sum_odd = 0

print("*** Calculate sum of odd and even numbers (Exit press 0) ***")

while True:
    num = int(input("Enter number: "))
    if num == 0:
        break

    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
        
print("Sum of even numbers =", sum_even)
print("Sum of odd numbers =", sum_odd)