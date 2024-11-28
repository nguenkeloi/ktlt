print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Khởi tạo các giá trị ban đầu của dãy Fibonacci
a, b = 0, 1
sum_even = 0

# Lặp qua các số trong dãy Fibonacci
while b < 4000000:
    if b % 2 == 0:
        sum_even += b
    a, b = b, a + b  # Cập nhật a và b

# In kết quả
print("Tổng các số chẵn trong dãy Fibonacci nhỏ hơn 4 triệu là:", sum_even)
