from hinh_hoc import HinhHoc

class HinhTron(HinhHoc):
    def __init__(self, r) -> None:
        super().__init__(r)
        self.r = r

    def TinhDienTich(self):
        return 3.14*self.r**2

    def xuat(self):
        print(f"Hinh tròn có diện tích là: {self.TinhDienTich}")