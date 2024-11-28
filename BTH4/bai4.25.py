print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def filter_odd_numbers(input_string):
    # Chuyển chuỗi đầu vào thành danh sách các số nguyên
    numbers = [int(num) for num in input_string.split(',')]
    
    # Lọc các số lẻ từ danh sách
    odd_numbers = [num for num in numbers if num % 2 != 0]
    
    # In kết quả dưới dạng chuỗi phân tách bằng dấu phẩy
    return ",".join(map(str, odd_numbers))

# Nhập chuỗi các số từ người dùng
input_string = input("Nhập danh sách các số (phân tách bởi dấu phẩy): ")

# Lọc các số lẻ và in kết quả
result = filter_odd_numbers(input_string)
print(result)
