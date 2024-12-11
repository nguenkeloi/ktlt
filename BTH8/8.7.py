import tkinter
import random
# List các màu có thể
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
# Thời gian chơi ban đầu là 120 giây
timeleft = 120
# Hàm bắt đầu trò chơi
def startGame(event):
    global score
    if timeleft == 120:
        # Bắt đầu đếm ngược thời gian
        countdown()
        # Chạy hàm chọn màu tiếp theo
        nextColour()
# Hàm chọn và hiển thị màu tiếp theo
def nextColour():
    global score
    global timeleft
    # Nếu thời gian còn lại > 0, tiếp tục trò chơi
    if timeleft > 0:
        # Làm cho ô nhập liệu trở nên hoạt động
        e.focus_set()
        
        # Nếu màu đã nhập trùng với màu hiển thị, cộng điểm
        if e.get().lower() == colours[1].lower():
            score += 2  # Cộng 2 điểm cho đúng
        else:
            score -= 1  # Trừ 1 điểm cho sai
        
        # Xóa ô nhập liệu
        e.delete(0, tkinter.END)
        
        # Xáo trộn lại danh sách màu sắc
        random.shuffle(colours)
        
        # Thay đổi màu hiển thị và tên màu
        label.config(fg=str(colours[1]), text=str(colours[0]))
        
        # Cập nhật điểm số
        scoreLabel.config(text="Score: " + str(score))

# Hàm đếm ngược thời gian
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        # Gọi lại hàm countdown sau 1 giây
        timeLabel.after(1000, countdown)
# Tạo cửa sổ GUI
root = tkinter.Tk()
# Thiết lập tiêu đề cửa sổ
root.title("COLORGAME")
# Thiết lập kích thước cửa sổ
root.geometry("375x300")
# Thêm nhãn hướng dẫn
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                         font=('Helvetica', 12))
instructions.pack()
# Thêm nhãn điểm số
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()
# Thêm nhãn thời gian còn lại
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
# Thêm nhãn hiển thị màu
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()
# Thêm ô nhập liệu để nhập màu sắc
e = tkinter.Entry(root)
# Khi nhấn phím Enter, bắt đầu trò chơi
root.bind('<Return>', startGame)
e.pack()
# Đặt focus vào ô nhập liệu
e.focus_set()
# Bắt đầu GUI
root.mainloop()
