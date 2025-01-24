import array as arr

# สร้าง array สำหรับเก็บค่าตัวเลข
data = arr.array('i', [50, 87, 65, 39])

# Print All data in array
print("All data in array:", list(data))

# Max and Min
print("Max =", max(data))
print("Min =", min(data))

# Sum and Average
total = sum(data)
average = total / len(data)
print("Sum =", total)
print("Average =", average)

# Sort min to max and print
sorted_data_asc = sorted(data)
print("Sorted (min to max):", sorted_data_asc)

# Sort max to min and print
sorted_data_desc = sorted(data, reverse=True)
print("Sorted (max to min):", sorted_data_desc)

# Show odd number
odd_numbers = [x for x in data if x % 2 != 0]
print("Odd numbers:", odd_numbers)

# Show even number
even_numbers = [x for x in data if x % 2 == 0]
print("Even numbers:", even_numbers)

# Search for a number
search_number = 87
if search_number in data:
    print(f"{search_number} found in array.")
else:
    print(f"{search_number} not found in array.")

search_number = 100
if search_number in data:
    print(f"{search_number} found in array.")
else:
    print(f"{search_number} not found in array.")

# Delete for a number
delete_number = 65
if delete_number in data:
    data.remove(delete_number)
    print(f"After deleting {delete_number}: {list(data)}")
else:
    print(f"{delete_number} not found in array.")
