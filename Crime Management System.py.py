#This is a crime management software based on python backed up with MySQL
import mysql.connector as ms
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import left

# creating the sql connection and table
my_con = ms.connect(host='localhost', user='root', password='mDJcvpmo2726!', database='crimerecords')
my_cursor = my_con.cursor()


class Firstpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        back_grd = Label(self, bg='black')
        back_grd.place(x=0, y=0, width=800, height=500)

        title = Label(self, text='LOGIN HERE', fg='ivory', bg='black', bd=5, font=('Arial bold', 45))
        title.place(x=35, y=20, width=725, height=120)

        border = tk.LabelFrame(self, bg='black', bd=5, font=('Arial,20'))
        border.pack(fill='both', expand='yes', padx=150, pady=150)

        L1 = tk.Label(border, text='Username', font=('Arial Bold', 15), bg='black', fg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=2)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text='Password', font=('Arial Bold', 15), bg='black', fg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            try:

                with open('Credential.txt', 'r') as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(',')
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(Thirdpage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo('Error', 'Please provide correct credentials')
            except:
                messagebox.showinfo('Error', 'Please provide correct username and password')

        B1 = tk.Button(border, text='Sign In', font=('Arial', 15), bg='white', command=verify)
        B1.place(x=295, y=120)

        def register():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg='deep sky blue')
            window.title('Register')
            l1 = tk.Label(window, text='Username:', font=('Arial', 15), bg='deep sky blue')
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text='Password:', font=('Arial', 15), bg='deep sky blue')
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show='*', bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text='Confirm Password:', font=('Arial', 15), bg='deep sky blue')
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show='*', bd=5)
            t3.place(x=200, y=110)

            def check():
                if t1.get() != '' or t2.get != '' or t3.get() != '':
                    if t2.get() == t3.get():
                        with open('Credential.txt', 'a') as f:
                            f.write(t1.get() + ',' + t2.get() + '\n')
                            messagebox.showinfo('Welcome', 'You are registered succesfully')
                    else:
                        messagebox.showinfo('Error', 'Password did not match')
                else:
                    messagebox.showinfo('Error', 'Please enter all the details!')

            b1 = tk.Button(window, text='Register', font=('Arial', 15), bg='#ffc22a', command=check)
            b1.place(x=170, y=150)

            window.geometry('477x220')
            window.mainloop()

        B2 = tk.Button(border, text='Sign Up', bg='white', font=('Arial', 15), command=register)
        B2.place(x=190, y=120)

        
        


class Secondpage(tk.Frame):
    def __init__(root, parent2, controller):
        tk.Frame.__init__(root, parent2)

        Label = tk.Label(root, bg='black', font=('Arial Bold', 30))
        Label.pack(fill='both', expand='yes')  # Label for the whole page

        # Heading to the page
        L3 = tk.Label(Label, text='Criminal Info', font=('League Gothic Bold', 25), fg='white', bg='black')
        L3.place(x=275, y=20)

        # textbox to enter name of new criminal
        name = tk.Label(Label, text='Name', font=('Arial Bold', 15), fg='white', bg='black')
        name.place(x=60, y=85)
        name_textbox = tk.Entry(Label, width=30, bd=4)
        name_textbox.place(x=150, y=90)

        # Textbox to enter DOB of criminal
        DOB = tk.Label(Label, text='Date of Birth', font=('Arial Bold', 15), fg='white', bg='black')
        DOB.place(x=60, y=135)
        DOB_textbox = tk.Entry(Label, width=30, bd=4)
        DOB_textbox.place(x=200, y=140)

        # Textbox to enter Gender of criminal
        Gender = tk.Label(Label, text='Gender', font=('Arial Bold', 15), fg='white', bg='black')
        Gender.place(x=60, y=185)
        Gender_textbox = tk.Entry(Label, width=30, bd=4)
        Gender_textbox.place(x=150, y=190)

        # Textbox to enter Blood Group of criminal
        Bgrp = tk.Label(Label, text='Blood Group', font=('Arial Bold', 15), fg='white', bg='black')
        Bgrp.place(x=375, y=185)
        Bgrp_textbox = tk.Entry(Label, width=30, bd=4)
        Bgrp_textbox.place(x=525, y=190)

        # Textbox to enter crime of criminal
        Crime = tk.Label(Label, text='Crime', font=('Arial Bold', 15), fg='white', bg='black')
        Crime.place(x=60, y=235)
        Crime_textbox = tk.Entry(Label, width=50, bd=4)
        Crime_textbox.place(x=150, y=240)

        # Textbox to enter date of the crime
        Dateofcrime = tk.Label(Label, text='Date of crime', font=('Arial Bold', 15), fg='white', bg='black')
        Dateofcrime.place(x=60, y=285)
        Dateofcrime_textbox = tk.Entry(Label, width=50, bd=4)
        Dateofcrime_textbox.place(x=200, y=290)

        def sno():
            my_cursor.execute("SELECT * from records2 ORDER BY Sno desc")
            data = my_cursor.fetchall()
            print(data)
            # for j in data:
            #     return j[0]
            #     break

        def save():
            a=301
            while a<1000:
                nm= "'" +str(name_textbox.get())+"'"
                Db="'" +str(DOB_textbox.get())+"'"
                gen="'" +str(Gender_textbox.get())+"'"
                bld="'" +str(Bgrp_textbox.get())+"'"
                crm="'" +str(Crime_textbox.get())+"'"
                dc= "'" +str(Dateofcrime_textbox.get())+"'"
                snos="'"+str(a)+"'"
                idn="'"+str('C' + str(a))+"'"
                q=(snos+','+idn+','+nm+','+Db+','+gen+','+bld+','+crm+','+dc)
                
                if my_con.is_connected():
                    query = 'insert into records2 values(' +q+ ')'
                    mycursor = my_con.cursor()
                    mycursor.execute(query)
                    my_con.commit()
                    a=a+1
                

        Button = tk.Button(root, text='Submit', font=('Arial Bold', 15), fg='black', bd=5,command=save)
        Button.place(x=450, y=350, width=80, height=40)

        Button = tk.Button(root, text='Back', font=('Arial Bold', 15), bd=5,command=lambda: controller.show_frame(Thirdpage))
        Button.place(x=100, y=350, width=80, height=40)


class Thirdpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Label = tk.Label(self, bg='black')
        Label.pack(fill='both', expand='yes')

        Label2 = tk.Label(self, text='CRIME DEPARTMENT', font=('Arial Bold', 20), fg='ivory', bg='black')
        Label2.place(x=250, y=10, width=300, height=30)

        frame = tk.LabelFrame(self, bg='black', bd=5)
        frame.place(x=12, y=40, width=775, height=400)

        name = tk.Label(frame, text='NAME', font=('Arial Bold', 15), bg='black', fg='ivory')
        name.place(x=40, y=25)
        name_textbox = tk.Entry(frame, width=50, bd=4)
        name_textbox.place(x=130, y=25)




        frame2 = tk.Frame(frame, bg='black')
        frame2.place(x=12, y=70, width=725, height=300)

        tv = ttk.Treeview(frame2, columns=(1, 2, 3, 4, 5, 6, 7, 8,9), show='headings', height='250')
        tv.pack(side=LEFT)
        tv.place(x=0,y=0)

        yscrollbar=ttk.Scrollbar(frame2,orient='vertical',command=tv.yview)
        yscrollbar.pack(side=RIGHT,fill='y')
        tv.configure(yscrollcommand=yscrollbar.set)


        tv.heading(1, text='Sno')
        tv.column(1, anchor=CENTER, stretch=NO, width=81)
        tv.heading(2, text='Id')
        tv.column(2, anchor=CENTER, stretch=NO, width=81)
        tv.heading(3, text='Name')
        tv.column(3, anchor=CENTER, stretch=NO, width=81)
        tv.heading(4, text='DOB')
        tv.column(4, anchor=CENTER, stretch=NO, width=81)
        tv.heading(5, text='Gender')
        tv.column(5, anchor=CENTER, stretch=NO, width=81)
        tv.heading(6, text='Bgrp')
        tv.column(6, anchor=CENTER, stretch=NO, width=81)
        tv.heading(7, text='Crime')
        tv.column(7, anchor=CENTER, stretch=NO, width=81)
        tv.heading(8, text='Date')
        tv.column(8, anchor=CENTER, stretch=NO, width=81)
        tv.heading(9, text='Status')
        tv.column(9, anchor=CENTER, stretch=NO, width=81)

        def find():
            sql = "select * from records2 WHERE name=" + "'" + str(name_textbox.get()) + "'"
            my_cursor.execute(sql)

            rows = my_cursor.fetchall()

            for i in rows:
                tv.insert('', 'end', values=i)

        search = tk.Button(self, text='SEARCH', font=('Arial Bold', 15), fg='ivory', bg='black', bd=5,command=find)
        search.place(x=500, y=67, width=200, height=35)

        def record():
            controller.show_frame(Secondpage)

        B3 = tk.Button(self, text='ENTER CRIMINAL DETAILS', font=('Arial Bold', 15), fg='ivory', bg='black', bd=5,command=record)
        B3.place(x=12, y=450, width=775, height=40)
    



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Creating a window

        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}  # Empty dictionary

        for i in (Firstpage, Secondpage, Thirdpage):
            frame = i(window, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(Firstpage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


app = Application()
app.maxsize(1920, 1080)
app.mainloop()
