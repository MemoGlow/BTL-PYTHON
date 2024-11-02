import pandas as pd

# Đọc file weather.csv
df = pd.read_csv('weather.csv')

# Lọc ra các giá trị duy nhất trong cột 'province'
unique_provinces = df['province'].unique()

# Hiển thị các giá trị duy nhất
print(unique_provinces)

# for i in unique_provinces:
#     print(i)
