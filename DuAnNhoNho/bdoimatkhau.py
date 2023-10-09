from tkinter import *
from openpyxl import *
import os

class doipw(Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("550x350+700+100")
        self.config(bg="#fff")
        self.title("Đổi mật khẩu")
        self.resizable(False,False)
        
        self.var_acc=StringVar()
        self.var_pw=StringVar()
        self.var_ou=StringVar()
        self.var_dm1=StringVar()
            
        heading_flame = Frame(self,width=500,height=300,bg="#fff",bd=5)
        heading_flame.place(x=0,y=0)
        heading = Label(heading_flame,text=" Cập nhật mật khẩu của Một User.",font="arial 17 bold",fg="black")
        heading.place(x=50,y=20)

        acc = Label(heading_flame,text="Nhập user: ",font="arial 11",bg="#fff",fg="black")
        acc.place(x=80,y=80)
        pw = Label(heading_flame,text="Nhập password: ",font="arial 11",bg="#fff",fg="black")
        pw.place(x=80,y=120)
        ou = Label(heading_flame,text="Nhập ou: ",font="arial 11",bg="#fff",fg="black")
        ou.place(x=80,y=160)
        dm1 = Label(heading_flame,text="Nhập doman: ",font="arial 11",bg="#fff",fg="black")
        dm1.place(x=80,y=200)
        
        self.result_label = Entry(self,font="arial 11",bg='#fff',fg="black",width=55)
        self.result_label.place(x=50, y=280)
        
        
        
        acc_field = Entry(self,width=35,bd=3,textvariable=self.var_acc)
        pw_field = Entry(self,width=35,bd=3,textvariable=self.var_pw)
        ou_field = Entry(self,width=35,bd=3,textvariable=self.var_ou)
        dm1_field = Entry(self,width=35,bd=3,textvariable=self.var_dm1)
        
        acc_field.bind("<Return>", doipw.focus2)
        pw_field.bind("<Return>", doipw.focus3)
        ou_field.bind("<Return>", doipw.focus4)
        dm1_field.bind("<Return>", doipw.focus1)
        
        acc_field.place(x=230,y=80)
        pw_field.place(x=230,y=120)
        ou_field.place(x=230,y=160)
        dm1_field.place(x=230,y=200)

        kq = Button(self, text="Run", fg="Black",bg="#00E676", command=lambda : self.executed(),width=12)
        kq.place(x=130,y=240)
        thoat = Button(self, text="Thoát", fg="Black",bg="#00E676", command=lambda : self.thoat(),width=12)
        thoat.place(x=300,y=240)
        
        
    def focus1(event):
        doipw.acc_field.focus_set()   
    def focus2(event):
        doipw.pw_field.focus_set()
    def focus3(event):
        doipw.ou_field.focus_set()  
    def focus4(event):
        doipw.dm1_field.focus_set()   

    def changePasswd(self,account, passwd, ou, domain):
        command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,dc={domain},dc=com" -pwd "{passwd}"'
        print(command)
        os.system(command)
    def executed(self):
            account = self.var_acc.get()
            passwd = self.var_acc.get()
            ou = self.var_acc.get()
            domain = self.var_acc.get()
            command = f'dsmod user "CN={account},ou={ou},OU=QTM_CTY,dc={domain},dc=.com" -pwd "{passwd}"'
            if account and passwd and ou and domain:
                self.changePasswd(account, passwd, ou, domain)
                self.result_label.insert(0,command)
    def thoat(self):
        self.destroy()
        self.master.deiconify()
if __name__ == "__main__":
    root = Tk()
    obj = doipw(master = root)
    root.mainloop()
    