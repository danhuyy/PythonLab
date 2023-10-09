from unidecode import *
from openpyxl import *
from tkinter import *
import os

class dichVuWeb(Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("550x350+700+100")
        self.config(bg="#fff")
        self.title("Tạo User")
        self.resizable(False,False)
            
        heading_flame = Frame(self,width=500,height=400,bg="#fff",bd=5)
        heading_flame.place(x=0,y=0)
        heading = Label(heading_flame,text="Cài dịch vụ Web cho Server.",font="arial 17 bold",fg="black")
        heading.place(x=80,y=20)
            
        self.result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
        self.result_label.place(x=50, y=150)
        
        kq = Button(self, text="Run", command= lambda: self.executed(), fg="Black",bg="#00E676",width=12)
        kq.place(x=130,y=100)
        thoat = Button(self, text="Thoát", fg="Black",bg="#00E676", command=lambda : self.thoat(),width=12)
        thoat.place(x=300,y=100)

    def install_service_web(self):
        command = "powershell.exe Install-windowsFeature - name Web-Server -IncludeManagermenttools"
        try:
            print(command)
            os.system(command)
        except Exception as e:
            print(e)
    def executed(self):
            command = "powershell.exe Install-windowsFeature - name Web-Server -IncludeManagermenttools"
            
            self.install_service_web()
            self.result_label.insert(0,command)   
    def thoat(self):
        self.destroy()
        self.master.deiconify()
if __name__ == "__main__":
    root = Tk()
    obj = dichVuWeb(master = root)
    root.mainloop()
     

