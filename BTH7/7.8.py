print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def write_list_to_file(file_name, data_list):
    try:
        with open(file_name, 'w') as file:
            # Ghi từng phần tử của danh sách vào file
            for item in data_list:
                file.write(str(item) + '\n')  # Ghi mỗi phần tử và xuống dòng
        print(f"Dữ liệu đã được ghi vào file '{file_name}' thành công!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Danh sách dữ liệu muốn ghi vào file
data_list = ['Hello, World!', 'Python programming is fun.', 'Writing to a file is easy!']

# Nhập tên file từ người dùng
file_name = input("Nhập tên file để ghi danh sách vào (ví dụ: 'output.txt'): ")

# Ghi danh sách vào file
write_list_to_file(file_name, data_list)
