from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.iconbitmap('py.ico')
        self.root.title("Face Recognition System")
#===================variables====================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


#rku logo
        img=Image.open("img/logo.png")
        img=img.resize((200,100),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl1=Label(self.root,image=self.photoimg)
        lbl1.place(x=0,y=0,width=200,height=100)

        bg_lbl=Label(self.root,text="Student Details",font=("times new roman",45,"bold"),bg="white",fg="red")
        bg_lbl.place(x=200,y=0,width=1100,height=100)

#bg image ................
        img3 = Image.open("img/bg.jpg")
        img3 = img3.resize((1366,768), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=90, width=1366, height=768)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=20,width=1346,height=600)


        #left lable frame................
        left_frame=LabelFrame(main_frame,bd=2,bg='white', relief= RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=570,height=530)


        #img_left = Image.open("img/11.jpg")
        #img_left = img_left.resize((560, 120), Image.ANTIALIAS)
        #self.photoimg_left = ImageTk.PhotoImage(img_left)

        #f_lbl = Label(left_frame,image=self.photoimg_left)
        #f_lbl.place(x=5, y=0, width=560, height=120)

#current course ...........................
        current_course_frame=LabelFrame(left_frame,bd=2,bg='white', relief= RIDGE,text="CURRENT COURSE DETAILS",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=20,width=560,height=120)
#department.......................................
        dep_lable=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=16)
        dep_combo["values"]=("Select Department","Computer","IT","Electronics","Mechanical","Civil") 
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

#course.......................................
        dep_lable=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=0,column=2,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=16)
        dep_combo["values"]=("Select Course","Diploma","B.Tech","M.Tech","PHD") 
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

#year.......................................
        dep_lable=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=1,column=0,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=16)
        dep_combo["values"]=("Select Year","2019-20","2020-21","2021-22","2022-23") 
        dep_combo.current(0)
        dep_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
#semester.......................................
        dep_lable=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=1,column=2,padx=10,sticky=W)


        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=16)
        dep_combo["values"]=("Select Semester","1","2","3","4","5","6","7","8") 
        dep_combo.current(0)
        dep_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


#class student information ...........................
        class_student_frame=LabelFrame(left_frame,bd=2,bg='white', relief= RIDGE,text="CLASS STUDENT INFORMATION",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=160,width=560,height=315)

#student id ..............................
        studentID_lable=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentID_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=14,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
#student name ..............................
        studentName_lable=Label(class_student_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_lable.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=14,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
#student division ..............................
        studentDiv_lable=Label(class_student_frame,text="Division:",font=("times new roman",12,"bold"),bg="white")
        studentDiv_lable.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=14)
        div_combo["values"]=("Select Division","A","B","C","D","E") 
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

#student roll no ..............................
        studentRollno_lable=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        studentRollno_lable.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentRollno_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=14,font=("times new roman",12,"bold"))
        studentRollno_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
#gender ..............................
        studentGender_lable=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        studentGender_lable.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gen_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=14)
        gen_combo["values"]=("Select Gender","Male","Female","Other") 
        gen_combo.current(0)
        gen_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

#DOB ..............................
        studentDOB_lable=Label(class_student_frame,text="DOB :",font=("times new roman",12,"bold"),bg="white")
        studentDOB_lable.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        studentDOB_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=14,font=("times new roman",12,"bold"))
        studentDOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

#Email ..............................
        studentMail_lable=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        studentMail_lable.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        studentMail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=14,font=("times new roman",12,"bold"))
        studentMail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

#Phone no. ..............................
        studentPhone_lable=Label(class_student_frame,text="Phone No. :",font=("times new roman",12,"bold"),bg="white")
        studentPhone_lable.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        studentPhone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=14,font=("times new roman",12,"bold"))
        studentPhone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

# Address..............................
        studentADD_lable=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        studentADD_lable.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        studentADD_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=14,font=("times new roman",12,"bold"))
        studentADD_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

#Teacher name ...............................
        teacher_lable=Label(class_student_frame,text="Teacher Name :",font=("times new roman",12,"bold"),bg="white")
        teacher_lable.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=14,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

#Radio buttons..............................
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="TAKE PHOTO SAMPLE",value='Yes')
        radionbtn1.grid(row=6,column=0)

        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="NO SAMPLE PHOTO",value='No')
        radionbtn2.grid(row=6,column=1)


