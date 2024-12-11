print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def read_and_reverse(file_name):
    try:
        with open(file_name, 'r') as file:
            # Đọc toàn bộ nội dung và đảo ngược chuỗi
            content = file.read()
            print(content[::-1])  # In ra nội dung đảo ngược
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")

# Lấy tên file từ người dùng và thực hiện chương trình
file_name = input("Nhập tên file cần đọc: ")
read_and_reverse(file_name)
