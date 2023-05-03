from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import pdb


mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.iconbitmap('py.ico')
        self.root.title("Face Recognition System")

#=================variables==========================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image ................
        img = Image.open("img/stu.jpg")
        img = img.resize((650, 180), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=650, height=120)


#second image ................
        img1 = Image.open("img/stu.jpg")
        img1 = img1.resize((650, 180), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=650, y=0, width=650, height=120)

#bg image ................
        img3 = Image.open("img/bg.jpg")
        img3 = img3.resize((1366,768), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=120, width=1366, height=586)

# title.................................
        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 30 , "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1366, height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1346,height=494)

 #left lable frame................
        left_frame=LabelFrame(main_frame,bd=2,bg='white', relief= RIDGE,text="STUDENT ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=570,height=470)


        img_left = Image.open("img/pre1.jpg")
        img_left = img_left.resize((560, 170), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=560, height=170)

        left_inside_frame=Frame(left_frame,relief=RIDGE,bd=4,bg='white')
        left_inside_frame.place(x=0,y=180,width=565,height=200)

#Attendance id ..............................
        attendaceID_lable=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendaceID_lable.grid(row=0,column=0,pady=5,sticky=W)

        attendaceID_entry=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendaceID_entry.grid(row=0,column=1,pady=5,sticky=W)

#rollno ................
        rollLable=Label(left_inside_frame,text="RollNo:",font=("comicsansns",12,"bold"),bg="white")
        rollLable.grid(row=0,column=2,pady=8,sticky=W)
        
        atten_roll=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_roll,font=("comicsansns",12,"bold"))
        atten_roll.grid(row=0,column=3,pady=8,sticky=W)

# name................
        nameLable=Label(left_inside_frame,text="Name:",font=("comicsansns",12,"bold"),bg="white")
        nameLable.grid(row=1,column=0,pady=8,sticky=W)

        atten_roll=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_name,font=("comicsansns",12,"bold"))
        atten_roll.grid(row=1,column=1,pady=8,sticky=W)

#department.................................
        depLable=Label(left_inside_frame,text="Department:",font=("comicsansns",12,"bold"),bg="white")
        depLable.grid(row=1,column=2,pady=8,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_dep,font=("comicsansns",12,"bold"))
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)
#Time.................................
        timeLable=Label(left_inside_frame,text="Time:",font=("comicsansns",12,"bold"),bg="white")
        timeLable.grid(row=2,column=0,pady=8,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_time,font=("comicsansns",12,"bold"))
        atten_time.grid(row=2,column=1,pady=8,sticky=W)

#Date.................................
        dateLable=Label(left_inside_frame,text="Date:",font=("comicsansns",12,"bold"),bg="white")
        dateLable.grid(row=2,column=2,pady=8,sticky=W)

        atten_date=ttk.Entry(left_inside_frame,width=14,textvariable=self.var_atten_date,font=("comicsansns",12,"bold"))
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

#Attendance Status.................................
        attendanceLable=Label(left_inside_frame,text="Attendance Status:",font=("comicsansns",12,"bold"),bg="white")
        attendanceLable.grid(row=3,column=0,pady=8,sticky=W)

        self.atten_status=ttk.Combobox(left_inside_frame,width=14,textvariable=self.var_atten_attendance,font=("comicsansns",12,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8,sticky=W)
        self.atten_status.current(0)


#button frames ..............................

        btn_frame=Frame(left_frame,bd=5,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=395,width=555,height=35)

        save_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

#RIGHT lable frame................
        right_frame=LabelFrame(main_frame,bd=2,bg='white', relief= RIDGE,text="ATTENDANCE DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=590,y=10,width=740,height=470)
        

        table_frame=Frame(right_frame,bd=2,relief=RIDGE,bg='white')
        table_frame.place(x=5,y=5,width=675,height=430)


        


# ========================Scrollbar=========================

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="RollNo")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Status")

        self.AttendanceReportTable["show"]="headings"

        

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease-1>",self.get_cursor)

# ======================== fetch data =========================

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
                self.AttendanceReportTable.insert('',END,values=i)

#import csv.........................
    def importCsv(self):
         global mydata
         mydata.clear()
         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("csv files","*.csv"),("all files","*.*")),parent=self.root)
         with open(fln) as myfile:
              csvread=csv.reader(myfile,delimiter=',')
              for i in csvread:
                  mydata.append(i)
              self.fetch_data(mydata)
         

#export csv...................

    def exportCsv(self):
         try:
            if len(mydata)<1:
                 messagebox.showerror("No Data","No Data to Export",parent=self.root)
                 return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Save CSV",filetypes=(("csv files","*.csv"),("all files","*.*")),parent=self.root)
            with open(fln,mode='w',newline="") as myfile:
                 exp_write=csv.writer(myfile,delimiter=',')
                #  start = pdb.set_trace()
                 roll_no=self.var_atten_roll.get()
                 id=self.var_atten_id.get()
                 name=self.var_atten_name.get()
                 time=self.var_atten_time.get()
                 dept=self.var_atten_dep.get()
                 date=self.var_atten_date.get()
                 attendance=self.var_atten_attendance.get()
                 exp_write.writerow(['{}'.format(id),'{}'.format(roll_no),'{}'.format(name),'{}'.format(dept),'{}'.format(time),'{}'.format(date),'{}'.format(attendance)])
                 for i in mydata:
                     exp_write.writerow(i)
            messagebox.showinfo("Success","Your data exported to "+os.path.basename(fln)+" successfully",parent=self.root)
         except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                


    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_id.set(rows[0])
         self.var_atten_roll.set(rows[1])
         self.var_atten_name.set(rows[2])
         self.var_atten_dep.set(rows[3])
         self.var_atten_time.set(rows[4])
         self.var_atten_date.set(rows[5])
         self.var_atten_attendance.set(rows[6])



    def reset_data(self):
         self.var_atten_id.set("")
         self.var_atten_roll.set("")
         self.var_atten_name.set("")
         self.var_atten_dep.set("")
         self.var_atten_time.set("")
         self.var_atten_date.set("")
         self.var_atten_attendance.set("")


 
if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop() 