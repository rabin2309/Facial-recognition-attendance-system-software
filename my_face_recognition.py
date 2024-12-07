
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import csv
import cv2
import os 
import numpy as np
import pyttsx3



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 1 is for female voice and 0 is for male voice


def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()



class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        
        
        
        # Load images and set up the GUI
        img1 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\recog.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl = Label(self.root, image=self.photoimg1)
        lbl.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\train3.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl = Label(self.root, image=self.photoimg2)
        lbl.place(x=500, y=0, width=500, height=130)

        img3 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\recog3.jpg")
        img3 = img3.resize((600, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl = Label(self.root, image=self.photoimg3)
        lbl.place(x=1000, y=0, width=600, height=130)

        img4 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\recog5.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)


        title_lbl = Label(
        bg_img,
        text="✨ F A C E   R E C O G N I T I O N ✨",
        font=("Georgia", 42, "bold"),  # Increased font size slightly for impact
        bg="#e6e6e6",  # A softer gray background for a polished look
        fg="#333333",  # Darker text color for contrast
        relief="groove",  # Adds a subtle border
        bd=3  # Border width for a defined look
        )
        title_lbl.place(x=0, y=0, width=1530, height=70)  # Adjusted height for better spacing


        b1_1 = Button(
        bg_img,
        text="🎭 Face Recognition",
        cursor="hand2",
        command=self.face_recog,
        font=("Courier", 15, "bold"),  # Slightly larger font for better visibility
        bg="green",  # A softer green shade (Bootstrap success green)
        fg="white",  # White text for contrast
        activebackground="#218838",  # Darker green when hovered
        activeforeground="white",  # Keep text white when hovered
        relief="raised",  # Raised button for a 3D effect
        bd=3  # Slightly thicker border for emphasis
        )
        b1_1.place(x=980, y=340, width=240, height=60)  # Adjusted position and size for balance


        title_lbl = Label(
        bg_img, 
        text="⛔ Please Press Enter to Terminate ⛔",
        font=("Georgia", 18, "bold"), 
        bg="#ffcccc",  # Light red background for a warning feel
        fg="darkred",  # Dark red text for better visibility
        relief="solid",  # Adds a solid border
        bd=2,  # Border width
        padx=10,  # Padding for a spacious look
        pady=5  # Padding for a spacious look
        )
        title_lbl.place(x=750, y=500, width=500, height=50)  # Adjusted dimensions for better alignment

       # Back Button
        back_btn = Button(
            self.root,
            text="⬅Back",
            font=("Courier", 20, "bold"),  # Retained the bold font for emphasis
            fg="white",  # White text for better contrast
            bg="#007BFF",  # A vibrant blue shade (Bootstrap primary blue)
            activebackground="#0056b3",  # Darker blue for hover effect
            activeforeground="white",  # Maintain white text on hover
            command=self.back_to_main,
            cursor="hand2",  # Hand cursor to indicate interactivity
            relief="raised",  # Slight 3D effect
            bd=3  # Slightly thicker border for better definition
        )
        back_btn.place(x=0, y=132, width=120, height=68)  # Adjusted position and size for better alignment


    def back_to_main(self):
        self.root.destroy()  # Close the Help window and return to the main window

        
      
      #Attendance
    def mark_attendance(self,i,r,n,d):
         # Check if the attendance file exists, if not, create it
        if not os.path.isfile("Student_attendance_list.csv"):
            with open("Student_attendance_list.csv", "w", newline="") as f:
                writer = csv.writer(f)
                # Write the header row
                writer.writerow(["Student ID", "Roll No", "Name", "Date"])

        with open("Student_attendance_list.csv","r+", newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            
            if((str(i) not in name_list) and (str(r) not in name_list) and (str(n) not in name_list) and (str(d) not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")         
        
        

   #aface recognition
    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))
                
                
                conn = mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
                my_cursor = conn.cursor()
                
                my_cursor.execute("select Student_id from student where Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(map(str, i)) if i else "Unknown"

                my_cursor.execute("select Roll_No from student where Student_id=" + str(id))
                r = my_cursor.fetchone()
                r="+".join(r) if r else "Unknown"  
                   
                
                
                my_cursor.execute("select Student_Name from student where Student_id=" + str(id))
                n = my_cursor.fetchone()
                n="+".join(n) if n else "Unknown"
                
                my_cursor.execute("select Department from student where Student_id=" + str(id))
                d = my_cursor.fetchone()
                d="+".join(d) if d else "Unknown"   
                
                if predict < 500:
                # if result[1] < 500:
                    confidence=int((100*(1-predict/300)))
                    # str2 = str(confidence)
                    # confidence = int(100 * (1 - (result[1])/300))
                    # display_string = str(confidence)+'% confidence it is user'
                # cv2.putText(img,display_string(250, 250), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
                    cv2.putText(img,f"Accuracy:{confidence}%",(x, y-125), cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
   
               
                

                if confidence > 70: 
                    cv2.putText(img, f"Student_id:{i}", (x, y-95), cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255), 3)
                    cv2.putText(img, f"Roll:{r}", (x, y-65), cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-35), cv2.FONT_HERSHEY_COMPLEX,0.8,(255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX,0.8, (255, 255, 255), 3) 
                    
                    self.mark_attendance(i,r,n,d)
                else:
                   
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                   
                    cv2.putText(img, f"Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
           
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)
        
        

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)
          
            if cv2.waitKey(1) == 13:  # Enter key
          
                break

        video_cap.release()
        cv2.destroyAllWindows()
        
    

        
#creating objects

if __name__ == "__main__":
          root = Tk()
          obj = Face_Recognition(root)
          root.mainloop()
