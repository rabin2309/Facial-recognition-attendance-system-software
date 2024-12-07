from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        
        
        
        #variables
        self.var_dep=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_roll=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
        self.var_phone=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_tec_name=StringVar()
        self.var_tec_sub=StringVar()
        self.var_photo=StringVar()
                
        # First image
        img1 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\student1.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

       
        lbl = Label(self.root, image=self.photoimg1)
        lbl.place(x=0, y=0, width=500, height=130)
        
        
        
         # Second Image
        img2 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\student1.jpg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        # Optionally, you might want to display the image in a label
        lbl = Label(self.root, image=self.photoimg2)
        lbl.place(x=500, y=0, width=500, height=130)
        
        
        
         # Third Image
        img3 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\student1.jpg")
        img3 = img3.resize((600, 130), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        # Optionally, you might want to display the image in a label
        lbl = Label(self.root, image=self.photoimg3)
        lbl.place(x=1000, y=0, width=600, height=130)
        
          # Loading and resizing the image for background images
        img4 = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Background.jpg")
        img4 = img4.resize((1530, 710), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        # Optionally, you might want to display the image in a label
        bg_img = Label(self.root, image=self.photoimg4)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img, text="S T U D E N T  M A N A G E M E N T  S Y S T E M",font=("georgia",35,"bold"),bg="#f0f0f0", fg="#4a4a4a")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #creating frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)
        
        #left label frame
        
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("georgia",12,"bold"))
        Left_frame.place(x=10, y=10, width=760,height=580)
        
        img_left = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Student4.jpg")
        img_left= img_left.resize((750, 130), Image.LANCZOS)
        self.photoimg_left =ImageTk.PhotoImage(img_left)

        # Optionally, you might want to display the image in a label
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=750, height=130)
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("georgia",13,"bold"))
        current_course_frame.place(x=5, y=135, width=750,height=80)
        
        #Department
        dep_label=Label(current_course_frame,text="Department:",font=("georgia",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("courier",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Bsc:CSIT","BCA","BIT")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        
        
        #Semester
        semester_label=Label(current_course_frame,text="Semester:",font=("georgia",13,"bold"),bg="white")
        semester_label.grid(row=0,column=2,padx=10,sticky=W)
        
        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("courier",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","First Semester","Second Semester","Third Semester","Fourth Semester","Fifth Semester","Six Semester","Seven Semester","Eight Semester")
        semester_combo.current(0)
        semester_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
        
        #class Student Information
        class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text=" Class Student Information",font=("georgia",13,"bold"))
        class_Student_frame.place(x=5, y=220, width=750,height=330)
        
        #student ID
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("georgia",13,"bold"),bg="white")
        studentId_label.grid(row=0, column=0,padx=10, pady=5, sticky=W)
        
        studentId_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_id,font=("courier",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student Name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("georgia",13,"bold"),bg="white")
        studentName_label.grid(row=0, column=2,padx=10, pady=5, sticky=W)
        
        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("courier",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
         #student Rollno
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("georgia",13,"bold"),bg="white")
        roll_no_label.grid(row=1, column=0,padx=10, pady=5, sticky=W)
        
        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("courier",12,"bold"))
        roll_no_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
         #student DOB
        dob_label=Label(class_Student_frame,text="Date of Birth:",font=("georgia",13,"bold"),bg="white")
        dob_label.grid(row=1, column=2,padx=10, pady=5, sticky=W)
        
        dob_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_dob,font=("courier",12,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
         #student Address:
        address_label=Label(class_Student_frame,text="Address:",font=("georgia",13,"bold"),bg="white")
        address_label.grid(row=2, column=0,padx=10, pady=5, sticky=W)
        
        address_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_address,font=("courier",12,"bold"))
        address_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        
        
         #student Phone no:
        phone_label=Label(class_Student_frame,text="Phone Number:",font=("georgia",13,"bold"),bg="white")
        phone_label.grid(row=2, column=2,padx=10, pady=5, sticky=W)
        
        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("courier",12,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("georgia",13,"bold"),bg="white")
        gender_label.grid(row=3,column=0,padx=10, pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("courier",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender:","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=3,column=1,padx=10,pady=10,sticky=W)
        
        
         #student E-mail:
        email_label=Label(class_Student_frame,text="E-mail:",font=("georgia",13,"bold"),bg="white")
        email_label.grid(row=3, column=2,padx=10, pady=5, sticky=W)
        
        email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("courier",12,"bold"))
        email_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
         #Teacher NAME
        TeacherName_label=Label(class_Student_frame,text="Teacher Name:",font=("georgia",13,"bold"),bg="white")
        TeacherName_label.grid(row=4, column=0,padx=10, pady=5, sticky=W)
        
        TeacherName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_tec_name,width=20,font=("courier",12,"bold"))
        TeacherName_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
        
        #Teacher subject
        TeacherSubject_label=Label(class_Student_frame,text="Teacher's Subject:",font=("georgia",13,"bold"),bg="white")
        TeacherSubject_label.grid(row=4, column=2,padx=10, pady=5, sticky=W)
        
        TeacherSubject_entry=ttk.Entry(class_Student_frame,textvariable=self.var_tec_sub,width=20,font=("courier",12,"bold"))
        TeacherSubject_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)
        
        #radio button
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,padx=20,pady=10,column=0)
        
       
        radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="NO")
        radiobtn2.grid(row=6,padx=10,pady=10,column=1)
        
        # Buttons Frame 1
      
        
        btn_frame=Frame(class_Student_frame,bd=3,relief=RIDGE,bg="#f0f0f0")
        btn_frame.place(x=0, y=225, width=750, height=180)
        
        # Save Button
        save_btn = Button(
            btn_frame,
            text="Save",
            command=self.add_data,
            width=10,
            font=("Arial", 13, "bold"),
            bg="#28a745",  # Green
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#218838",
            activeforeground="white",
            cursor="hand2"
        )
        save_btn.grid(row=0, column=0, padx=10, pady=5)

        # Update Button
        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=10,
            font=("Arial", 13, "bold"),
            bg="#007bff",  # Blue
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#0056b3",
            activeforeground="white",
            cursor="hand2"
           
        )
        update_btn.grid(row=0, column=1, padx=10, pady=5)

        # Delete Button
        delete_btn = Button(
            btn_frame,
            text="Delete",
            command=self.delete_data,
            width=10,
            font=("Arial", 13, "bold"),
            bg="#dc3545",  # Maroon
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#c82333",
            activeforeground="white",
            cursor="hand2"
           
        )
        delete_btn.grid(row=0, column=2, padx=10, pady=5)

        # Reset Button
        reset_btn = Button(
            btn_frame,
            text="Reset",
            command=self.reset_data,
            width=10,
            font=("Arial", 13, "bold"),
            bg="#ffc107",  # Olive/Yellow
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#e0a800",
            activeforeground="white",
            cursor="hand2"
           
        )
        reset_btn.grid(row=0, column=3, padx=10, pady=5)

        # Take Photo Button
        take_photo_btn = Button(
            btn_frame,
            command=self.generate_dataset,
            text="Take Photo Sample",
            width=20,
            font=("Arial", 13, "bold"),
            bg="#6f42c1",  # Purple
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#5a32a3",
            activeforeground="white",
            cursor="hand2",
            
        )
        take_photo_btn.grid(row=1, column=0, padx=15, pady=0)

        # Update Photo Button
        update_photo_btn = Button(
            btn_frame,
            text="Update Photo Sample",
            width=20,
            font=("Arial", 13, "bold"),
            bg="#001f3d",  # Navy
            fg="white",
            relief="flat",
            bd=5,
            activebackground="#003366",
            activeforeground="white",
            cursor="hand2"
           
        )
        update_photo_btn.grid(row=1, column=1, padx=15, pady=5)
        #Right label frame
        
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Record",font=("georgia",13,"bold"))
        Right_frame.place(x=780, y=10, width=685,height=580)
        
        #Right LABEL Form
        img_right = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\Student7.jpg")
        img_right= img_right.resize((750, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        # Optionally, you might want to display the image in a label
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=750, height=130)
        
      #Search Frame
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search Student Information",font=("georgia",13,"bold"))
        Search_frame.place(x=5, y=135, width=675,height=70)
        
        search_label=Label(Search_frame,text="Search By:",font=("courier",15,"bold"),bg="brown",fg="white")
        search_label.grid(row=0, column=0,padx=10, pady=5, sticky=W)
        
        self.var_com_search=StringVar()
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=("courier",12,"bold"),state="readonly",width=13)
        search_combo["values"]=("Select","Roll No","Phone")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search=StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=12,font=("georgia",12,"bold"))
        search_entry.grid(row=0,column=2,padx=5,sticky=W)
        
        
        search_btn=Button(Search_frame,command=self.search_data, text="SEARCH",width=10,font=("courier",12,"bold"),bg="green",fg="white")
        search_btn.grid(row=0,padx=5, column=3)
        
        
        showAll_btn=Button(Search_frame,command=self.fetch_data, text="Show All",width=10,font=("courier",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0, column=4)
        
        
        #table frame
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5, y=210, width=670,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","sem","id","name","rollno","dob","add","phone","gender","email","tec_name","tec_sub","photo","role"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                                        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Student Name")
        self.student_table.heading("rollno",text="Roll No")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("add",text="Address")
        self.student_table.heading("phone",text="Phone No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("email",text="E-mail")
        self.student_table.heading("tec_name",text="Teacher Name")
        self.student_table.heading("tec_sub",text="Teacher Subject")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("rollno",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("add",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("gender",width=100) 
        self.student_table.column("email",width=100)
        self.student_table.column("tec_name",width=100) 
        self.student_table.column("tec_sub",width=100)
        self.student_table.column("photo",width=150)
                 
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
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
        back_btn.place(x=0, y=132, width=120, height=50)  # Adjusted position and size for better alignment

        

    def back_to_main(self):
        self.root.destroy()  # Close the Help window and return to the main window


        
        
        
        
        
        
        
        
        
        
      #function declaration
    def add_data(self):
          if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
              messagebox.showerror("Error", "All Fields are required!!", parent=self.root)
          else:
              try:
                  conn = mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
                  my_cursor = conn.cursor()
                  my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                      self.var_dep.get(),
                      self.var_semester.get(),
                      self.var_std_id.get(),
                      self.var_std_name.get(),
                      self.var_roll.get(),
                      self.var_dob.get(),
                      self.var_address.get(),
                      self.var_phone.get(),
                      self.var_gender.get(),
                      self.var_email.get(),
                      self.var_tec_name.get(),
                      self.var_tec_sub.get(),
                      self.var_radio1.get()
                  ))

                  conn.commit()
                  self.fetch_data()
                  
                  conn.close()
                  messagebox.showinfo("Success", "Student details have been added successfully!", parent=self.root)
              except Exception as es:
                  messagebox.showerror("Error",f"Due To : {str(es)}", parent=self.root)
          
          #function declaration        
    def fetch_data(self):
        try:
            conn = mysql.connector.connect(
            host="localhost",
            username="root",
            password="admin@2309",
            database="face_recognizer"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) != 0:
            # Clear existing data in the table
                self.student_table.delete(*self.student_table.get_children())
            # Insert new data
            for i in data:
                self.student_table.insert("", END, values=i)

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
        # Close cursor and connection in the finally block to ensure they're closed even if an error occurs
            if my_cursor:
                my_cursor.close()
        if conn and conn.is_connected():
            conn.close()

                    
        #function declaration
    def get_cursor(self,event=""):
          cursor_focus=self.student_table.focus()
          content=self.student_table.item(cursor_focus)
          data=content["values"]
          if data:
            self.var_dep.set(data[0])
            self.var_semester.set(data[1])
            self.var_std_id.set(data[2])
            self.var_std_name.set(data[3])
            self.var_roll.set(data[4])
            self.var_dob.set(data[5])
            self.var_address.set(data[6])
            self.var_phone.set(data[7])
            self.var_gender.set(data[8])
            self.var_email.set(data[9])
            self.var_tec_name.set(data[10])
            self.var_tec_sub.set(data[11])
            self.var_radio1.set(data[12])
          else:
           messagebox.showerror("Error", "No data found for this entry.")    
           
           
          #update function
    def update_data(self):
     if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All Fields are required!!", parent=self.root)
     else:
        try:
            Update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if Update>0:
                conn=mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
                my_cursor = conn.cursor()
                my_cursor.execute("update student set Department=%s, Semester=%s,Student_Name=%s, Roll_No=%s, Date_of_Birth=%s, Address=%s, Phone=%s, Gender=%s, Email=%s,Teacher_Name=%s,Teacher_Subject=%s,PhotoSample=%s where Student_id=%s",(
    
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_tec_name.get(),
                    self.var_tec_sub.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                ))
                
            else:
                if not Update:
                    return
            messagebox.showinfo("Success","Student details successfully update completed!",parent=self.root)    
            conn.commit()
            self.fetch_data()
            conn.close()      
            
        except Exception as es:
            messagebox.showerror("Error",f"Due To: {str(es)}", parent=self.root)
            
            #delete function
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
                    my_cursor = conn.cursor() 
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                       return
                   
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details!",parent=self.root)
                      
            except Exception as es:
                messagebox.showerror("Error",f"Due To: {str(es)}", parent=self.root)
                
                
         #Reset function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")    
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_dob.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_gender.set("Select Gender")
        self.var_email.set("")
        self.var_tec_name.set("")
        self.var_tec_sub.set("")
        self.var_radio1.set("")
        
        
    def search_data(self):
    # Validate search inputs
        if not self.var_com_search.get() or not self.var_search.get():
            messagebox.showerror("Error", "Please select search options")
            return

        # Sanitize the input by stripping spaces and unwanted characters
        search_column_raw = self.var_com_search.get().strip().replace(":", "")

       
        # Mapping user-friendly search options to actual column names
        column_mapping = {
            "Student ID": "Student_id",
            "Student Name": "Student_Name",
            "Department": "Department",
            "Semester": "Semester",
            "Roll No": "Roll_No",
            "Date of Birth": "Date_of_Birth",
            "Address": "Address",
            "Phone": "Phone",
            "Gender": "Gender",
            "Email": "Email",
            "Teacher Name": "Teacher_Name",
            "Teacher Subject": "Teacher_Subject"
        }

        search_column = column_mapping.get(search_column_raw)

        # If the search column is invalid, display error
        if not search_column:
            messagebox.showerror("Error", "Invalid search column")
            return


        try:
            conn = mysql.connector.connect(
                host="localhost", 
                username="root", 
                password="admin@2309", 
                database="face_recognizer"
            )
            my_cursor = conn.cursor()

            # Special case for 'Phone', as it's a numeric field and needs to be cast to a string
            if search_column == "Phone":
                query = f"SELECT * FROM student WHERE CAST({search_column} AS CHAR) LIKE %s"
            else:
                query = f"SELECT * FROM student WHERE {search_column} LIKE %s"

            search_value = f"%{self.var_search.get()}%"


            my_cursor.execute(query, (search_value,))
            rows = my_cursor.fetchall()

            if rows:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No data found")
         

            conn.commit()

        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

        finally:
            conn.close()

            
        
        
        
      
#Generate Data Set take a photo Sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
                my_cursor = conn.cursor() 
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                
                my_cursor.execute("update student set Department=%s, Semester=%s, Student_Name=%s, Roll_No=%s, Date_of_Birth=%s, Address=%s, Phone=%s, Gender=%s, Email=%s, Teacher_Name=%s, Teacher_Subject=%s, PhotoSample=%s where Student_id=%s""",
                (
                    self.var_dep.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_roll.get(),
                    self.var_dob.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_tec_name.get(),
                    self.var_tec_sub.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                )
            )
            
                conn.commit()
                self.fetch_data()
                self.reset_data()
            except Exception as e:
                messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)
            finally:
                conn.close()
            #load prededefined data on face frontals from opencv
            
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            def face_cropped(img):
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=face_classifier.detectMultiScale(gray,1.3,5)
                # scaling factor =1.3
                #minimum neighbour =5
                
                for(x,y,w,h) in faces:
                    face_cropped=img[y:y+h,x:x+w]
                    return face_cropped
                
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
            messagebox.showinfo("Result","Generating data sets completed!!!")    
            
        
                #creating objects

if __name__ == "__main__":
          root = Tk()
          obj = Student(root)
          root.mainloop()
