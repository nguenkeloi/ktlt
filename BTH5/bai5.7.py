import pip as np

# Định nghĩa kiểu dữ liệu của mảng
data_type = [('name', 'S15'), ('class', int), ('height', float)]

# Dữ liệu chi tiết của sinh viên
students_details = [('loi', 5, 48.5), ('manh', 6, 52.5), ('anh', 5, 42.10), ('Pit', 5, 40.11)]

# Tạo một mảng có cấu trúc với dtype là data_type
students_details = np.array(students_details, dtype=data_type)

# In ra mảng gốc
print("Original array:")
print(students)

# Sắp xếp mảng theo chiều cao (thứ tự tăng dần)
print("\nSorted by height:")
sorted_students = np.sort(students, order='height')
print(sorted_students)
