# Bài 3: Kiểm tra số nguyên tố

n = int(input("Nhập số nguyên dương n: "))

if n < 2:
    print("Không phải số nguyên tố")
else:
    la_nguyen_to = True

    for i in range(2, int(n**0.5) + 1):  # kiểm tra đến căn bậc 2
        if n % i == 0:
            la_nguyen_to = False
            break

    if la_nguyen_to:
        print("Đây là số nguyên tố")
    else:
        print("Không phải số nguyên tố")