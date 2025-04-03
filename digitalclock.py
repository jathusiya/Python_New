from tkinter import*
import time
clk = Tk()
clk.title("clock")
clk.geometry("1350x700+0+0")
clk.config(bg="blue")

def clock():
    hr = str(time.strftime("%H"))
    mn = str(time.strftime("%M"))
    sc = str(time.strftime("%S"))
    print(hr,mn,sc)
    if int(hr)> 12 and int(mn)> 0: #to convert AM to PM
        ib.dn.congig(text ="PM")
    if int(hr)>12:
        hr = str(int(int(hr)-12))    
    ib_hr.config(text = hr)
    ib_mn.config(text = mn)
    ib_sc.config(text = sc)

    ib_hr.after(200,clock) #clock update every day


ib_hr = Label(clk,text ="12", font=("times 20 bold", 75, 'bold'), bg = '#0875B7', fg = "white")
ib_hr.place(x=350, y=200, width=150, height=150)

ib_hr_txt = Label(clk, text= "HOUR", font=("Times 20 bold", 20, "bold"),bg = "#0875B7", fg="white")
ib_hr_txt.place(x=350, y= 360, width = 150, height= 50)

ib_mn = Label(clk,text ="12", font=("times 20 bold", 75, 'bold'), bg = '#008EA4', fg = "white")
ib_mn.place(x=520, y=200, width=150, height=150)

ib_mn_txt = Label(clk, text= "MINUTE", font=("Times 20 bold", 20, "bold"),bg = "#008EA4", fg="white")
ib_mn_txt.place(x=520, y= 360, width = 150, height= 50)

ib_sc = Label(clk,text ="12", font=("times 20 bold", 75, 'bold'), bg = '#06B4B8', fg = "white")
ib_sc.place(x=690, y=200, width=150, height=150)

ib_sc_txt = Label(clk, text= "SECOUND", font=("Times 20 bold", 20, "bold"),bg = "#06B4B8", fg="white")
ib_sc_txt.place(x=690, y= 360, width = 150, height= 50)

ib_dn = Label(clk,text ="AM", font=("times 20 bold", 75, 'bold'), bg = '#9F0646', fg = "white")
ib_dn.place(x=860, y=200, width=150, height=150)

ib_dn_txt = Label(clk, text= "NOON", font=("Times 20 bold", 20, "bold"),bg = "#9F0646", fg="white")
ib_dn_txt.place(x=860, y= 360, width = 150, height= 50)

clock()
clk.mainloop()