#button frames ..............................

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame.place(x=0,y=215,width=555,height=70)

        save_btn=Button(btn_frame,text="SAVE",command=self.add_data,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",command=self.reset_data,width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg='white')
        btn_frame1.place(x=0,y=245,width=555,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_data,text="TAKE PHOTO SAMPLE",width=30,font=("times new roman",12,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,command=self.update_data,text="UPDATE PHOTO SAMPLE",width=30,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #RIGHT lable frame................
        right_frame=LabelFrame(main_frame,bd=2,bg='white', relief= RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=590,y=10,width=675,height=530)


        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="SEARCH",font=("times new roman",12,"bold"))
        search_frame.place(x=0,y=20,width=720,height=80)


 
        search_lable=Label(search_frame,text="Search By :",font=("times new roman",14,"bold"),bg="red",fg="white")
        search_lable.grid(row=0,column=0,padx=10,pady=5,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","Roll_No","Phone_No") 
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W) 

        search_btn=Button(search_frame,text="Search",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=14,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
#=================================TABLE FRAME ===================================================
        table_frame=LabelFrame(right_frame,bd=2,bg='white', relief= RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        table_frame.place(x=5,y=120,width=710,height=380)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()


#=================================function declaration==================================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                        (
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_id.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get()
                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
        
            except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

#     =================================fetch data=============================
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

#================================get cursor=======================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #update function
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                 Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                 if Update>0:
                      conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                      my_cursor=conn.cursor()
                      my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_id.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()
                                                                ))
                 else:
                      if not Update:
                           return
                 messagebox.showinfo("Success","Student Details Updated Successfully",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
             except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)     


#delete function
    def delete_data(self):
         if self.var_std_id.get()=="":
                messagebox.showerror("Error","Student ID must be required",parent=self.root)
         else:
             try:
                 Delete=messagebox.askyesno("Delete","Do you want to delete this student details",parent=self.root)
                 if Delete>0:
                     conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                     my_cursor=conn.cursor()
                     my_cursor.execute("delete from student where Student_id=%s",(self.var_std_id.get(),))
                 else:
                     if not Delete:
                         return
                 messagebox.showinfo("Success","Student Details Deleted Successfully",parent=self.root)
                 conn.commit()
                 self.fetch_data()
                 conn.close()
             except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)

#reset
    def reset_data(self):
         self.var_dep.set("Select Department"),
         self.var_course.set("Select Course"),
         self.var_year.set("Select Year"),
         self.var_semester.set("Select Semester"),
         self.var_std_id.set(""),
         self.var_std_name.set(""),
         self.var_div.set("Select Division"),
         self.var_roll.set(""),
         self.var_gender.set("Select Gender"),
         self.var_dob.set(""),
         self.var_email.set(""),
         self.var_phone.set(""),
         self.var_address.set(""),
         self.var_teacher.set(""),
         self.var_radio1.set("")




# =========================Generate Data set or take photo samples=====================================

    def generate_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
             try:
                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                      id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Student_id=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                        self.var_dep.get(),
                                        self.var_course.get(),
                                        self.var_year.get(),
                                        self.var_semester.get(),
                                        self.var_std_id.get(),
                                        self.var_std_name.get(),
                                        self.var_div.get(),
                                        self.var_roll.get(),
                                        self.var_gender.get(),
                                        self.var_dob.get(),
                                        self.var_email.get(),
                                        self.var_phone.get(),
                                        self.var_address.get(),
                                        self.var_teacher.get(),
                                        self.var_radio1.get(),
                                        self.var_std_id.get()==id+1
                                                                ))     
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
             except Exception as es:
                messagebox.showerror("Error",f"Error due to {str(es)}",parent=self.root)


# ==================load predefined  data on face frontals from open cv=====================================
        face_clasifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        def face_cropped(img):
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=face_clasifier.detectMultiScale(gray,1.3,5)
            #scaling factor = 1.3
            #Minimum Neighbour = 5
            if faces is():
                return None
            for(x,y,w,h) in faces:
                cropped_face=img[y:y+h,x:x+w]
            return cropped_face
        cap=cv2.VideoCapture(0)
        img_id=0
        while True:
             ret,my_frame=cap.read()
             if face_cropped(my_frame) is not None:
                 img_id+=1
                 face=cv2.resize(face_cropped(my_frame),(450,450))
                 face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                 file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                 cv2.imwrite(file_name_path,face)
                 cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                 cv2.imshow("Cropped Face",face)
                 
        
             if cv2.waitKey(1)==13 or int(img_id)==100:
                    break
        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data Generated Successfully",parent=self.root)

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 