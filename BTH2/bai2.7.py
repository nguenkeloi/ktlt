print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def create_square_dictionary(n):
    square_dict = {i: i * i for i in range(1, n + 1)}
    return square_dict

# Nhập giá trị n
n = int(input("Nhập số nguyên n: "))
result = create_square_dictionary(n)
print(result)
