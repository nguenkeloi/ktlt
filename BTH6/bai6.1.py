print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import math  # Import thư viện math để sử dụng giá trị π

class Circle:
    # Constructor để khởi tạo bán kính khi tạo đối tượng
    def __init__(self, radius):
        self.radius = radius  # Khởi tạo thuộc tính radius của đối tượng
        
    # Phương thức tính diện tích hình tròn
    def area(self):
        return math.pi * (self.radius ** 2)  # Công thức diện tích A = π * r^2

# Tạo một đối tượng Circle với bán kính 7
circle1 = Circle(7)

# Tính diện tích của circle1
print(f"Diện tích của hình tròn có bán kính {circle1.radius} là: {circle1.area():.2f}")
