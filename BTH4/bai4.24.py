print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def count_upper_lower(input_string):
    upper_count = 0
    lower_count = 0

    # Duyệt qua từng ký tự trong chuỗi đầu vào
    for char in input_string:
        if char.isupper():  # Kiểm tra nếu ký tự là chữ hoa
            upper_count += 1
        elif char.islower():  # Kiểm tra nếu ký tự là chữ thường
            lower_count += 1
    
    # In kết quả
    print(f"Chữ hoa: {upper_count}")
    print(f"Chữ thường: {lower_count}")

# Nhập câu đầu vào từ người dùng
input_string = input("Nhập một câu: ")

# Gọi hàm đếm chữ hoa và chữ thường
count_upper_lower(input_string)
