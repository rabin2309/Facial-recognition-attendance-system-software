from tkinter import *
from tkinter import ttk
from tkinter import Tk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")

        # Variables
        self.var_attend_id = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

        # First image
        img1 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\attendance5.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl = Label(self.root, image=self.photoimg1)
        lbl.place(x=0, y=0, width=500, height=130)

        # Second Image
        img2 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\attendance4.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl = Label(self.root, image=self.photoimg2)
        lbl.place(x=500, y=0, width=500, height=130)

        # Third Image
        img3 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\attendance6.jpg")
        img3 = img3.resize((600, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl = Label(self.root, image=self.photoimg3)
        lbl.place(x=1000, y=0, width=600, height=130)

        # Background Image
        img4 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Background.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # Title
        title_lbl = Label(bg_img, text="A T T E N D A N C E   M A N A G E M E N T   S Y S T E M", font=("georgia", 35, "bold"), bg="#f0f0f0", fg="#4a4a4a")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Main Frame
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=70, width=1485, height=570)

        # Left Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("georgia", 12, "bold"))
        Left_frame.place(x=10, y=10, width=850, height=580)

        img_left = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Student4.jpg")
        img_left = img_left.resize((750, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)

        # Left Inside Frame
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=0, y=135, width=850, height=580)

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("georgia", 13, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        attendanceId_entry = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_attend_id, font=("courier", 12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        rollLabel_label = Label(left_inside_frame, text="Roll No:", font=("comicsansns", 13, "bold"), bg="white")
        rollLabel_label.grid(row=0, column=2, padx=4, pady=4)
        atten_roll = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_attend_roll, font=("courier", 12, "bold"))
        atten_roll.grid(row=0, column=3, pady=5)

        # Name
        nameLabel = Label(left_inside_frame, text="Name:", font=("georgia", 13, "bold"), bg="white")
        nameLabel.grid(row=1, column=0)
        atten_name = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_attend_name, font=("courier", 12, "bold"))
        atten_name.grid(row=1, column=1, pady=8)

        # Department
        depLabel = Label(left_inside_frame, text="Department:", font=("georgia", 13, "bold"), bg="white")
        depLabel.grid(row=1, column=2, padx=4, pady=8)
        atten_dep = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_attend_dep, font=("courier", 12, "bold"))
        atten_dep.grid(row=1, column=3, pady=8)

        # Time
        timeLabel = Label(left_inside_frame, text="Time:", font=("georgia", 13, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)
        atten_time = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_attend_time, font=("courier", 12, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside_frame, text="Date:", font=("georgia", 13, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)
        atten_date = ttk.Entry(left_inside_frame, width=18, textvariable=self.var_attend_date, font=("courier", 12, "bold"))
        atten_date.grid(row=2, column=3, pady=7)

        # Attendance Status
        attendance_label = Label(left_inside_frame, text="Attendance Status:", font=("georgia", 13, "bold"), bg="white")
        attendance_label.grid(row=3, column=0)
        self.atten_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_attend_attendance, font=("courier", 12, "bold"), state="readonly", width=20)
        self.atten_combo["values"] = ("Status", "Present", "Absent")
        self.atten_combo.current(0)
        self.atten_combo.grid(row=3, column=1, pady=8)

        # Buttons Frame
        btn_frame = Frame(left_inside_frame, bd=3, relief=RIDGE, bg="#f8f8f8")
        btn_frame.place(x=0, y=180, width=750, height=160)

        # Import CSV Button
        imp_btn = Button(
            btn_frame,
            text="Import Csv",
            command=self.importCsv,
            width=15,
            font=("Arial", 13, "bold"),
            bg="#28a745",
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#218838",
            activeforeground="white",
            cursor="hand2",
            padx=10,
            pady=10,
        )
        imp_btn.grid(row=0, padx=15, pady=10, column=0)

        # Export CSV Button
        exp_btn = Button(
            btn_frame,
            text="Export Csv",
            command=self.exportCsv,
            width=15,
            font=("Arial", 13, "bold"),
            bg="#dc3545",
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#c82333",
            activeforeground="white",
            cursor="hand2",
            padx=10,
            pady=10,
        )
        exp_btn.grid(row=0, padx=15, pady=10, column=1)

        # Reset Button
        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=15,
            font=("Arial", 13, "bold"),
            bg="#007bff",
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#0056b3",
            activeforeground="white",
            cursor="hand2",
            padx=10,
            pady=10
        )
        reset_btn.grid(row=0, padx=15, pady=10, column=2)

        # Submit Button
        submit_btn = Button(
            btn_frame,
            text="Submit",
            command=self.submit_data,
            width=15,
            font=("Arial", 13, "bold"),
            bg="#ffc107",
            fg="black",
            relief="flat",
            bd=5,
            activebackground="#e0a800",
            activeforeground="black",
            cursor="hand2",
            padx=10,
            pady=10
        )
        submit_btn.grid(row=1, column=1, padx=15, pady=10)
           
        # Right Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("georgia", 12, "bold"))
        Right_frame.place(x=780, y=10, width=700, height=500)


        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)
        
        #scroll bar table
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        # Define the Treeview Table
        self.AttendanceReportTable = ttk.Treeview(
            table_frame,
            columns=("id", "roll_no", "name", "department", "time", "date", "attendance_status"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        # Configure scrollbars
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Set Treeview headings and columns
        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll_no", text="Roll_no")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance_status", text="Attendance_Status")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll_no", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance_status", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        # Bind the get_cursor method
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

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
        back_btn.place(x=0, y=132, width=110, height=50)  # Adjusted position and size for better alignment

    
    def back_to_main(self):
        self.root.destroy()  


        # Define the get_cursor method
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        if rows:  # Ensure rows exist to prevent errors
            self.var_attend_id.set(rows[0])
            self.var_attend_roll.set(rows[1])
            self.var_attend_name.set(rows[2])
            self.var_attend_dep.set(rows[3])
            self.var_attend_time.set(rows[4])
            self.var_attend_date.set(rows[5])
            self.var_attend_attendance.set(rows[6])

       
    # Database connection
    def connect_to_db(self):
        try:
            conn = mysql.connector.connect(
                 host="localhost", username="root", password="admin@2309", database="face_recognizer"
            )
            return conn
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {e}")
            return None

    # Fetch Attendance from DB
    def fetchData(self):
        conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="admin@2309",  # Replace with your MySQL password
            database="face_recognizer"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM attendance")
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())  # Correct widget reference
            for row in rows:
                self.AttendanceReportTable.insert("", "end", values=row)
        conn.close()


    # Submit Data
    def submit_data(self):
        conn = self.connect_to_db()
        if conn is None:
            return

        cursor = conn.cursor()
        sql = """INSERT INTO attendance (attendance_id, roll_no, name, department, time, date, attendance_status)
                 VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        values = (
            self.var_attend_id.get(),
            self.var_attend_roll.get(),
            self.var_attend_name.get(),
            self.var_attend_dep.get(),
            self.var_attend_time.get(),
            self.var_attend_date.get(),
            self.var_attend_attendance.get()
        )

        try:
            cursor.execute(sql, values)
            conn.commit()
            messagebox.showinfo("Success", "Attendance has been recorded successfully!")
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Failed to insert data: {e}")
        finally:
            cursor.close()
            conn.close()

    # Reset Data
    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_dep.set("")
        self.var_attend_name.set("")
        self.var_attend_roll.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

    # Import CSV
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )

        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
                self.insert_attendance_from_csv(i)

        self.fetchData()

    def insert_attendance_from_csv(self, data):
        try:
                # Skip if data is empty
            if not data or len(data) != 7:  # Ensure all 7 columns are provided
               print("Skipping invalid data:", data)
               return
            conn = mysql.connector.connect(
                host="localhost",
                username="root",
                password="admin@2309",  # Replace with your MySQL password
                database="face_recognizer"
            )
            cursor = conn.cursor()

            # Generate unique attendanceid
            cursor.execute("SELECT MAX(attendanceid) FROM attendance")
            max_id = cursor.fetchone()[0] or 0  # Default to 0 if no records
            data[0] = max_id + 1  # Update the first column (attendanceid) dynamically


            # Corrected SQL query
            sql = """INSERT INTO attendance 
                     (attendanceid, roll_no, name, department, time, date, attendance_status) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s)
                     ON DUPLICATE KEY UPDATE attendanceid = attendanceid;
                        """

            # Debugging: Print the data being inserted
            print("Data being inserted:", data)

            # Execute the query
            cursor.execute(sql, tuple(data))
            conn.commit()

            print("Record inserted successfully!")
            conn.close()
        except mysql.connector.Error as ex:
            if "1062" in str(ex):  # Duplicate entry
                print("Duplicate entry, skipping:", data)
            else:
                print("Error during insertion:", ex)
           
    
    # Export CSV
    def exportCsv(self):
        try:
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
            with open(filename, mode="w", newline="") as file:
                writer = csv.writer(file)
                for row in mydata:
                    writer.writerow(row)
            messagebox.showinfo("Success", "Data Exported Successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export data: {e}")


    



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
