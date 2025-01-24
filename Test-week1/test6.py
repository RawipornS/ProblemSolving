print("***Calculate the sum between start and stop number***")

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

total_sum = sum(range(start, end + 1))

print(f"The sum from {start} to {end} is {total_sum}")
