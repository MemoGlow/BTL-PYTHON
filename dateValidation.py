import pandas as pd

# Đọc file weather.csv
df = pd.read_csv('weather.csv')

# Chuyển đổi cột 'date' sang kiểu datetime, các giá trị không hợp lệ sẽ thành NaT
df['date_valid'] = pd.to_datetime(df['date'], errors='coerce')

# Lọc các hàng có giá trị NaT trong cột 'date_valid' (tức là ngày không hợp lệ)
invalid_dates = df[df['date_valid'].isna()]

# Hiển thị các hàng có giá trị ngày không hợp lệ
print("Cac hang chua hop le: ")
print(invalid_dates)
