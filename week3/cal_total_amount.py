lone = float(input("ป้อนจำนวนเงินกู้(บาท): "))

if lone <= 1000:
    interest = 0.10
elif lone <= 10000:
    interest = 0.05
else:
    interest = 0.02

total = lone * (1 + interest)

print("จำนวนเงินที่ต้องคืนรวมดอกเบี้ย: {:.2f} บาท".format(total))