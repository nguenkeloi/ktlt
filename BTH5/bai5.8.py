def Sequential_Search(dlist, item):
    # Duyệt qua từng phần tử trong danh sách
    for i in range(len(dlist)):
        if dlist[i] == item:
            # Nếu tìm thấy phần tử, trả về True và chỉ mục
            return (True, i)
    
    # Nếu không tìm thấy phần tử, trả về False và -1
    return (False, -1)

# Chương trình nhập danh sách và phần tử cần tìm
if __name__ == "__main__":
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử của danh sách
    dlist = []
    print("Nhập các phần tử:")
    for _ in range(n):
        dlist.append(int(input()))

    # Nhập phần tử cần tìm
    item = int(input("Nhập phần tử cần tìm: "))
    
    # Tìm kiếm phần tử trong danh sách
    result = Sequential_Search(dlist, item)
    
    # In kết quả
    if result[0]:
        print(f"Phần tử {item} được tìm thấy tại chỉ mục {result[1]}")
    else:
        print(f"Phần tử {item} không có trong danh sách.")
