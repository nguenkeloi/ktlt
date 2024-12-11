print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()

# Khởi tạo biến để lưu trữ lựa chọn
v = tk.IntVar()
v.set(1)  # Khởi tạo giá trị mặc định, ví dụ Python

# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị lựa chọn khi người dùng chọn một radio button
def ShowChoice():
    print(v.get())

# Thêm nhãn hướng dẫn
tk.Label(root, 
         text="Choose your favourite programming language:", 
         justify=tk.LEFT, padx=20).pack()

# Tạo các radio buttons cho mỗi ngôn ngữ lập trình
for val, language in languages:
    tk.Radiobutton(root, 
                   text=language[0], 
                   padx=20, 
                   variable=v, 
                   command=ShowChoice, 
                   value=language[1]).pack(anchor=tk.W)

# Vòng lặp chính của Tkinter
root.mainloop()
