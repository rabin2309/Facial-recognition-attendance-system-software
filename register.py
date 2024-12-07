from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import Button
from tkinter import messagebox
import mysql.connector
import re #regular expression

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")
        
        #variables
        
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_q=StringVar()
        self.var_security_a=StringVar()
        self.var_password=StringVar()
        self.var_confirm_password=StringVar()
        
        
        #bg img
        img_down = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\bg2.jpg")
        img_down = img_down.resize((1530, 710), Image.LANCZOS)
        self.photoimg_down = ImageTk.PhotoImage(img_down)

        bg_img_down = Label(self.root, image=self.photoimg_down)
        bg_img_down.place(x=0, y=0, width=1530, height=790)
            
        
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)
        
        register_lbl=Label(frame,text="Register Here",font=("georgia", 25, "bold"), bg="white", fg="maroon")
        register_lbl.place(x=20,y=20)

        
        #label and entry
        fname=Label(frame,text="First Name:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("courier",15,"bold"))
        fname_entry.place(x=50, y=130,width=250)
        
        #bind and validation register
        validate_name=self.root.register(self.checkname)
        fname_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        
        l_name=Label(frame,text="Last Name:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        l_name.place(x=370,y=100)
        
        lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("courier",15,"bold"))
        lname_entry.place(x=370,y=130,width=250)
        
    
        #callback and validation register
        validate_name=self.root.register(self.checkname)
        lname_entry.config(validate='key',validatecommand=(validate_name,'%P'))
        
        
        contact=Label(frame,text="Contact:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        contact.place(x=50,y=170)
        
        entry_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("courier",15,"bold"))
        entry_contact.place(x=50,y=200,width=250)
        
        #callback and validation register
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
        
        
        email_lbl=Label(frame,text="E-mail:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        email_lbl.place(x=370,y=170)
        
        txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("courier",15,"bold"))
        txt_email.place(x=370,y=200,width=250)
        
        
        security_q=Label(frame,text="Select Security Questions:",font=("georgia",13,"bold"),bg="white",fg="blue")
        security_q.place(x=50,y=240)
        
        self_combo_security_q=ttk.Combobox(frame,textvariable=self.var_security_q,font=("courier",12,"bold"),state="readonly")
        self_combo_security_q["values"]=("Select","Your Birth Place?","Your Favourite dishes?","Your Favourite Languages?")
        self_combo_security_q.place(x=50,y=270,width=250)
        self_combo_security_q.current(0)
        
        security_a=Label(frame,text="Security Answer:",font=("georgia", 15, "bold"),bg="white",fg="blue")
        security_a.place(x=370,y=240)
        
        self.txt_security=ttk.Entry(frame,textvariable=self.var_security_a,font=("georgia",13,"bold"))
        self.txt_security.place(x=370,y=270,width=250)
        
        password=Label(frame,text="Password:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        password.place(x=50,y=310)
        
        self.txt_password=ttk.Entry(frame,textvariable=self.var_password,font=("courier",15,"bold"))
        self.txt_password.place(x=50,y=340,width=250)
        
        
        confirm_password=Label(frame,text="Confirm Password:",font=("georgia", 15, "bold"), bg="white", fg="blue")
        confirm_password.place(x=370,y=310)
        
        self.txt_confirm_password=ttk.Entry(frame,textvariable=self.var_confirm_password,font=("courier",15,"bold"))
        self.txt_confirm_password.place(x=370,y=340,width=250)
        
        
        #check button
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("courier",12,"bold"),bg="white", fg="blue",onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=390)
        
        #button
        img=Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\register1.jpg")
        img=img.resize((200,80),Image.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=0,y=420,width=200)
        
        
        
        img_login=Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\loginn.jpg")
        img_login=img_login.resize((200,80),Image.LANCZOS)
        self.photoimage_login=ImageTk.PhotoImage(img_login)
        b1=Button(frame,image=self.photoimage_login,command=self.return_login,borderwidth=0,cursor="hand2")
        b1.place(x=330,y=420,width=200)
        
     
     
     
   # def combined_function(self,*args):
  #      self.register_data()
   #     self.validation()    
#function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_security_q.get()=="":
            messagebox.showerror("Error","All fields are required!!")
        
        elif self.var_password.get()!=self.var_confirm_password.get():
            messagebox.showerror("Error","Password and Confirm Password must be same!!")
            
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms & conditions!!")    
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already Exist. Please try another email address.")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                    
                    
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_q.get(),
                    self.var_security_a.get(),
                    self.var_password.get()
                   
                       
                ))
       
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully!!")
       
    
    
   
    #validation for fname and last name
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=='':
            return True
        else:
            messagebox.showerror("Invalid",'Not Allowed'+name[-1])
            
     #check contact validation
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showerror("Invalid","Invalid entry")
            return False   
     
     
      #check password validation
    def checkpassword(self,password):
        if len(password)<=21:
            if re.match("^(?=.*[0=9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True
            else:
                messagebox.showinfo("invalid","Enter Valid Password(Example:rabin@5432#)")
                return False
        else:
            messagebox.showerror("Invalid","Minimum 6 character required")
            return False
        
        
      #check password validation
    def checkemail(self,email):
        if len(email)>7:
            if re.match(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", email):

                return True
            else:
                messagebox.showwarning("Alert","Invalid email Please enter Valid emailaddress(Example:rabinbhattarai44@gmail.com)")
                return False
        else:
            messagebox.showinfo("Invalid","Email length is too small please enter a valid email address")
            return False 
        
        
            
    #validation
   # def validation(self):
        #if self.var_fname.get()=="":
         #   messagebox.showerror("error","Plese enter your firstname",parent=self.root)
            
        #elif self.var_lname.get()=="":
         #   messagebox.showerror("error","Plese enter your lastname",parent=self.root)
        
        #if self.var_contact.get()=="":
        #    messagebox.showerror("error","Plese enter your contact number",parent=self.root)
        
       # elif self.var_email.get()=="":
          # messagebox.showerror("error","Plese enter your email",parent=self.root)
                                
        #elif self.var_security_q.get()=="":
         #   messagebox.showerror("error","select enter your security question",parent=self.root)
                
        #elif self.var_security_a.get()=="":
         #   messagebox.showerror("error","Plese enter your security answer",parent=self.root)
        
        #elif self.var_password.get()=="":
         #  messagebox.showerror("error","Plese enter your password",parent=self.root)
                
        #elif self.var_confirm_password.get()=="":
         #   messagebox.showerror("error","Plese enter your password again",parent=self.root)
                                
    def return_login(self):
        self.root.destroy()
    

    
       
       
        #creating objects

if __name__ == "__main__":
          root = Tk()
          obj = Register(root)
          root.mainloop()
        