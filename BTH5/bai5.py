print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# bai5.py

import bai5_5

def main():
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử của danh sách
    arr = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr.append(value)
    
    # Sử dụng module bai5_5 để sắp xếp danh sách
    sorted_arr = bai5_5.sort_list(arr)
    print("Danh sách sau khi sắp xếp:", sorted_arr)
    
    # Tìm phần tử lớn nhất trong danh sách
    max_value = bai5_5.find_max(arr)
    print("Phần tử lớn nhất trong danh sách:", max_value)
    
    # Tìm phần tử nhỏ nhất trong danh sách
    min_value = min(arr)
    print("Phần tử nhỏ nhất trong danh sách:", min_value)

if __name__ == "__main__":
    main()
