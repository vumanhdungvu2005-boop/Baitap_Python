# Bài 4: Tổng số chẵn nhỏ hơn n

n = int(input("Nhập số nguyên n: "))

tong = 0

for i in range(n):
    if i % 2 == 0:  # kiểm tra số chẵn
        tong += i

print("Tổng các số chẵn nhỏ hơn", n, "là:", tong)