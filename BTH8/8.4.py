print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
from tkinter import *

# Khởi tạo cửa sổ đồ họa
window = Tk()
window.title("Welcome to LikeGeeks app")  # Tiêu đề cửa sổ
window.geometry('350x200')  # Kích thước cửa sổ

# Thêm một label (nhãn) vào cửa sổ
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)  # Đặt vị trí của label trên cửa sổ

# Phương thức xử lý sự kiện khi bấm nút
def clicked():
    lbl.configure(text="Button was clicked !!")  # Thay đổi nội dung của label khi bấm nút

# Tạo một button (nút bấm) và gán phương thức `clicked` vào sự kiện bấm nút
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)  # Đặt vị trí của button trên cửa sổ

# Phương thức xử lý sự kiện khi nhấn phím
def key_pressed(event):
    lbl.configure(text=f"You pressed {event.char} key!")  # Hiển thị phím vừa nhấn

# Liên kết sự kiện phím với phương thức xử lý
window.bind('<KeyPress>', key_pressed)

# Bắt đầu vòng lặp chính để hiển thị cửa sổ
window.mainloop()
