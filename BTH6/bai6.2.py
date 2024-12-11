print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
class Hinhchunhat:
    # Constructor để khởi tạo chiều dài và chiều rộng
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    # Phương thức tính diện tích
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

# Tạo đối tượng Hinhchunhat với chiều dài 5 và chiều rộng 2
hcn = Hinhchunhat(5,2)

# Tính diện tích
dien_tich = hcn.tinh_dien_tich()

# In kết quả
print("Diện tích hình chữ nhật là:", dien_tich)

