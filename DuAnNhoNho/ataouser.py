from unidecode import *
from openpyxl import *
from tkinter import *
import os

class taouser(Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("550x350+700+100")
        self.config(bg="#fff")
        self.title("Tạo User")
        self.resizable(False,False)
        
        self.var_ten = StringVar()
        self.var_pw = StringVar()
        self.var_ou = StringVar()
        self.var_dm1 = StringVar()
            
        heading_flame = Frame(self,width=500,height=400,bg="#fff",bd=5)
        heading_flame.place(x=0,y=0)
        heading = Label(heading_flame,text=" Tạo User trên hệ thống Domain Controller",font="arial 17 bold",fg="black")
        heading.place(x=50,y=20)
            
        ten = Label(heading_flame,text="Nhập tên user: ",font="arial 11",bg="#fff",fg="black")
        ten.place(x=80,y=80)
        pw = Label(heading_flame,text="Nhập password: ",font="arial 11",bg="#fff",fg="black")
        pw.place(x=80,y=120)
        ou = Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black")
        ou.place(x=80,y=160)
        dm1 = Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black")
        dm1.place(x=80,y=200)
            
        self.result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
        self.result_label.place(x=50, y=280)
            
        ten_field = Entry(self,width=35,bd=3,textvariable=self.var_ten)
        pw_field = Entry(self,width=35,bd=3,textvariable=self.var_pw)
        ou_field = Entry(self,width=35,bd=3,textvariable=self.var_ou)
        dm1_field = Entry(self,width=35,bd=3,textvariable=self.var_dm1)
            
        ten_field.bind("<Return>", taouser.focus2)
        pw_field.bind("<Return>", taouser.focus3)
        ou_field.bind("<Return>", taouser.focus4)
        dm1_field.bind("<Return>", taouser.focus1)
            
        ten_field.place(x=230,y=80)
        pw_field.place(x=230,y=120)
        ou_field.place(x=230,y=160)
        dm1_field.place(x=230,y=200)
        kq = Button(self, text="Run", command= lambda: self.executed(), fg="Black",bg="#00E676",width=12)
        kq.place(x=130,y=240)
        thoat = Button(self, text="Thoát", fg="Black",bg="#00E676", command=lambda : self.thoat(),width=12)
        thoat.place(x=300,y=240)
    def focus1(event):
        taouser.ten_field.focus_set()      
    def focus2(event):
        taouser.pw_field.focus_set()
    def focus3(event):
        taouser.ou_field.focus_set()      
    def focus4(event):
        taouser.dm1_field.focus_set()
    def split_name(self,name):
        name_parts = name.lower().split()
        return unidecode(name_parts[-1])+''.join(part[0].upper() for part in name_parts[:-1])

    def createUsers(self,name,passwd,ou, domain):
        account = self.split_name(name)
        command = f'dsadd user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" -pwd "{passwd}"'
        print(command)
        os.system(command)
    def executed(self):
            user = self.var_ten.get()
            passwd = self.var_pw.get()
            ou = self.var_ou.get()
            domain = self.var_dm1.get()
            command = f'dsadd user "CN={self.split_name(user)},OU={ou},OU=QTM_CTY,dc={domain},dc=com" -pwd "{passwd}"'
            if user and passwd and ou and domain:
                self.createUsers(user, passwd, ou, domain)
                self.result_label.insert(0,command)   
    def thoat(self):
        self.destroy()
        self.master.deiconify()
if __name__ == "__main__":
    root = Tk()
    obj = taouser(master = root)
    root.mainloop()
     

