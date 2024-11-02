import pandas as pd

# Đọc file weather.csv
df = pd.read_csv('weather.csv')

# Danh sách các hướng hợp lệ
valid_directions = {
    "N", "NNE", "NE", "ENE", "E", 
    "ESE", "SE", "SSE", "S", "SSW", 
    "SW", "WSW", "W", "WNW", "NW", "NNW"
}

# Kiểm tra tính hợp lệ của cột 'wind_d'
invalid_wind_d = df[~df['wind_d'].isin(valid_directions)]

# In kết quả
if not invalid_wind_d.empty:
    print("Cac gia tri khong hop le:")
    print(invalid_wind_d)
else:
    print("Tat ca cac gia tri deu hop le")
