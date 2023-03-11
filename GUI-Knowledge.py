from tkinter import*
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk () # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมเช็คสถานะการบ้าน') # นี่คือชื่อโปรแกรม
GUI.geometry('800x800') #นี่คือขนาดโปรแกรม

#B1=ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)

L1=Label(GUI,text='โปรแกรมเช็กลิสต์การบ้าน',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

#################
def Button1():
    text = 'เสร็จแล้ว ดีมาก ชมตัวเองในความตั้งใจ'
    messagebox.showinfo('สถานะการบ้าน',text)

FB1=Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B1=ttk.Button(FB1,text='ทำการบ้านEP1หรือยัง',command=Button1)
B1.pack(ipadx=20,ipady=20)
#################

def Button2():
    text = 'เสร็จแล้ว ดีมาก ชมตัวเองในความตั้งใจ'
    messagebox.showinfo('สถานะการบ้าน',text)

FB2=Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=200)
B2=ttk.Button(FB1,text='ทำการบ้านEP2หรือยัง',command=Button2)
B2.pack(ipadx=20,ipady=20)

def Button3():
    text = 'เสร็จแล้ว ดีมาก ชมตัวเองในความตั้งใจ'
    messagebox.showinfo('สถานะการบ้าน',text)

FB3=Frame(GUI) #คล้ายกระดาน
FB3.place(x=100,y=300)
B3=ttk.Button(FB1,text='ทำการบ้านEP3หรือยัง',command=Button3)
B3.pack(ipadx=20,ipady=20)

def Button4():
    text = 'ยังเรียนไม่ถึง'
    messagebox.showinfo('สถานะการบ้าน',text)

FB4=Frame(GUI) #คล้ายกระดาน
FB4.place(x=100,y=400)
B4=ttk.Button(FB1,text='ทำการบ้านEP4หรือยัง',command=Button4)
B4.pack(ipadx=20,ipady=20)

def Button5():
    text = 'ยังเรียนไม่ถึง'
    messagebox.showinfo('สถานะการบ้าน',text)

FB5=Frame(GUI) #คล้ายกระดาน
FB5.place(x=100,y=500)
B5=ttk.Button(FB1,text='ทำการบ้านEP5หรือยัง',command=Button5)
B5.pack(ipadx=20,ipady=20)

def Button6():
    text = 'ยังเรียนไม่ถึง'
    messagebox.showinfo('สถานะการบ้าน',text)

FB6=Frame(GUI) #คล้ายกระดาน
FB6.place(x=100, y=600)
B6=ttk.Button(FB1,text='ทำการบ้านEP6หรือยัง',command=Button6)
B6.pack(ipadx=20,ipady=20)

def Button7():
    text = 'ลุงยังไม่สอน'
    messagebox.showinfo('สถานะการบ้าน',text)

FB7=Frame(GUI) #คล้ายกระดาน
FB7.place(x=100, y=700)
B7=ttk.Button(FB1,text='ทำการบ้านEP7หรือยัง',command=Button7)
B7.pack(ipadx=20,ipady=20)

def Button8():
    text = 'ลุงยังไม่สอน'
    messagebox.showinfo('สถานะการบ้าน',text)

FB8=Frame(GUI) #คล้ายกระดาน
FB8.place(x=100, y=800)
B8=ttk.Button(FB1,text='ทำการบ้านEP8หรือยัง',command=Button8)
B8.pack(ipadx=20,ipady=20)



GUI.mainloop()
