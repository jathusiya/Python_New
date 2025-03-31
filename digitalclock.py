from tkinter import*
clk = Tk()
clk.title("clock")
clk.geometry("1350x700+0+0")
clk.config(bg="blue")

ib_hr = Label(clk,text ="12", font=("times 20 bold", 75, 'bold'), bg = 'yellow', fg = "white")
ib_hr.place(x=350, y=200, width=150, height=150)

ib_hr_txt = Label(clk, text= "HOUR", font=("Times 20 bold", 20, "bold"),bg = "#87587", fg="white")
ib_hr_txt.place(x=350, y= 360, width = 150, height= 50)

ib_mn = Label(clk,text ="12", font=("times 20 bold", 75, 'bold'), bg = 'yellow', fg = "white")
ib_mn.place(x=350, y=200, width=150, height=150)

ib_mn_txt = Label(clk, text= "HOUR", font=("Times 20 bold", 20, "bold"),bg = "#87587", fg="white")
ib_mn_txt.place(x=350, y= 360, width = 150, height= 50)

clk.mainloop()