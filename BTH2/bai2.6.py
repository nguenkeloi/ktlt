print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Tìm các số trong đoạn 2000 đến 3200
result = []

for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        result.append(str(number))

# In kết quả
print(', '.join(result))
