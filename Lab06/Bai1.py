import pandas as pd

df = pd.read_csv("C:\\Users\\LENOVO\\OneDrive\\Máy tính\\Python\\Lab06\\Automobile_data.csv")

#Xuất dl đọc từ tập tin "Automobile_data"
#mặc định sẽ hiện thị 5 dòng đầu và 5 dòng cuối

print(df)

#Xuất 6 dòng đầu tiên
#print(df.head(6))

#xuất 7 dòng cuối cùng
#print(df.tail(7))

#Tên công ty có ô tô đắt nhất
df = df[['company','price']] [df.price == df['price'].max()]
print(df)


#xuât thông tin chi tiết của tất cả các xe toyota
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group("toyota")
print(toyotaDf)

# Đếm số xe từng hãng
counts = df.groupby('company').size()

# In kết quả
print(counts)

#print(df['company'].value_counts())

#Hiển thị giá xe cao nhất của mỗi hãng xe
price = df['company']

# Tìm giá xe cao nhất của mỗi hãng
max_price = price.groupby('company').max()

# In kết quả
print(max_price)