import csv
from tkinter import *

class docFile(Toplevel):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("550x350+700+100")
        self.config(bg="#fff")
        self.title("Đọc file")
        self.resizable(False,False)
            
        heading_flame = Frame(self,width=500,height=400,bg="#fff",bd=5)
        heading_flame.place(x=0,y=0)
        heading = Label(heading_flame,text="Đọc file CSV",font="arial 17 bold",fg="black")
        heading.place(x=80,y=20)
            
        self.result_label = Entry(heading_flame,font="arial 11",bg='#fff',fg="black", text= "",width=55)
        self.result_label.place(x=50, y=150)
        
        kq = Button(self, text="Run", command= lambda: self.executed(), fg="Black",bg="#00E676",width=12)
        kq.place(x=130,y=100)
        thoat = Button(self, text="Thoát", fg="Black",bg="#00E676", command=lambda : self.thoat(),width=12)
        thoat.place(x=300,y=100)

    def read_csv_file(self):
        user_data = []
        file_path = 'D:\HocTap\LapTrinhPyThon\DuAnNhoNho\\DATASERVER.csv'
        try: 
            with open(file_path, newline='', encoding='utf8') as csvfile:
                csvreader = csv.reader(csvfile)
                for row in csvreader:
                    if len(row) >= 3:
                        user = {
                            'user' : row[0],
                            'ou' : row[1],
                            'passwd' : row[2]
                        }
                        user_data.append(user)
                    print(user_data)
                return user_data
        except Exception as e:
            print(e)
            return None
        
    def executed(self):
            dt = self.read_csv_file()
            
            self.result_label.insert(0,dt)   
    def thoat(self):
        self.destroy()
        self.master.deiconify()
if __name__ == "__main__":
    root = Tk()
    obj = docFile(master = root)
    root.mainloop()
     

