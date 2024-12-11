print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def copy_file_content(source_file, destination_file):
    try:
        # Mở file nguồn để đọc
        with open(source_file, 'r') as src:
            content = src.read()  # Đọc toàn bộ nội dung của file nguồn

        # Mở file đích để ghi
        with open(destination_file, 'w') as dest:
            dest.write(content)  # Ghi nội dung vào file đích
        
        print(f"Nội dung từ '{source_file}' đã được sao chép vào '{destination_file}' thành công!")
    except FileNotFoundError:
        print(f"File '{source_file}' không tồn tại!")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Nhập tên file nguồn và file đích từ người dùng
source_file = input("Nhập tên file nguồn (ví dụ: 'source.txt'): ")
destination_file = input("Nhập tên file đích (ví dụ: 'destination.txt'): ")

# Sao chép nội dung từ file nguồn sang file đích
copy_file_content(source_file, destination_file)
