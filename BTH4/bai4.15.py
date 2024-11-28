# Nhập chuỗi từ bàn phím
input_string = input("Nhập các từ tiếng Anh (cách nhau bằng dấu cách): ")

# Tách chuỗi thành danh sách các từ
words = input_string.split()

# Sắp xếp danh sách theo thứ tự từ điển
words.sort()

# In ra các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:")
for word in words:
    print(word)
#nguyenkeloi235752021610061
