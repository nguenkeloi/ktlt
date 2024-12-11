print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
class ATM:
    def __init__(self, balance=0):
        self.balance = balance  # Số dư tài khoản
    def check_balance(self):
        # Kiểm tra số dư tài khoản
        print(f"Số dư hiện tại: {self.balance} VND")
    def deposit(self, amount):
        # Gửi tiền vào tài khoản
        if amount > 0:
            self.balance += amount
            print(f"Đã gửi {amount} VND vào tài khoản.")
        else:
            print("Số tiền gửi phải lớn hơn 0!")
    def withdraw(self, amount):
        # Rút tiền từ tài khoản
        if amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút {amount} VND từ tài khoản.")
        else:
            print("Số dư không đủ để rút!")
def main():
    atm = ATM(100000)  # Khởi tạo tài khoản với số dư ban đầu là 100,000 VND
    while True:
        print("\n--- Chào mừng đến với ATM ---")
        print("1. Kiểm tra số dư")
        print("2. Gửi tiền")
        print("3. Rút tiền")
        print("4. Thoát") 
        try:
            choice = int(input("Chọn một thao tác (1-4): "))
            if choice == 1:
                atm.check_balance()
            elif choice == 2:
                amount = float(input("Nhập số tiền muốn gửi: "))
                atm.deposit(amount)
            elif choice == 3:
                amount = float(input("Nhập số tiền muốn rút: "))
                atm.withdraw(amount)
            elif choice == 4:
                print("Cảm ơn bạn đã sử dụng dịch vụ ATM. Hẹn gặp lại!")
                break
            else:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
        except ValueError:
            print("Vui lòng nhập số hợp lệ.")
if __name__ == "__main__":
    main()
