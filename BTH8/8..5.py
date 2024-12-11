import tkinter as tk

# Tạo cửa sổ chính
root = tk.Tk()
print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Danh sách các ngôn ngữ lập trình
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

# Hàm hiển thị lựa chọn khi người dùng chọn hoặc bỏ chọn indicator
def ShowChoice():
    selected_languages = []
    for i, var in enumerate(language_vars):
        if var.get():
            selected_languages.append(languages[i][0])
    print("Selected languages:", selected_languages)

# Thêm nhãn hướng dẫn
tk.Label(root, 
         text="Choose your favourite programming language(s):", 
         justify=tk.LEFT, padx=20).pack()

# Danh sách các biến để theo dõi trạng thái các checkbox
language_vars = []

# Tạo các checkbox (indicator) cho mỗi ngôn ngữ lập trình
for language, index in languages:
    var = tk.IntVar()  # Biến lưu trạng thái checkbox
    language_vars.append(var)
    cb = tk.Checkbutton(root, 
                        text=language, 
                        padx=20, 
                        variable=var, 
                        command=ShowChoice)
    cb.pack(anchor=tk.W)

# Vòng lặp chính của Tkinter
root.mainloop()
