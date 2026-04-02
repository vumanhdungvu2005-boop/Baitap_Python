# Bài 3

# Tạo file demo_file1.txt
with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO")

# a) In trên 1 dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("a) In trên 1 dòng:")
    print(f.read().replace("\n", " "))

# b) In từng dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("\nb) In từng dòng:")
    for line in f:
        print(line.strip())