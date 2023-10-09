import tkinter as tk
root=tk.Tk()
 
# Chỉnh kích thước của khung
root.geometry("600x400")
  
# khai báo biến chuỗi
# để lưu tên và mật khẩu
name_var=tk.StringVar()
passw_var=tk.StringVar()
 
# định nghĩa một hàm sẽ
# lấy tên và mật khẩu và
# in chúng ra màn hình
def submit():
 
    name=name_var.get()
    password=passw_var.get()
     
    print("The name is : " + name)
    print("The password is : " + password)
     
    name_var.set("")
    # passw_var.set("")
     
# tạo nhãn cho
# tên sử dụng Nhãn tiện ích
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
  
# tạo mục nhập cho đầu vào
# tên sử dụng mục nhập widget
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
  
# tạo nhãn cho mật khẩu
passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
  
# tạo mục nhập cho mật khẩu
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
  
# tạo nút bằng tiện ích
# Nút sẽ gọi hàm submit
sub_btn=tk.Button(root,text = 'Submit', command = submit)
  
# đặt nhãn và mục nhập vào
# vị trí được yêu cầu sử dụng lưới
# phương pháp
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
passw_label.grid(row=1,column=0)
passw_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
  
# thực hiện vòng lặp vô hạn
# để cửa sổ hiển thị
root.mainloop()