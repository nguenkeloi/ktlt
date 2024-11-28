print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import math

def pascal_triangle(n):
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(math.comb(i, j))  # Tính tổ hợp C(i, j)
        print(" ".join(map(str, row)))

# Nhập số dòng cần in
n = int(input("Nhập số dòng của Tam giác Pascal: "))
pascal_triangle(n)
