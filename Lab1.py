'''
#BÀI TẬP 1
#Bai 1
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")

#bai 2
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

#Bai 3
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

#Bai 4
from math import pi
r = float(input('Nhập bán kính: '))
print('Diện tích hình tròn có bán kính', r ,'là: ' + str(pi * r**2))

#Bai 5
a = input('Nhập họ: ')
b = input('Nhập tên: ')
print (b + ' ' + a)

# Bài 6
a = input("Nhập dãy số : ")
list = a.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#Bài 7
filename = input("Nhập tên tệp: ")
a = filename.split(".")
print ("phần mở rộng là : " + repr(a[-1]))

#Bài 8
color_list = ["Red","Green","White" ,"Black"]
print('Màu đầu tiên là: ',color_list[0], '\nMàu cuối cũng là: ',color_list[-1])

#Bài 9
exam_st_date = (11,12,2014)
print( "Kỳ thi bắt đầu từ : %i / %i / %i"%exam_st_date)

#Bài 10
a = int(input('Nhập n: '))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print(f'Giá trị mẫu của {a} có kết quả mong đợi là: ', n1 + n2 + n3)

#Bài 11
a = abs(-10)
print('Giá trị tuyệt đối là: ', a)

#Bài 12
import calendar
y = int(input("Nhập năm : "))
m = int(input("Nhập tháng : "))
print(calendar.month(y, m))

#Bài 13
print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")

#Bài 14
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print('Sản lượng dự kiến: ', delta.days, 'ngày')

#Bài 15
pi = 3.1415926535897931
r= 6.0
V= 4.0/3.0*pi* r**3
print('Thể tích hình cầu: ',V)

#Bài 16
def difference(n):
    if n <= 17:
        return 17 - n
    else:
        return (n - 17) * 2 

print(difference(22))
print(difference(14))

#Bài 17
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))

#bài 18
def sum_thrice(x, y, z):

     sum = x + y + z
  
     if x == y == z:
      sum = sum * 3
     return sum

print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))

#Bài 19
def new_string(text):
  if len(text) >= 2 and text [:2] == "Is":
    return text
  return "Is" + text
print(new_string("Array"))
print(new_string("IsEmpty")) 

#Bài 20
def larger_string(text, n):
   result = ""
   for i in range(n):
      result = result + text
   return result
print(larger_string('abc', 2))
print(larger_string('.py', 3)) 

#Bài 21
num = int(input("Nhập số: "))
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

#Bài 22
def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4:
      count = count + 1

  return count

print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))

#Bài 23
def substring_copy(text, n):
  flen = 2
  if flen > len(text):
    flen = len(text)
  substr = text[:flen]
  result = ""
  for i in range(n):
    result = result + substr
  return result
print(substring_copy('abcdef', 2))
print(substring_copy('p', 3))

#Bài 24
def is_vowel(char):
    all_vowels = 'aeiou'
    return char in all_vowels
print(is_vowel('c'))
print(is_vowel('e'))

#Bài 25
def is_group_member(group_data, n):
   for value in group_data:
       if n == value:
           return True
   return False
print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))


#BÀI TẬP 2
#1
a=int(input("Nhập a: ")) 
b=int(input("Nhập b: ")) 
def Tinh_a_cong_b(a,b): 
    return a+b 
def Tinh_a_chia_b(a,b): 
    return a/b
def Tinh_a_mu_b(a,b): 
    return pow(a,b) 
kq1=Tinh_a_cong_b(a,b) 
kq2=Tinh_a_chia_b(a,b) 
kq3=Tinh_a_mu_b(a,b) 
print (" a + b = ",kq1) 
print(" a/b = ",kq2) 
print(" a^b = ",kq3)

#2 
cd = float(input("Nhập chiều dài: "))
cr = float(input("Nhập chiều rộng: "))

dt = cd * cr
print('Diện tích hình chữ nhật là: ',dt)

#3
import math
def KTSoNguyenTo(n):
    if n == 1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False
    return True

def LietKeSoNT(a, b):
   for i in range(a, b + 1):
       if KTSoNguyenTo(i):
           print(i, end=' ')

a = int(input('Nhập số đầu: '))
b = int(input('Nhập số cuối '))

if a < 0 or b < 0:
    print('Vui lòng nhập số tự nhiên')
elif a > b:
    print('Số đầu lớn hơn số cuối')
else:
    LietKeSoNT(a, b)


#4
def KiemTraFibonacci(a):
      if a == ((a-1)+(a-2)):
             return True
      else:
             return False
      
a = int(input('Nhập số nguyên: '))
if KiemTraFibonacci(a) == True:
       print(a, 'là số Fibonacci')
else :
       print(a,'Không phải số Fibonacci')

#Bai8
import math
  
# Nhập số a và kiểm tra điều kiện khác 0
a = int(input("Nhập vào số a: "))
b = int(input("Nhập vào số b: "))
 
while True:
    if a == 0 and b == 0:
        print("Một trong hai số a và b phải khác 0: ")
        a = int(input("Nhập lại số a: "))
 
        b = int(input("Nhập lại số b: "))
    else:
        break
 
c = int(input("Nhập vào số c: "))
 
delta = b**2 - 4 * a * c
 
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x2 = ", (-(b) - math.sqrt(delta))/(2*a) )

#Bai9
def tinhgiaithua(n):
    kq = 1
    if (n == 0 or n == 1):
        return kq
    else:
        for i in range(2, n + 1):
            kq *= i
        return kq
 
n = int(input("Nhập số nguyên dương n = "))
print("Giai thừa của", n, "là", tinhgiaithua(n))

#Bai10
n = int(input("Nhập kích thước tam giác: "))

for i in range(n):
    for j in range(n):
        if(j==0 or j==i or i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#Bai 11
sogiay =int(input("Nhập vào số giây: "))

gio = sogiay // 3600
phut = (sogiay % 3600) // 60
giay = sogiay % 60
print(f"{gio}:{phut}:{giay}")
'''
#Bai 12
arr=[]
arr1=[]
n=int(input("Nhập kích thước mảng: "))
for i in range(n):
    a=int(input(f"Nhập phần tử thứ {i+1}:"))
    arr.append(a)

def ds_khong_chia_het_cho_5(arr):
    for num in arr:
        if num % 2 != 0 and num % 5 != 0:
            arr1.append(num)
    print("số lẻ không chia hết cho 5 là ",arr1)

ds_khong_chia_het_cho_5(arr)
