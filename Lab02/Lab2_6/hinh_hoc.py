class HinhHoc:
    def __init__(self, cd) -> None:
        self.canh = cd

    def HinhHoc(self, cd):
        self.canh = cd

    def TinhDienTich(self):
        return self.canh**2
    
    def xuat(self):
        print("canh hinh hoc: ",self.canh)
        
