from openpyxl import *
from tkinter import *
import os

class xoauser(Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("550x350+700+100")
        self.config(bg="#fff")
        self.title("Xóa user")
        self.register(False,False)
        
        self.var_ten = StringVar()
        self.var_ou = StringVar()
        self.var_dm1 = StringVar()
        
        heading_flame = Frame(self,width=550,height=400,bg="#fff",bd=5)
        heading_flame.place(x=0,y=0)
        heading = Label(heading_flame,text="Xóa Một User trên hệ thống Domain Controller.",font="arial 16 bold",fg="black")
        heading.place(x=50,y=20)
        
        ten = Label(heading_flame,text="Nhập tên user: ",font="arial 11",bg="#fff",fg="black")
        ten.place(x=80,y=80)
        ou = Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black")
        ou.place(x=80,y=120)
        dm1 = Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black")
        dm1.place(x=80,y=160)
        
        self.result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
        self.result_label.place(x=50, y=240)
        
        ten_field = Entry(self,width=35,bd=3,textvariable=self.var_ten)
        ou_field = Entry(self,width=35,bd=3,textvariable=self.var_ou)
        dm1_field = Entry(self,width=35,bd=3,textvariable=self.var_dm1)
            
        ten_field.bind("<Return>", xoauser.focus2)
        ou_field.bind("<Return>", xoauser.focus3)
        dm1_field.bind("<Return>", xoauser.focus1)
            
        ten_field.place(x=230,y=80)
        ou_field.place(x=230,y=120)
        dm1_field.place(x=230,y=160)
        
        kq = Button(self, text="Run", command= lambda: self.executed(), fg="Black",bg="#00E676",width=12)
        kq.place(x=130,y=200)
        thoat = Button(self, text="Thoát", fg="Black",bg="#00E676", command=lambda : self.thoat(),width=12)
        thoat.place(x=300,y=200)
        
    def focus1(event):
        xoauser.ten_field.focus_set()
    def focus2(event):
        xoauser.ou_field.focus_set()
    def focus3(event):
        xoauser.dm1_field.focus_set()   
        
    def delUser(self,account, ou, domain):
        command = f'dsrm user "CN={account},OU={ou},OU=QTM_CTY,{domain}"'
        print(command)
        os.system(command)
    def executed(self):
            user = self.var_ten.get()
            ou = self.var_ou.get()
            domain = self.var_dm1.get()
            command = f'dsrm user "CN={user},OU={ou},OU=QTM_CTY,{domain}"'
            if user and ou and domain:
                self.delUser(user, ou, domain)
                self.result_label.insert(0,command)
    def thoat(self):
        self.destroy()
        self.master.deiconify()
if __name__ == "__main__":
    root =  Tk()
    obj = xoauser(master = root)    
    root.mainloop()
     