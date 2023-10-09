from tkinter import *
from PIL import *
from PIL import ImageTk,Image
from ataouser import taouser
from bdoimatkhau import doipw
from cProfileHomeDir import profileHomeDir
from dxoauser import xoauser
from eDichVuWeb import dichVuWeb
from fDichVuTelnet import dichVuTelnet
from gDocFile import docFile
class giaodien(Tk):
        def __init__(self):
            super().__init__()
            
            self.geometry("500x600+700+100")
            
            bg_frame = Frame(self,width=500,height=800,bg="#fff",bd=10)
            bg_frame.place(x=0,y=0)
            heading_frame = Frame(self,width=500,height=70,bg="#708090",bd=10)
            heading_frame.place(x=0,y=0)
            heading = Label(heading_frame,text="Mạng máy tính",font="arial 20 bold",bg="#708090")
            heading.place(x=150,y=8)
            
            a = Button(self, text="1. Tạo User trên hệ thống Domain Controller", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfoa)
            a.place(x=30,y=90)
            b = Button(self, text="2. Cập nhật mật khẩu của Một User.", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfob)
            b.place(x=30,y=130)
            c = Button(self, text="3. Tạo Profile và Home Dir cho Một User.", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfoc)
            c.place(x=30,y=170)
            d = Button(self, text="4. Xóa Một User trên hệ thống Domain Controller.", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfod)
            d.place(x=30,y=210)
            e = Button(self, text="5. Hàm cài dịch vụ Web cho Server.", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfoe)
            e.place(x=30,y=250)
            f = Button(self, text="6. Hàm cài dịch vụ Web cho Telnet.", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfof)
            f.place(x=30,y=290)
            g = Button(self, text="7. Đọc file CSV", fg="Black",bg="#00E676", font="arial 13 ",width=48,height=1,command=self.showCusInfog)
            g.place(x=30,y=330)
            
        def showCusInfoa(self):
            self.app = taouser(master = self)
            self.withdraw()
        def showCusInfob(self):
            self.app = doipw(master = self)
            self.withdraw()
        def showCusInfoc(self):
            self.app = profileHomeDir(master = self)
            self.withdraw()
        def showCusInfod(self):
            self.app = xoauser(master = self)
            self.withdraw()
        def showCusInfoe(self):
            self.app = dichVuWeb(master = self)
            self.withdraw()
        def showCusInfof(self):
            self.app = dichVuTelnet(master = self)
            self.withdraw()
        def showCusInfog(self):
            self.app = docFile(master = self)
            self.withdraw()
        

if __name__ == "__main__":
    obj = giaodien()
    obj.mainloop()