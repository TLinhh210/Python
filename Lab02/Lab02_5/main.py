from datetime import datetime
from sinh_vien import SinhVien

from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSv

sv1 = SinhVienChinhQuy(1957691,"Nguyễn văn C",datetime.strptime("05/12/1999","%d/%m/%Y"),90)
sv2 = SinhVienChinhQuy(1957690,"Nguyễn văn A",datetime.strptime("05/12/1999","%d/%m/%Y"),80)
sv3 = SinhVienPhiCQ(1957692,"Thái Thị Thu",datetime.strptime("15/08/1998","%d/%m/%Y"),"cao đẳng",2)
sv4 = SinhVienPhiCQ(2000324,"Trần Thanh Tâm",datetime.strptime("27/08/2000","%d/%m/%Y"),"cao đẳng",2)
sv5 = SinhVienPhiCQ(2004544,"Nguyễn Thanh Trà",datetime.strptime("17/05/1999","%d/%m/%Y"),"trung cấp",2.5)
sv6 = SinhVienChinhQuy(2004567,"Nguyễn Thành Nam",datetime.strptime("07/12/1999","%d/%m/%Y"),60)
sv7 = SinhVienPhiCQ(2004545,"Nguyễn Thanh Thanh",datetime.strptime("29/10/1999","%d/%m/%Y"),"trung cấp",2.5)
sv8 = SinhVienChinhQuy(2004679,"Võ Hoài Nam",datetime.strptime("04/01/2000","%d/%m/%Y"),70)

dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.xuat()

vt = dssv.timSVTheoMs(2000324)
print(f"Sinh viên ở vị trí thứ {vt + 1} trong danh sách")

kq = dssv.timSvTheoLoai("chinhquy")
print("Danh sách sinh viên theo loại: ")
for sv in kq:
    print(sv)
    
kq1 = dssv.timSV_coDiemRL_Tren80(80)
print ("Danh sách sinh viên điểm rèn luyện trên 80: ")
for sv in kq1:
    print (sv)

kq2= dssv.timSV_coTrinhDoCaoDang_truoc_ngay("cao đẳng",datetime.strptime("15/08/1999","%d/%m/%Y"))
print ("=================")
for sv in kq2:
    print(sv)
