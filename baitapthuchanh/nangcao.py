import os
import difflib
import re

# Đọc tất cả file .py trong thư mục
def read_all_code(folder_path):
    code = ""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    code += f.read() + "\n"
    return code

# Chuẩn hóa code (bỏ comment + khoảng trắng)
def normalize_code(code):
    # bỏ comment
    code = re.sub(r"#.*", "", code)
    # bỏ khoảng trắng dư
    code = " ".join(code.split())
    return code

# Tính % trùng lặp
def similarity(code1, code2):
    return difflib.SequenceMatcher(None, code1, code2).ratio() * 100

# Phân tích cấu trúc code
def analyze_structure(code):
    return {
        "for": code.count("for "),
        "if": code.count("if "),
        "while": code.count("while "),
        "def": code.count("def ")
    }

# So sánh cấu trúc
def compare_structure(s1, s2):
    score = 0
    total = len(s1)

    for key in s1:
        if s1[key] == s2[key]:
            score += 1

    return (score / total) * 100


# ===== MAIN =====
folder1 = input("Nhập đường dẫn thư mục 1: ")
folder2 = input("Nhập đường dẫn thư mục 2: ")

code1 = read_all_code(folder1)
code2 = read_all_code(folder2)

# Chuẩn hóa
norm1 = normalize_code(code1)
norm2 = normalize_code(code2)

# So sánh nội dung
sim_percent = similarity(norm1, norm2)

# So sánh cấu trúc
struct1 = analyze_structure(code1)
struct2 = analyze_structure(code2)
struct_percent = compare_structure(struct1, struct2)

# Kết quả
print("\n===== KẾT QUẢ =====")
print(f"Độ trùng lặp code: {sim_percent:.2f}%")
print(f"Độ giống về cấu trúc: {struct_percent:.2f}%")

# Đánh giá
if sim_percent > 70:
    print("⚠️ Code rất giống nhau (có thể copy)")
elif sim_percent > 40:
    print("⚠️ Code giống ở mức trung bình")
else:
    print("✅ Code khác nhau")