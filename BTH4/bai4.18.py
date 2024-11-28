# Nhập số nguyên n từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Danh sách để lưu các số Fibonacci
fibonacci_numbers = []

# Các số Fibonacci bắt đầu
a, b = 0, 1

# Tính các số Fibonacci nhỏ hơn n
while a < n:
    fibonacci_numbers.append(a)
    a, b = b, a + b  # Cập nhật các số Fibonacci

# In ra danh sách các số Fibonacci
print("Các số Fibonacci nhỏ hơn", n, "là:", fibonacci_numbers)
#guyenkeloi235752021610061
