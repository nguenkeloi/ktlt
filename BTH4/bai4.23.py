print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def count_letters_and_digits(input_string):
    letter_count = 0
    digit_count = 0

    # Duyệt qua từng ký tự trong chuỗi đầu vào
    for char in input_string:
        if char.isalpha():  # Kiểm tra nếu ký tự là chữ cái
            letter_count += 1
        elif char.isdigit():  # Kiểm tra nếu ký tự là chữ số
            digit_count += 1
    
    # In kết quả
    print(f"Số chữ cái là: {letter_count}")
    print(f"Số chữ số là: {digit_count}")

# Nhập câu đầu vào từ người dùng
input_string = input("Nhập một câu: ")

# Gọi hàm đếm chữ cái và chữ số
count_letters_and_digits(input_string)
