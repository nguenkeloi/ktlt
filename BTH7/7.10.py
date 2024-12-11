print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def find_longest_words(text):
    # Tách văn bản thành các từ
    words = text.split()
    
    # Tìm độ dài của từ dài nhất
    max_length = max(len(word) for word in words)
    
    # Tìm tất cả các từ có độ dài bằng với từ dài nhất
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()  # Đọc toàn bộ nội dung của file
        return text
    except FileNotFoundError:
        print(f"File '{file_name}' không tồn tại!")
        return None

# Nhập tên file từ người dùng
file_name = input("Nhập tên file cần tìm từ dài nhất: ")

# Đọc nội dung từ file
text = read_file(file_name)

if text:
    # Tìm và in ra các từ dài nhất
    longest_words = find_longest_words(text)
    print(f"Các từ dài nhất trong văn bản là: {', '.join(longest_words)}")
