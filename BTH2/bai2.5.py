print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Nhập vào một số tự nhiên n > 0
n = int(input("Enter a number ---> "))

# Kiểm tra điều kiện n > 0
if n > 0:
    # In ra các số tự nhiên từ n đến 0, mỗi số trên một hàng
    while n >= 0:
        print(n)
        n -= 1
else:
    print("Vui lòng nhập một số tự nhiên lớn hơn 0.")
