print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def read_first_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            # Đọc n dòng đầu tiên
            for i in range(n):
                line = file.readline()
                if line:  # Nếu còn dòng nào, in ra
                    print(line.strip())  # Dùng strip để loại bỏ ký tự newline
                else:
                    print(f"File chỉ có {i} dòng.")
                    break
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Nhập tên file và số dòng từ người dùng
file_name = input("Nhập tên file cần đọc: ")
n = int(input("Nhập số dòng đầu tiên cần đọc: "))

# Đọc và in n dòng đầu tiên của file
read_first_n_lines(file_name, n)
