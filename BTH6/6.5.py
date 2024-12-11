print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
class ReverseString:
    def __init__(self, input_string):
        self.input_string = input_string
    
    def reverse_words(self):
        # Chia chuỗi thành các từ
        words = self.input_string.split()
        # Đảo ngược thứ tự các từ
        reversed_words = words[::-1]
        # Nối các từ lại thành một chuỗi mới
        return ' '.join(reversed_words)

# Nhập chuỗi từ người dùng
input_str = 'nguyen ke loi'

# Tạo đối tượng của lớp ReverseString
reverse_string = ReverseString(input_str)

# Đảo ngược chuỗi và in kết quả
result = reverse_string.reverse_words()
print(result)
