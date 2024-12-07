from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import datetime
import mysql.connector
from student import Student
from train import Train
from my_face_recognition import Face_Recognition
from attendance import Attendance
from help import Help
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x1200+0+0")
        self.root.title("Facial Recognition System")

        # Top toggle button for sidebar
        self.toggle_btn = Button(self.root, text="✖", font=("Helvetica", 12, "bold"), fg="white", bg="#2C3E50",  activebackground="#34495E", activeforeground="white", bd=0, command=self.toggle_sidebar)
        self.toggle_btn.pack(pady=10, anchor="w", padx=20)

        # Sidebar (Navigation Bar)
        self.sidebar = Frame(self.root, bg="#2C3E50", width=300)
        self.sidebar.pack(side=LEFT, fill=Y)

        # Logo Image and Title
        logo_img = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\logoes.png")
        logo_img = logo_img.resize((50, 50), Image.LANCZOS)  # Resize the logo if necessary
        self.logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = Label(self.sidebar, text="  FRAS", font=("Helvetica", 25, "bold"), fg="white", bg="#2C3E50", image=self.logo_photo, compound=LEFT)
        logo_label.pack(pady=20)


        # Initialize the welcome message label
        self.welcome_label = Label(self.root, text="WELCOME TO FACIAL RECOGNITION ATTENDANCE SYSTEM SOFTWARE", font=("arial", 24, "bold"), fg="black")
        self.welcome_label.place(x=-600, y=5)  # Start the label off-screen to the left

        # Start the sliding animation
        self.animate_welcome()

        

        # Sidebar buttons with hover effect
        self.create_nav_button("Dashboard", self.show_dashboard, 1)
        self.create_nav_button("Student Details", self.student_details, 2)
        self.create_nav_button("Face Detector", self.face_data, 3)
        self.create_nav_button("Attendance", self.attendance_data, 4)
        self.create_nav_button("Train Data", self.train_data, 5)
        self.create_nav_button("Photos", self.open_img, 6)
        self.create_nav_button("Help Desk", self.help_data, 7)
        self.create_nav_button("Exit", self.iExit, 8)

        # Main content area (dynamic content)
        self.content_frame = Frame(self.root, bg="#f0f0f0")
        self.content_frame.pack(side=RIGHT, fill=BOTH, expand=True)
        
        

        # Initialize dashboard label
        #self.dashboard_label = Label(self.scrollable_frame, text="Welcome to the Dashboard", font=("Helvetica", 30, "bold"), bg="#f0f0f0")
        self.show_dashboard()  # Show dashboard initially

        # Initialize clock
        self.clock_label = Label(self.root, font=("Helvetica", 20, "bold"), fg="white", bg="#2C3E50")
        self.clock_label.place(relx=0.98, rely=0.01, anchor="ne")  # Place clock in top right corner
        self.update_clock()  # Start the clock updating
        
    
    
    def animate_welcome(self):
        # Function to animate the welcome label from left to right continuously
        current_x = self.welcome_label.winfo_x() + 2  # Move 2 pixels to the right (slower speed)

        # If the label moves off screen to the right, reset to start from the left again
        if current_x > self.root.winfo_width():
            current_x = -self.welcome_label.winfo_width()

        # Update the label's position
        self.welcome_label.place(x=current_x, y=5)

        # Call this function again after 50 ms for continuous movement
        self.root.after(50, self.animate_welcome)

     
     
    def create_nav_button(self, text, command, index, icon_path=None):
        def on_enter(e):
            button.config(bg="#5DADE2", fg="white")  # Highlight on hover

        def on_leave(e):
            button.config(bg="#34495E", fg="white")  # Revert to default

        
        
        # Sidebar Button directly on root (main window)
        button = Button(
            self.sidebar, text=text, command=command, 
            font=("Helvetica", 14, "bold"), 
            bg="#34495E", fg="white", 
            activebackground="#2C3E50", activeforeground="white",
            bd=0, padx=10, pady=5, cursor="hand2"
        )
        button.pack(fill=X, pady=8, padx=10)
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        

    def add_hover_effect(self, button):
        button.bind("<Enter>", lambda e: button.config(bg="#34495E"))
        button.bind("<Leave>", lambda e: button.config(bg="#2C3E50"))

    def toggle_sidebar(self):
        if self.sidebar.winfo_ismapped():
            self.sidebar.pack_forget()  # Hide sidebar
            self.content_frame.pack(side=LEFT, fill=BOTH, expand=True)
            self.toggle_btn.config(text="☰")  # Update button text
        else:
            self.sidebar.pack(side=LEFT, fill=Y)  # Show sidebar
            self.content_frame.pack(side=RIGHT, fill=BOTH, expand=True)
            self.toggle_btn.config(text="✖")  # Update button text

    def clear_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
    # Clear content frame before adding new widgets
        self.clear_content_frame()
       

        # Define the path to the dashboard image
        img_path = r"C:\Users\HP\Desktop\facial_recognition system\college_images\student7.jpg"
        # Check if the image file exists before opening
        if os.path.exists(img_path):
            img = Image.open(img_path)
            img = img.resize((1530, 710), Image.LANCZOS)  # Resize the background to fit the dashboard size
            self.photoimg4 = ImageTk.PhotoImage(img)  # Store the image reference
        else:
            print(f"Error: {img_path} not found.")
            return  # Skip dashboard setup if image is not found

        # Create a Label widget to hold the background image
        bg_img = Label(self.content_frame, image=self.photoimg4)
        bg_img.place(x=0, y=0, width=1530, height=780)  # Place background image inside the content frame

        # Statistics Panel
        stats_frame = Frame(bg_img, bg="white", bd=5, relief=RIDGE)
        stats_frame.place(x=50, y=540, width=1260, height=135)

        stats = [
            ("Total Students", self.get_total_students(), "students_icon.png"),
            ("Total Attendance", f"{self.get_average_attendance()}%", "attendance_icon.png"),
            ("Last Login", datetime.datetime.now().strftime("%d-%m-%Y %H:%M"), "login_icon.png"),
        ]

        for i, (label, value, icon_path) in enumerate(stats):
            # Individual Stat Frame
            stat_frame = Frame(stats_frame, bg="#34495E", bd=0, relief=FLAT)
            stat_frame.place(x=20 + i * 410, y=10, width=400, height=110)

            # Icon Placeholder (replace with actual icons if available)
            icon_label = Label(stat_frame, text="🔹", font=("Helvetica", 30), bg="#34495E", fg="white")
            icon_label.place(x=10, y=25)

            # Stat Label
            text_frame = Frame(stat_frame, bg="#34495E")
            text_frame.place(x=80, y=10, width=310, height=90)

            Label(text_frame, text=label, font=("Poppins", 16, "bold"), fg="white", bg="#34495E").pack(anchor="w", pady=2)
            Label(text_frame, text=value, font=("Helvetica", 24, "bold"), fg="#FFD700", bg="#34495E").pack(anchor="w", pady=5)

        
       
     # Quick Actions Frame
        action_frame = Frame(bg_img, bg="#34495E", bd=5, relief=RIDGE)
        action_frame.place(x=50, y=150, width=1250, height=110)

        # Button Styles
        def on_enter(e):
            e.widget['bg'] = '#5DADE2'

        def on_leave(e):
            e.widget['bg'] = 'blue'

        actions = [
            ("Start Recognition", self.face_data, "start_icon.png"),
            ("Manage Students", self.student_details, "manage_icon.png"),
            ("View Attendance", self.attendance_data, "attendance_icon.png"),
            ("Train Data", self.train_data, "train_icon.png"),
        ]

        for i, (label, command, icon_path) in enumerate(actions):
            # Use icons if available
            button_frame = Frame(action_frame, bg="#34495E")
            button_frame.pack(side=LEFT, expand=True, fill=BOTH, padx=10, pady=5)
            
            # Use Label to simulate buttons for rounded corners
            button = Label(
                button_frame, text=label, font=("Helvetica", 20, "bold"),
                fg="white", bg="blue", relief=RAISED, bd=2, padx=10, pady=5,
                cursor="hand2"
            )
            button.bind("<Enter>", on_enter)
            button.bind("<Leave>", on_leave)
            button.bind("<Button-1>", lambda e, cmd=command: cmd())

            button.pack(expand=True, fill=BOTH)
   
        
        
        
         # Adding a subtle shadow effect
        shadow_lbl = Label(
            bg_img,
            bg="#003153",  # Slightly darker shade of the main background
        )
        shadow_lbl.place(x=-5, y=0, width=1530, height=90)  # Shadow dimensions just slightly larger than title

        
        # Logo Image and Title
        title_img = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\logoes.png")
        title_img = title_img.resize((50, 50), Image.LANCZOS)  # Resize the logo if necessary
        self.title_logo_photo = ImageTk.PhotoImage(title_img)
        title_lbl = Label(
            bg_img,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("Helvetica", 30, "bold"), 
            bg="#2C3E50",  # Dark blue background
            fg="white", 
            image=self.title_logo_photo,  # Add an image for branding
            compound=LEFT,  # Position the image to the left of the text
            padx=10,
            pady=10# Add padding between the image and text
        )
        title_lbl.place(x=-80, y=0, width=1630, height=80)

       
    
   

    def update_clock(self):
        # Get the current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        # Update the clock label's text
        self.clock_label.config(text=current_time)
        
        # Call this function again after 1000 milliseconds (1 second)
        self.clock_label.after(1000, self.update_clock)
        
    
    

    def open_img(self):
        try:
            os.startfile("data")
        except FileNotFoundError:
            messagebox.showerror("Error", "The 'data' directory was not found.")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")


    def get_total_students(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
            cursor = conn.cursor()

            # Query to count the number of students
            query = "SELECT COUNT(*) FROM student"
            cursor.execute(query)
            result = cursor.fetchone()

            # Return the count
            return result[0]

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "Error"

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()


  
    def get_average_attendance(self):
        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
               

            cursor = conn.cursor()

            # Query to fetch the attendance data
            query = "SELECT attendance_status FROM attendance"
            cursor.execute(query)

            # Fetch all the records
            records = cursor.fetchall()

            # Count the total attendance and present counts
            total_classes = len(records)
            present_count = sum(1 for record in records if record[0] == 'Present')

            # Calculate the average attendance percentage
            if total_classes > 0:
                average_attendance = (present_count / total_classes) * 100
            else:
                average_attendance = 0

            return round(average_attendance, 2)

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()



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
        exit_confirmation = messagebox.askyesno("Facial Recognition", "Are you sure want to exit this project?")
        if exit_confirmation > 0:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()