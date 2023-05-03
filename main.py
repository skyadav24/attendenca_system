from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
from student import Student
from datetime import datetime
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from PIL import Image
# from developer import Developer
# from help import Help



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.iconbitmap('py.ico')
        self.root.title("Attendence System")

        #rku logo
        img=Image.open("img/logo.png")
        img=img.resize((200,100),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl1=Label(self.root,image=self.photoimg)
        lbl1.place(x=0,y=0,width=200,height=100)

        bg_lbl=Label(self.root,text="RKU Attendence System",font=("times new roman",45,"bold"),bg="white",fg="red",padx=10)
        bg_lbl.place(x=200,y=0,width=1100,height=100)

#bg image ................
        img3 = Image.open("img/bg.jpg")
        img3 = img3.resize((1366,768), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=100, width=1366, height=768)  

# =================time==========================
       # def time():
        #         string=datetime.strftime("%H:%M:%S %p")
        #         self.lbl_clock.config(text=string)
        #         self.lbl_clock.after(1000,self.time)


        # lbl= Label(title_lbl,font=("times new roman",15,"bold"),bg="white",fg="blue")
        # lbl.place(x=0,y=0,width=110,height=50)
        # time()


 # Student Button.....................       
        img4 = Image.open("img/student.jpg")
        img4 = img4.resize((210,190), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=100, y=50, width=210, height=190)


        b1_1 = Button(bg_img,text='STUDENT DETAILS',command=self.student_details,cursor="hand2",font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b1_1.place(x=100, y=240, width=210, height=40)

 # face scanner Button.....................       
        img5 = Image.open("img/face.png")
        img5 = img5.resize((210,190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.Face_data) 
        b2.place(x=550, y=50, width=210, height=190)


        b2_1 = Button(bg_img,text='FACE SCANNER', cursor="hand2",command=self.Face_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b2_1.place(x=550, y=240, width=210, height=40)

# attendance Button.....................       
        img6 = Image.open("img/attendance.jpg")
        img6 = img6.resize((210,190), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attendance_data)
        b3.place(x=1000, y=50, width=210, height=190)


        b3_1 = Button(bg_img,text='ATTENDANCE', cursor="hand2",command=self.attendance_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b3_1.place(x=1000, y=240, width=210, height=40)


# # help Button.....................       
#         img7 = Image.open("img/help.jpg")
#         img7 = img7.resize((210,190), Image.LANCZOS)
#         self.photoimg7 = ImageTk.PhotoImage(img7)

#         b4 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.help_data)
#         b4.place(x=1000, y=60, width=210, height=190)


#         b4_1 = Button(bg_img,text='HELP', cursor="hand2",command=self.help_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
#         b4_1.place(x=1000, y=250, width=210, height=40)


# Train Button.....................       
        img8 = Image.open("img/training.jpg")
        img8 = img8.resize((210,190), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=100, y=320, width=210, height=190)


        b5_1 = Button(bg_img,text='TRAIN', cursor="hand2",command=self.train_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b5_1.place(x=100, y=500, width=210, height=40)


# Photos Button.....................       
        img9 = Image.open("img/photo.jpg")
        img9 = img9.resize((210,190), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b6.place(x=550, y=320, width=210, height=190)


        b6_1 = Button(bg_img,text='PHOTOS', cursor="hand2",command=self.open_img,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b6_1.place(x=550, y=500, width=210, height=40)



# # Developer  Button.....................       
#         img10 = Image.open("img/developer.jpg")
#         img10 = img10.resize((210,190), Image.LANCZOS)
#         self.photoimg10 = ImageTk.PhotoImage(img10)

#         b7 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
#         b7.place(x=700, y=320, width=210, height=190)


#         b7_1 = Button(bg_img,text='DEVELOPER', cursor="hand2",command=self.developer_data,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
#         b7_1.place(x=700, y=500, width=210, height=40)


# Exit Button.....................       
        img11 = Image.open("img/exit.jpg")
        img11 = img11.resize((210,190), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b8.place(x=1000, y=320, width=210, height=190)


        b8_1 = Button(bg_img,text='EXIT', cursor="hand2",command=self.iExit,font=("times new roman", 15 , "bold"), bg="brown", fg="white")
        b8_1.place(x=1000, y=500, width=210, height=40)


    def open_img(self):
        os.startfile("data")


    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Face Recognition System", "do you want to exit",parent=self.root)
        if  self.iExit > 0:
            self.root.destroy()
        else:
            return


# ==============================Function Buttons====================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    def Face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    # def developer_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Developer(self.new_window)
    # def help_data(self):
    #     self.new_window=Toplevel(self.root)
    #     self.app=Help(self.new_window)

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
 