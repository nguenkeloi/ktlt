print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Nhập xâu ký tự từ bàn phím
input_str = input("Nhập một xâu ký tự: ")

# Tách xâu ký tự thành danh sách các từ
b = input_str.split()
print("Danh sách các từ:", b)

# Kết hợp lại các từ thành xâu ký tự với dấu cách
c = " ".join(b)
print("Xâu ký tự đã kết hợp lại:", c)
