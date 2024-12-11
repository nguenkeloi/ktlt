print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
class Nguoi(object):  # Lớp cơ sở
    def getGender(self):
        return "Unknown"  # Giá trị mặc định

class Nam(Nguoi):  # Lớp con Nam
    def getGender(self):
        return "Nam"  # Ghi đè phương thức getGender

class Nu(Nguoi):  # Lớp con Nu
    def getGender(self):
        return "Nữ"  # Ghi đè phương thức getGender

# Tạo đối tượng từ các lớp
aNam = Nam()
aNu = Nu()

# In kết quả phương thức getGender của các đối tượng
print(aNam.getGender())  # In ra: Nam
print(aNu.getGender())   # In ra: Nữ
