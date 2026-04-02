# ====== 1. Hàm tính tổng 2 số ======
def tong_2_so(a, b):
    # Hàm nhận vào 2 số a và b
    # Trả về tổng của 2 số
    return a + b


# ====== 2. Hàm tính tổng danh sách ======
def tong_danh_sach(ds):
    # ds là một list (danh sách các số)
    # sum(ds) là hàm có sẵn trong Python để tính tổng
    return sum(ds)


# ====== 3. Hàm kiểm tra số nguyên tố ======
def la_so_nguyen_to(n):
    # Nếu n < 2 thì không phải số nguyên tố
    if n < 2:
        return False

    # Duyệt từ 2 đến căn bậc 2 của n
    # Nếu tồn tại số chia hết thì không phải số nguyên tố
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:   # nếu n chia hết cho i
            return False

    # Nếu không chia hết cho số nào -> là số nguyên tố
    return True


# ====== 4. Tìm số nguyên tố trong đoạn [a, b] ======
def tim_so_nguyen_to(a, b):
    ket_qua = []  # tạo danh sách rỗng để lưu kết quả

    # Duyệt từ a đến b
    for i in range(a, b + 1):
        # Nếu i là số nguyên tố thì thêm vào danh sách
        if la_so_nguyen_to(i):
            ket_qua.append(i)

    return ket_qua


# ====== 5. Hàm kiểm tra số hoàn hảo ======
def la_so_hoan_hao(n):
    # Số <= 0 không phải số hoàn hảo
    if n <= 0:
        return False

    tong = 0  # biến lưu tổng các ước

    # Duyệt các số từ 1 đến n-1 để tìm ước
    for i in range(1, n):
        if n % i == 0:  # nếu i là ước của n
            tong += i   # cộng vào tổng

    # Nếu tổng các ước = n thì là số hoàn hảo
    return tong == n


# ====== 6. Tìm số hoàn hảo trong đoạn [a, b] ======
def tim_so_hoan_hao(a, b):
    ket_qua = []  # danh sách lưu kết quả

    # Duyệt từ a đến b
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            ket_qua.append(i)

    return ket_qua


# ====== 7. MENU ======
def menu():
    while True:  # lặp vô hạn cho đến khi chọn thoát
        print("\n===== MENU =====")
        print("1. Tính tổng 2 số")
        print("2. Tính tổng danh sách")
        print("3. Kiểm tra số nguyên tố")
        print("4. Tìm số nguyên tố trong đoạn")
        print("5. Kiểm tra số hoàn hảo")
        print("6. Tìm số hoàn hảo trong đoạn")
        print("0. Thoát")

        # Nhập lựa chọn từ người dùng
        chon = int(input("Nhập lựa chọn: "))

        # ====== Xử lý từng chức năng ======

        if chon == 1:
            # Nhập 2 số
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))

            # Gọi hàm và in kết quả
            print("Tổng =", tong_2_so(a, b))

        elif chon == 2:
            # Nhập nhiều số, cách nhau bằng dấu cách
            ds = list(map(int, input("Nhập các số: ").split()))

            # Tính tổng
            print("Tổng =", tong_danh_sach(ds))

        elif chon == 3:
            n = int(input("Nhập số: "))

            # Kiểm tra số nguyên tố
            if la_so_nguyen_to(n):
                print("Là số nguyên tố")
            else:
                print("Không phải số nguyên tố")

        elif chon == 4:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))

            # Tìm các số nguyên tố
            print("Các số nguyên tố:", tim_so_nguyen_to(a, b))

        elif chon == 5:
            n = int(input("Nhập số: "))

            # Kiểm tra số hoàn hảo
            if la_so_hoan_hao(n):
                print("Là số hoàn hảo")
            else:
                print("Không phải số hoàn hảo")

        elif chon == 6:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))

            # Tìm số hoàn hảo
            print("Các số hoàn hảo:", tim_so_hoan_hao(a, b))

        elif chon == 0:
            # Thoát chương trình
            print("Thoát chương trình")
            break

        else:
            # Trường hợp nhập sai
            print("Chọn sai, nhập lại!")


# ====== Chạy chương trình ======
menu()