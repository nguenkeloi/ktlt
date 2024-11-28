print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Import thư viện NumPy
import numpy as np

# Tạo mảng với các giá trị từ 12 đến 37 (38 không bao gồm)
x = np.arange(12, 38)

# In mảng ban đầu
print("Mảng được tạo:")
print(x)

# Đảo ngược mảng
reversed_x = x[::-1]

# In mảng đã đảo ngược
print("Mảng đảo ngược:")
print(reversed_x)
