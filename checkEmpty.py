import pandas as pd

# Đọc file weather.csv
df = pd.read_csv('weather.csv')

# Kiểm tra các cột có giá trị trống
missing_values = df.isnull().sum()

# In ra các cột có giá trị trống
empty_columns = missing_values[missing_values > 0]

if not empty_columns.empty:
    print("Cac o hang chua o trong")
    print(empty_columns)
else:
    print("Tat ca cac hang deu hop le")
