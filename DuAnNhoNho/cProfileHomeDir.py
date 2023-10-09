from tkinter import *
from unidecode import *
from openpyxl import *
import os

class profileHomeDir(Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("550x400+700+100")
        self.config(bg="#fff")
        self.title("Đổi mật khẩu")
        
        self.var_ten = StringVar()
        self.var_pw = StringVar()
        self.var_ou = StringVar()
        self.var_dm1 = StringVar()
        self.var_fd = StringVar()
            
        heading_flame = Frame(self,width=500,height=400,bg="#fff",bd=5)
        heading_flame.place(x=0,y=0)
        heading = Label(heading_flame,text="Tạo Profile và Home Dir cho Một User.",font="arial 17 bold",fg="black")
        heading.place(x=50,y=20)
            
        ten = Label(heading_flame,text="Nhập tên user: ",font="arial 11",bg="#fff",fg="black")
        ten.place(x=80,y=80)
        pw = Label(heading_flame,text="Nhập password: ",font="arial 11",bg="#fff",fg="black")
        pw.place(x=80,y=120)
        ou = Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black")
        ou.place(x=80,y=160)
        dm1 = Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black")
        dm1.place(x=80,y=200)
        namefd = Label(heading_flame,text="Nhập tên folder: ",font="arial 11",bg="#fff",fg="black")
        namefd.place(x=80,y=240)
            
        self.result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
        self.result_label.place(x=50, y=320)
            
        acc_field = Entry(self,width=35,bd=3,textvariable=self.var_ten)
        ip_field = Entry(self,width=35,bd=3,textvariable=self.var_pw)
        ou_field = Entry(self,width=35,bd=3,textvariable=self.var_ou)
        dm1_field = Entry(self,width=35,bd=3,textvariable=self.var_dm1)
        namefd_field = Entry(self,width=35,bd=3,textvariable=self.var_fd)   
        
        acc_field.bind("<Return>", profileHomeDir.focus1)
        ip_field.bind("<Return>", profileHomeDir.focus2)
        ou_field.bind("<Return>", profileHomeDir.focus3)
        dm1_field.bind("<Return>", profileHomeDir.focus4)
        namefd_field.bind("<Return>", profileHomeDir.focus5) 
        
        acc_field.place(x=200,y=80)
        ip_field.place(x=200,y=120)
        ou_field.place(x=200,y=160)
        dm1_field.place(x=200,y=200)
        namefd_field.place(x=200,y=240)
    
    
        kq = Button(self, text="Run", command= lambda: self.executed(), fg="Black",bg="#00E676",width=12)
        kq.place(x=130,y=280)
        thoat = Button(self, text="Thoát", fg="Black",bg="#00E676", command=lambda : self.thoat(),width=12)
        thoat.place(x=300,y=280)
    def focus1(event):
        profileHomeDir.ten_field.focus_set()      
    def focus2(event):
        profileHomeDir.pw_field.focus_set()
    def focus3(event):
        profileHomeDir.ou_field.focus_set()      
    def focus4(event):
        profileHomeDir.dm1_field.focus_set()
    def focus5(event):
        profileHomeDir.namefd_field.focus_set()
        
            
    def createProfileAndHomeDir(self,account,nameFolder, ou, domain,ip_server):
        cmdMkdir = f'mkdir C:\\{nameFolder}'
        os.system(cmdMkdir)
        cmdshare = f'net share {nameFolder}= C:\\{nameFolder}'
        print(cmdshare)
        os.system(cmdshare)
        path_profile = f'-profile \\{ip_server}\\profiles\\{account}'
        command2 = f'dsmod user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" {path_profile}'
        print(command2)
        os.system(command2)
    def executed(self):
            account = self.var_ten.get()
            ip = self.var_pw.get()
            ou = self.var_ou.get()
            domain = self.var_dm1.get()
            namefd = self.var_fd.get
            path_profile = f'-profile \\{ip}\\profiles\\{account}'
            command2 = f'dsmod user "CN={account},OU={ou},OU=QTM_CTY,dc={domain},dc=com" {path_profile}'
            if account and namefd and ou and domain and ip:
                self.createProfileAndHomeDir(account,ip,ou,domain,namefd)
                self.result_label.insert(0,command2)
    def thoat(self):
        self.destroy()
        self.master.deiconify()

if __name__ == "__main__":
    root = Tk()
    obj = profileHomeDir(master = root)
    root.mainloop()
    