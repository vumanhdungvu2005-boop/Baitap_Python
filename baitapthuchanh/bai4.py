# Nhập thông tin cá nhân
ten = input("Nhập tên: ")
tuoi = input("Nhập tuổi: ")
email = input("Nhập email: ")
skype = input("Nhập skype: ")
dia_chi = input("Nhập địa chỉ: ")
noi_lam_viec = input("Nhập nơi làm việc: ")

# a) Lưu vào file setInfo.txt
with open("setInfo.txt", "w", encoding="utf-8") as f:
    f.write(f"Tên: {ten}\n")
    f.write(f"Tuổi: {tuoi}\n")
    f.write(f"Email: {email}\n")
    f.write(f"Skype: {skype}\n")
    f.write(f"Địa chỉ: {dia_chi}\n")
    f.write(f"Nơi làm việc: {noi_lam_viec}\n")

print("Đã lưu thông tin vào file setInfo.txt")

# b) Đọc file và hiển thị ra màn hình
print("\nThông tin đọc từ file:")
with open("setInfo.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)