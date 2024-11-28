input_string = input("Nhập một chuỗi: ")

# Loại bỏ các chữ số
output_string = ''.join(char for char in input_string if not char.isdigit())

print("Chuỗi mới sau khi loại bỏ chữ số:", output_string)
#nguyenkeloi235752021610061
