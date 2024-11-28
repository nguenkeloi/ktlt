print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def is_all_even_digits(number):
    # Kiểm tra xem tất cả các chữ số trong number có phải là số chẵn không
    for digit in str(number):
        if int(digit) % 2 != 0:  # Nếu chữ số không phải chẵn
            return False
    return True

def find_even_digit_numbers(start, end):
    # Lưu các số có tất cả chữ số chẵn
    even_digit_numbers = []
    for num in range(start, end + 1):
        if is_all_even_digits(num):
            even_digit_numbers.append(str(num))  # Chuyển số thành chuỗi để in ra dễ dàng
    return ",".join(even_digit_numbers)

# Định nghĩa phạm vi tìm kiếm
start = 1000
end = 3000

# Tìm các số thỏa mãn điều kiện và in kết quả
result = find_even_digit_numbers(start, end)
print(result)
