print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def check_divisible_by_5(binary_numbers):
    # Danh sách để lưu các số nhị phân chia hết cho 5
    divisible_by_5 = []
    
    # Duyệt qua từng số nhị phân trong danh sách
    for binary in binary_numbers:
        # Chuyển từ nhị phân sang thập phân
        decimal = int(binary, 2)
        
        # Kiểm tra nếu số thập phân chia hết cho 5
        if decimal % 5 == 0:
            divisible_by_5.append(binary)
    
    # In các số chia hết cho 5, phân tách bằng dấu phẩy
    return ",".join(divisible_by_5)

# Nhập chuỗi các số nhị phân phân tách bằng dấu phẩy
input_string = input("Nhập chuỗi các số nhị phân (4 chữ số), phân tách bằng dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# Gọi hàm và in kết quả
result = check_divisible_by_5(binary_numbers)
print(result)
