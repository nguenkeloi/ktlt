# main.py
from bai5_9 import bai5_9

def main():
    # Nhập số lượng phần tử
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử và tạo danh sách
    lst = []
    print("Nhập các phần tử trong danh sách (các số phải được cách nhau bằng dấu cách):")
    lst = list(map(int, input().split()))

    # Đảm bảo danh sách được sắp xếp (vì thuật toán tìm kiếm nhị phân yêu cầu mảng đã sắp xếp)
    lst.sort()

    # Nhập giá trị cần tìm kiếm
    value = int(input("Nhập giá trị cần tìm: "))

    # Gọi hàm binary_search
    result = binary_search(lst, value)

    # In kết quả
    if result:
        print(f"Giá trị {value} có trong danh sách.")
    else:
        print(f"Giá trị {value} không có trong danh sách.")

if __name__ == "__main__":
    main()
