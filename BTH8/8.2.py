print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import turtle
import random

# Danh sách màu sắc
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

# Tạo đối tượng turtle để vẽ
painter = turtle.Turtle()
painter.pensize(3)

# Vẽ 10 vòng tròn với màu sắc ngẫu nhiên và các biến đổi vị trí
for i in range(10):
    # Chọn màu ngẫu nhiên từ danh sách màu
    color = random.choice(colors)
    painter.pencolor(color)  # Thiết lập màu bút vẽ

    # Vẽ một vòng tròn có bán kính 100
    painter.circle(100)

    # Xoay bút vẽ theo các góc khác nhau
    painter.right(30)  # Quay 30 độ sang phải
    painter.left(60)   # Quay 60 độ sang trái

    # Di chuyển về vị trí (0, 0) để vẽ vòng tròn tiếp theo
    painter.setposition(0, 0)

# Kết thúc chương trình
turtle.done()
