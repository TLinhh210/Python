from hinh_chu_nhat import HinhChuNhat

class HinhVuong(HinhChuNhat):
    def __init__(self, canh) -> None:
        super().__init__(canh)
    def xuat(self):
        print(f"DT hình vuông là: {self.TinhDienTich}")
        