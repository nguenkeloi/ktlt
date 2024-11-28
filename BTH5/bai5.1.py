print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# mymath.py

# Hàm tính bình phương
def square(n):
    return n * n

# Hàm tính lập phương
def cube(n):
    return n * n * n

# Hàm tính giá trị trung bình của một danh sách số
def average(values):
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum) / nvals

