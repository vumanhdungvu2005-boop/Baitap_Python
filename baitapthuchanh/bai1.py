# Nhập số dòng cần đọc
n = int(input("Nhập số dòng cần đọc: "))

# Mở file để đọc (r = read)
with open("input.txt", "r", encoding="utf-8") as f:
    for i in range(n):
        line = f.readline()   # đọc từng dòng
        if not line:          # nếu hết file thì dừng
            break
        print(line.strip())   # strip() bỏ xuống dòng