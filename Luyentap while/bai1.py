# Bài 1: Tính tích từ 1 đến 10

tich = 1  # khởi tạo biến tích

for i in range(1, 11):  # chạy từ 1 đến 10
    tich *= i  # nhân dồn

print("Tích của 10 số tự nhiên đầu tiên là:", tich)