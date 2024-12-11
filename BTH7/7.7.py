print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def count_lines_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Đếm số dòng trong file
            lines = file.readlines()  # Đọc tất cả các dòng vào danh sách
            num_lines = len(lines)  # Đếm số dòng
            print(f"Số dòng trong file '{file_name}': {num_lines}")
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Nhập tên file từ người dùng và thực hiện chương trình
file_name = input("Nhập tên file cần đếm dòng: ")
count_lines_in_file(file_name)
