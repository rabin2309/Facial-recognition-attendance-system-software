


from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from student import Student
from train import Train
from my_face_recognition import Face_Recognition
from attendance import Attendance
from help import Help

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        
        
        # First image
        img1 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\second.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbl = Label(self.root, image=self.photoimg1)
        lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img2 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\firstimg.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl = Label(self.root, image=self.photoimg2)
        lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img3 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\second.jpg")
        img3 = img3.resize((600, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbl = Label(self.root, image=self.photoimg3)
        lbl.place(x=1000, y=0, width=600, height=130)

        # Loading and resizing the image for background images
        img4 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Background.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        
        # Load the logo image
        logo_img = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\logoes.png")  # Specify the correct path to your logo image
        logo_img = logo_img.resize((50, 50), Image.LANCZOS)  # Resize the logo if necessary
        self.logo_photo = ImageTk.PhotoImage(logo_img)

# Title with Logo and Text
        title_lbl = Label(bg_img, text="  FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",  # Add a space after the logo
                font=("Helvetica", 35, "bold"), bg="#0f4c81", fg="white",
                image=self.logo_photo, compound=LEFT, padx=2)  # Use image, compound=LEFT to place image on the left
        title_lbl.place(x=0, y=0, width=1530, height=60)


        # Student button
        img5 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\button1.jpg")
        img5 = img5.resize((220, 220), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, command=self.student_details,compound=TOP, cursor="hand2")
        b1.place(x=100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details, cursor="hand2",
                      font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=100, y=300, width=220, height=40)

        # Detecting face
        img6 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button2.jpg")
        img6 = img6.resize((220, 220), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data,
                      font=("georgia", 15, "bold"),bg="#4a90e2", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance
        img7 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button3.jpg")
        img7 = img7.resize((220, 220), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.attendance_data)
        b1.place(x=850, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data,
                      font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=850, y=300, width=220, height=40)

        # Help Desk
        img8 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button4.png")
        img8 = img8.resize((220, 220), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.help_data)
        b1.place(x=1200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data,
                      font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=1200, y=300, width=220, height=40)

        # Train Data
        img9 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button5.png")
        img9 = img9.resize((220, 220), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.train_data)
        b1.place(x=100, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=100, y=600, width=220, height=40)

        # Photos
        img10 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button6.jpg")
        img10 = img10.resize((220, 220), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img,font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=500, y=600, width=220, height=40)

        # Developer
        img11 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button7.jpg")
        img11 = img11.resize((220, 220), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=850, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2",
                      font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=850, y=600, width=220, height=40)

        # Exit Button
        img12 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Button8.jpg")
        img12 = img12.resize((220, 220), Image.LANCZOS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b1 = Button(bg_img, image=self.photoimg12, cursor="hand2",command=self.iExit)
        b1.place(x=1200, y=400, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit,
                      font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        b1_1.place(x=1200, y=600, width=220, height=40)
    
    
    
    def create_button(self, parent, image_path, command, text, x, y):
        img = Image.open(image_path).resize((220, 220), Image.LANCZOS)
        photo_img = ImageTk.PhotoImage(img)
        button = Button(parent, image=photo_img, cursor="hand2", command=command)
        button.place(x=x, y=y, width=220, height=220)
        button.image = photo_img  # To prevent garbage collection
    
        lbl = Button(parent, text=text, cursor="hand2", command=command,
                     font=("georgia", 15, "bold"), bg="#4a90e2", fg="white")
        lbl.place(x=x, y=y + 200, width=220, height=40)
        

        
    def open_img(self):
        try:
            os.startfile("data")
        except FileNotFoundError:
            messagebox.showerror("Error", "The 'data' directory was not found.")

        
        
        
#Function Button


    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
        
        
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)    
    
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)    
    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)    
    
    def iExit(self):
        exit_confirmation=messagebox.askyesno("Facial Recognition","Are you sure want to exit this project?")
        if exit_confirmation>0:
           self.root.destroy()
        else:
            return    


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()