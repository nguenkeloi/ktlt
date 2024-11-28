print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import math

# Nhập tọa độ của điểm thứ nhất
x1 = int(input("Enter x1 ---> "))
y1 = int(input("Enter y1 ---> "))

# Nhập tọa độ của điểm thứ hai
x2 = int(input("Enter x2 ---> "))
y2 = int(input("Enter y2 ---> "))

# Tính khoảng cách giữa hai điểm
dx = (x2 - x1) * (x2 - x1)  # Độ chênh lệch tọa độ x
dy = (y2 - y1) * (y2 - y1)   # Độ chênh lệch tọa độ y
res = math.sqrt(dx + dy)  # Công thức tính khoảng cách

# In kết quả
print("Distance between two points:", res)
