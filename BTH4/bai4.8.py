input_string = input("Nhập một dãy các từ: ")
words = input_string.split()  # Tách chuỗi thành danh sách các từ

# Tìm độ dài lớn nhất của các từ
max_length = max(len(word) for word in words)

# Tìm các từ có độ dài bằng độ dài lớn nhất
longest_words = [word for word in words if len(word) == max_length]

print("Các từ dài nhất trong dãy vừa nhập:", ', '.join(longest_words))
#nguyenkeloi235752021610061
