# Bài 5: Đếm số lần xuất hiện của các từ trong file

import os

file_name = "demo_file2.txt"

# Nếu file chưa tồn tại thì tự tạo file
if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Dem so luong tu xuat hien abc abc abc 12 12 it it eaut")
    print("Đã tạo file demo_file2.txt")

# Đọc file
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

# Chuẩn hóa về chữ thường (tránh phân biệt hoa/thường)
text = text.lower()

# Tách từ
words = text.split()

# Đếm số lần xuất hiện
count_dict = {}

for word in words:
    if word in count_dict:
        count_dict[word] += 1
    else:
        count_dict[word] = 1

# In kết quả
print("Kết quả:")
print(count_dict)