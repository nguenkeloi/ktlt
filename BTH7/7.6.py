print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def read_last_n_lines(file_name, n):
    try:
        with open(file_name, 'r') as file:
            # Đọc tất cả các dòng vào danh sách
            lines = file.readlines()
            
            # Nếu file có ít hơn n dòng, chỉ đọc các dòng có trong file
            last_n_lines = lines[-n:] if len(lines) >= n else lines
            
            # Hiển thị các dòng cuối cùng
            print("Các dòng cuối cùng trong tệp là:")
            for line in last_n_lines:
                print(line.strip())  # Loại bỏ ký tự newline

    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Nhập tên file và số dòng cần đọc từ người dùng
file_name = input("Nhập tên file cần đọc: ")
n = int(input("Nhập số dòng cuối cùng cần đọc: "))

# Đọc và hiển thị n dòng cuối cùng của file
read_last_n_lines(file_name, n)
