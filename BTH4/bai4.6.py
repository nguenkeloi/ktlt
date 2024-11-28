full_name = input("Nhập tên người: ")
name_parts = full_name.split()

# Giả định rằng họ là phần đầu tiên và tên riêng là phần cuối cùng
last_name = name_parts[0]
first_name = name_parts[-1]

print("Họ:", last_name)
print("Tên riêng:", first_name)
#nguyenkeloi235752021610061
