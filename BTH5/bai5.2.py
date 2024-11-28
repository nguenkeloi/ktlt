print(" Nguyễn Kế Lợi")
print("MSSV: 235752021610061")
# Import thư viện datetime với alias là dt
import datetime as dt

# Định nghĩa định dạng ngày giờ
format = '%Y-%m-%dT%H:%M:%S'

# Chuyển chuỗi '2008-10-12T14:45:52' thành đối tượng datetime
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In thông tin về ngày, tháng, phút và giây từ đối tượng t1
print('Day ' + str(t1.day))        # Trích xuất ngày
print('Month ' + str(t1.month))    # Trích xuất tháng
print('Minute ' + str(t1.minute))  # Trích xuất phút
print('Second ' + str(t1.second)) # Trích xuất giây

# Định nghĩa ngày và giờ hiện tại
t2 = dt.datetime.now()

# Tính sự khác biệt giữa ngày giờ hiện tại và t1
diff = t2 - t1

# In ra sự khác biệt về số ngày
print('How many days difference? ' + str(diff.days))
