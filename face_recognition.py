from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
# from datetime import strftime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.iconbitmap('py.ico')
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1366,height=45)
#1st image...............................................
        img_top = Image.open("img/recognize.jpg")
        img_top = img_top.resize((550,660), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=550, height=660)


#2nd image...............................................

        img_bottom = Image.open("img/r1.jpg")
        img_bottom = img_bottom.resize((760,660), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=550, y=45, width=760, height=660)

        b5_1 = Button(f_lbl,text='Face Recognition',command=self.face_recog, cursor="hand2",font=("times new roman", 15 , "bold"), bg="dark green", fg="white")
        b5_1.place(x=235, y=500, width=300, height=40)
#===========================attendance===================================
    def mark_attendance(self,i,r,n,d):
        with open("attendance.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split(",")
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime('%d/%m/%Y')
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
#===========================face recognition==============================
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbour)
            coord = [] 
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x + w, y + h),(0,255,0), 3)
                id, predict= clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn=mysql.connector.connect(host="localhost",user="root",password="",database="face_recognizer")
                mycursor=conn.cursor()

                mycursor.execute("select Name from student where Student_id="+str(id))
                n=mycursor.fetchone()
                n="+".join(n)

                mycursor.execute("select Roll from student where Student_id="+str(id))
                r=mycursor.fetchone()
                r="+".join(r)

                mycursor.execute("select Dep from student where Student_id="+str(id))
                d=mycursor.fetchone()
                d="+".join(d)

                mycursor.execute("select Student_id from student where Student_id="+str(id))
                i=mycursor.fetchone()
                i="+".join(str(i))



                if confidence > 72:
                    cv2.putText(img,f"ID :{i}",(x,y-75),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),3)

                coord=[x,y,w,h]

            return coord
        


        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10,(255,25,255), "Face", clf)
            return img  
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognisation",img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop() 