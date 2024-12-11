print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius  # Bán kính của hình tròn

    def area(self):
        # Tính diện tích hình tròn
        return math.pi * self.radius ** 2

    def circumference(self):
        # Tính chu vi hình tròn
        return 2 * math.pi * self.radius

# Ví dụ sử dụng
circle = Circle(5)  # Khởi tạo một đối tượng Circle với bán kính 5

print("Diện tích hình tròn:", circle.area())  # In diện tích
print("Chu vi hình tròn:", circle.circumference())  # In chu vi
