print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import re

def is_valid_password(password):
    # Kiểm tra các điều kiện của mật khẩu
    if (6 <= len(password) <= 12 and
            re.search(r"[a-z]", password) and
            re.search(r"[0-9]", password) and
            re.search(r"[A-Z]", password) and
            re.search(r"[$#@]", password)):
        return True
    return False

# Nhập chuỗi mật khẩu từ bàn phím, phân tách bởi dấu phẩy
input_passwords = input("Nhập các mật khẩu (phân tách bằng dấu phẩy): ")
password_list = input_passwords.split(',')

# Lọc và in ra mật khẩu hợp lệ
valid_passwords = [pwd.strip() for pwd in password_list if is_valid_password(pwd.strip())]

print("Mật khẩu hợp lệ:", ', '.join(valid_passwords))
