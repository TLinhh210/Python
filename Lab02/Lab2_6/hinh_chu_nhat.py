from hinh_hoc import HinhHoc

class HinhChuNhat(HinhHoc):
    def __init__(self, cd, cr) -> None:
        super().__init__(cd)
        self.dai = cd
        self.rong = cr

    def TinhDienTich(self):
        return self.dai*self.rong
    
    def xuat(self):
        print(f"Diện tích HCN là: {self.TinhDienTich}")