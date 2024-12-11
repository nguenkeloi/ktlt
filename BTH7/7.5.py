print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def append_text_to_file(file_name, text_to_append):
    try:
        # Mở file ở chế độ 'a' để nối văn bản vào cuối file
        with open(file_name, 'a') as file:
            file.write(text_to_append + '\n')  # Nối văn bản vào file và thêm dấu xuống dòng

        print("Văn bản đã được nối vào file thành công!")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def read_and_display_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()  # Đọc toàn bộ nội dung của file
        print("\nNội dung của tệp hiện tại:")
        print(content)
    
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file: {e}")

# Nhập tên file và văn bản muốn nối vào file
file_name = input("Nhập tên file cần nối văn bản vào: ")
text_to_append = input("Nhập văn bản bạn muốn nối vào tệp: ")

# Nối văn bản vào tệp
append_text_to_file(file_name, text_to_append)

# Hiển thị nội dung của tệp sau khi nối
read_and_display_file(file_name)
