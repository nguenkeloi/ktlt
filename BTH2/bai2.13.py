print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import math

def solve_quadratic(a, b, c):
    # Tính delta
    delta = b**2 - 4*a*c
    
    if delta > 0:
        # Hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return (x1, x2)
    elif delta == 0:
        # Nghiệm kép
        x = -b / (2*a)
        return (x,)
    else:
        # Không có nghiệm thực
        return None

# Nhập các hệ số từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Kiểm tra nếu a = 0
if a == 0:
    print("Hệ số a không thể bằng 0 cho phương trình bậc 2.")
else:
    # Giải phương trình
    solutions = solve_quadratic(a, b, c)
    
    if solutions is None:
        print("Phương trình không có nghiệm thực.")
    elif len(solutions) == 1:
        print(f"Phương trình có nghiệm kép: x = {solutions[0]}")
    else:
        print(f"Phương trình có hai nghiệm phân biệt: x1 = {solutions[0]}, x2 = {solutions[1]}")
