print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# bai5-6.py

import bai5_6

def main():
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử của danh sách
    arr = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr.append(value)
    
    # Sử dụng module bai5_6 để sắp xếp danh sách
    sorted_arr = bai5_6.sort_list(arr)
    print("Danh sách sau khi sắp xếp:", sorted_arr)
    
    # Tìm phần tử lớn nhất trong danh sách
    max_value = bai5_6.find_max(arr)
    max_index = arr.index(max_value)  # Tìm vị trí phần tử lớn nhất
    print("Phần tử lớn nhất trong danh sách:", max_value)
    print(f"Vị trí phần tử lớn nhất (index) là: {max_index}")
    
    # Tìm phần tử nhỏ nhất trong danh sách
    min_value = bai5_6.find_min(arr)
    min_index = arr.index(min_value)  # Tìm vị trí phần tử nhỏ nhất
    print("Phần tử nhỏ nhất trong danh sách:", min_value)
    print(f"Vị trí phần tử nhỏ nhất (index) là: {min_index}")

if __name__ == "__main__":
    main()
