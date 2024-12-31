import tkinter as tk
from tkinter import Label, Button
from tkinter import ttk
import femod
def admin():
    m=tk.Tk()
    m.title("Admin Panel")
    m.geometry("500x600")
    z=Label(m,text="RKAS Industries Pvt Ltd.",font=("Helvetica", 24))
    z.pack()
    y=Label(m,text="Admin Panel",font=("Helvetica", 24))
    y.pack()
    a=Button(m,text="Train",command=lambda:femod.FaceCap().train(),bg='gold1',fg='black')
    a.place(relw=0.8, relh=0.25, relx=0.104167, rely=0.265185)
    d=Button(m,text="Acess Attendance",bg='darkolivegreen1',fg='black')
    d.place(relw=0.8, relh=0.25, relx=0.104167, rely=0.59)
def take_attendance():
    x=femod.FaceCap()
attd_file="Attendance.csv"
m=tk.Tk()
m.title("Attendance System")
m.geometry("500x600")
a=Label(m,text="RKAS Industries Pvt Ltd.",font=("Helvetica", 24))
a.pack()
b=Label(m,text="Attendance System",font=("Helvetica", 18))
b.pack()
z=Button(m,text="Admin Login",command=lambda:admin())
z.place(relw=0.2,relh=0.05,relx=0.7,rely=0.15)
c=Button(m,text="Take Attendance",height=5,width=50,command=lambda:take_attendance(),bg='gold1',fg='black')
c.place(relw=0.8, relh=0.25, relx=0.104167, rely=0.265185)
d=Button(m,text="Quit",command=lambda:quit(),bg='darkolivegreen1',fg='black')
d.place(relw=0.8, relh=0.25, relx=0.104167, rely=0.59)
m.mainloop()
