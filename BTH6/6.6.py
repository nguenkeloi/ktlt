print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
class StringManipulator:
    def __init__(self):
        self.input_string = ""
    
    def get_String(self):
        # Nhận chuỗi từ người dùng
        self.input_string = input("Nhập một chuỗi: ")
    
    def print_String(self):
        # In chuỗi bằng chữ in hoa
        print(self.input_string.upper())

# Tạo đối tượng của lớp StringManipulator
string_manipulator = StringManipulator()

# Gọi phương thức để nhận chuỗi và in ra chữ in hoa
string_manipulator.get_String()  # Nhập chuỗi từ người dùng
string_manipulator.print_String()  # In chuỗi in hoa
