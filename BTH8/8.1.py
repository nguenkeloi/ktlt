print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import turtle

# Tạo cửa sổ vẽ
window = turtle.Screen()
window.bgcolor("lightgreen")  # Thiết lập màu nền cho cửa sổ vẽ

# Tạo đối tượng turtle để vẽ
painter = turtle.Turtle()
painter.fillcolor('blue')  # Thiết lập màu sắc tô trong
painter.pencolor('blue')  # Thiết lập màu sắc của bút vẽ
painter.pensize(3)  # Thiết lập độ dày của bút vẽ

# Định nghĩa hàm vẽ hình vuông
def drawsq(t, s):
    for i in range(4):
        t.forward(s)  # Di chuyển bút vẽ về phía trước s đơn vị
        t.left(90)  # Quay bút 90 độ sang trái (tạo góc vuông)

# Vẽ hình vuông với cạnh dài 200 đơn vị
for i in range(1, 180):
    painter.left(18)  # Quay bút 18 độ sau mỗi vòng lặp
    drawsq(painter, 200)  # Vẽ hình vuông có cạnh dài 200 đơn vị

# Kết thúc chương trình vẽ
turtle.done()
