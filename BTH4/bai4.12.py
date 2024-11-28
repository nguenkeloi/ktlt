input_list = input("Nhập danh sách các từ (cách nhau bằng dấu cách): ").split()

# Bỏ phần tử theo giá trị
element_to_remove = input("Nhập phần tử cần xóa: ")
if element_to_remove in input_list:
    input_list.remove(element_to_remove)
    print("Danh sách sau khi xóa phần tử:", input_list)
else:
    print("Phần tử không có trong danh sách.")
#nguyenkeloi235752021610061
