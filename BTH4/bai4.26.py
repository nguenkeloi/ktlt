print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
def calculate_balance():
    balance = 0  # Khởi tạo số dư tài khoản
    
    while True:
        # Nhập một giao dịch từ người dùng
        transaction = input("Nhập giao dịch (hoặc 'q' để kết thúc): ")
        
        # Nếu người dùng nhập 'q', kết thúc vòng lặp
        if transaction.lower() == 'q':
            break
        
        # Tách giao dịch thành mã loại giao dịch và số tiền
        transaction_parts = transaction.split()
        action = transaction_parts[0]
        amount = int(transaction_parts[1])
        
        # Xử lý giao dịch gửi tiền (D) và rút tiền (W)
        if action == 'D':
            balance += amount  # Tiền gửi vào tài khoản
        elif action == 'W':
            balance -= amount  # Tiền rút ra khỏi tài khoản
    
    # In kết quả cuối cùng là số dư tài khoản
    print(balance)

# Gọi hàm để thực hiện tính toán số dư
calculate_balance()
