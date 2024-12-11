print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            # Đọc toàn bộ nội dung của file
            content = file.read()
            print(content)  # In ra nội dung của file
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")

# Lấy tên file từ người dùng và thực hiện chương trình
file_name = input("Nhập tên file cần đọc: ")
read_file(file_name)
