import tkinter as tk
from tkinter.ttk import Style, Frame
from tkinter import ttk, END

root = tk.Tk()
root.geometry("820x400+240+180")

root.columnconfigure(0, pad=4)

root.title("Quản lý món ăn")

lblTop = tk.Label(text="Nhóm món ăn").grid(row=0, column=1, sticky='W',pady=20)

n = tk.StringVar()
food_cbb = ttk.Combobox(root, width=20, textvariable=n)
food_cbb['values'] = ('Khai vị', 'Hải sản', 'Bia - Nước ngọt')
food_cbb.current(0)

food_cbb.grid(row=0, column=4, sticky='E', pady=20)

class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = tk.Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

t = Table(root)
root.mainloop()
