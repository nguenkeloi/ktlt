print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
class RomanToInteger:
    def __init__(self):
        # Tạo từ điển để ánh xạ các ký tự La Mã sang giá trị số nguyên
        self.roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def roman_to_integer(self, roman: str) -> int:
        total = 0
        prev_value = 0
        
        # Duyệt từng ký tự trong chuỗi La Mã từ phải sang trái
        for char in reversed(roman):
            current_value = self.roman_dict.get(char, 0)
            
            # Nếu giá trị của ký tự hiện tại nhỏ hơn giá trị của ký tự trước đó,
            # chúng ta trừ đi giá trị của ký tự hiện tại
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value

            # Cập nhật giá trị của ký tự trước đó
            prev_value = current_value
        
        return total

# Ví dụ sử dụng lớp
converter = RomanToInteger()
roman_number = "IX"  # Số La Mã cần chuyển đổi
integer_value = converter.roman_to_integer(roman_number)

print(f"Số La Mã {roman_number} chuyển thành số nguyên là: {integer_value}")
