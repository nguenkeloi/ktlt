input_list = input("Nhập danh sách các từ (cách nhau bằng dấu cách): ").split()

# Tìm tất cả các chỉ số của một phần tử
element_to_find = input("Nhập phần tử cần tìm: ")
indices = [i for i, x in enumerate(input_list) if x == element_to_find]

if indices:
    print(f"Phần tử '{element_to_find}' nằm ở các chỉ số: {indices}")
else:
    print(f"Phần tử '{element_to_find}' không có trong danh sách.")
#nguyenkeloi235752021610061
