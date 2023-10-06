import pyodbc

# Kết nối tới SQL Server sử dụng DNS
connectionString = pyodbc.connect('''DRIVER={SQL Server};SERVER=LinhIuDau;DATABASE=QLSinhVien;UID=sa;PWD=sa''')

# Thực hiện các truy vấn SQL bằng cách tạo đối tượng cursor
cursor = connectionString.cursor()
cursor.execute('select *from SinhVien')
rows = cursor.fetchall()

# In kết quả
for row in rows:
    print(row)

# Đóng kết nối
connectionString.close()

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT * FROM Lop"
        cursor.execute(select_query)
        records = cursor.fetchall()
        print(f"danh sach cac lop la: ")
        for row in records:
            print("*"*50)
            print("Mã Lớp: ",row[0])
            print("Tên Lớp: ",row[1])

        close_connection(connection)

    except (Exception, pyodbc.Error) as error:
                print("Đã có lỗi xảy ra. Thông tin lỗi: ", error)

get_all_class()
