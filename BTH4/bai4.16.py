# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi các số nhị phân (cách nhau bằng dấu phẩy): ")

# Tách chuỗi thành danh sách các số nhị phân
binary_numbers = input_string.split(',')

# In ra các số nhị phân
print("Các số nhị phân đã nhập:")
for binary in binary_numbers:
    print(binary.strip())  # Sử dụng strip() để loại bỏ khoảng trắng nếu có
#nguyenkeloi235752021610061
