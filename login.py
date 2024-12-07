from tkinter import *
from tkinter import ttk, Button, Frame, messagebox, Toplevel
import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector
from main import Face_Recognition_System
from register import Register
import hashlib
import re
import pyttsx3

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
        



class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root2=root
        self.root.title("Login")
        self.root.geometry("600x700")
        #self.root.resizable(False, False)
        
        self.var_email=tk.StringVar()
        self.var_password = tk.StringVar()
        self.show_password = tk.IntVar(value=0)  # 0 means password is hidden
        
        
        
         # text to speech
        self.engine=pyttsx3.init()
        self.voices=self.engine.getProperty("voices")
        self.engine.setProperty("voice",self.voices[1].id)

        # Background Gradient Frame
        bg_frame = Frame(self.root, bg="#f0f8ff")
        bg_frame.place(x=0, y=0, width=600, height=600)

        # Login Frame
        login_frame = Frame(self.root, bg="white", highlightbackground="#3b5998", highlightthickness=3)
        login_frame.place(x=150, y=100, width=300, height=480)

        # Title
        title = Label(login_frame, text="Login", font=("roboto", 24, "bold"), bg="white", fg="#3b5998")
        title.pack(pady=20) 
        
        
        # Username Label and Entry
        username_label = Label(login_frame, text="Username", font=("Arial", 15), bg="white", fg="#555")
        username_label.pack(pady=10)
        self.username_entry = ttk.Entry(login_frame, textvariable=self.var_email, font=("Arial", 12))
        self.username_entry.pack(pady=5, ipadx=5, ipady=5)

        # Password Label and Entry
        password_label = Label(login_frame, text="Password", font=("Arial", 15), bg="white", fg="#555")
        password_label.pack(pady=10)
        self.password_entry = ttk.Entry(login_frame, textvariable=self.var_password, font=("Arial", 12), show="*")
        self.password_entry.pack(pady=5, ipadx=5, ipady=5) 
       
       
     
       
         # Eye Toggle Button for Password Visibility
        self.toggle_button = Button(login_frame, text="👁", command=self.toggle_password, bg="white", border=0)
        self.toggle_button.pack(pady=5)

        # Login Button
        login_btn = Button(login_frame, text="Login", command=self.login, font=("poppins", 15, "bold"), bg="#3b5998", fg="white", relief=FLAT, cursor="hand2")
        login_btn.pack(pady=20, ipadx=50, ipady=5)

        # Sign-Up Button
        register_btn = Button(login_frame, text="Sign Up", command=self.register_window, font=("roboto", 12), bg="white", fg="#3b5998", relief=FLAT, cursor="hand2")
        register_btn.pack()
    
      # Forgot Password Button
        forgot_btn = Button(login_frame, text="Forgot Password?", command=self.forgot_password_window, font=("roboto", 12), bg="white", fg="#3b5998", relief=FLAT, cursor="hand2")
        forgot_btn.pack(pady=10)



        
        #icon images
    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)    
        
    
    def show_message(self, title, message):
        messagebox.showerror(title, message)
    
    def toggle_password(self):
        if self.show_password.get() == 0:
            self.password_entry.config(show="")
            self.toggle_button.config(text="👁️")
            self.show_password.set(1)
        else:
            self.password_entry.config(show="*")
            self.toggle_button.config(text="🔒")
            self.show_password.set(0)

    def login(self):
        if self.var_email.get() == "" or self.var_password.get() == "":
            self.engine.say("Please enter both username and password.")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter both username and password.")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="admin@2309",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                # Optional: Hash the password if needed
                # hashed_password = self.hash_password(self.var_password.get())

                my_cursor.execute(
                    "SELECT * FROM register WHERE email=%s AND password=%s", (
                        self.var_email.get(),  # Use correct variables
                        self.var_password.get()  # Or hashed_password if hashing is needed
                    )
                )

                row = my_cursor.fetchone()
                if row is None:
                    self.engine.say("Invalid Username or Password")
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Invalid Username or Password")
                else:
                    
                    # Open the main page before TTS
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
                    
                   

                    user_name = row[1]  # Assuming the second column is the user's name
                    self.engine.say(f"Welcome,{user_name} ,to the Facial Recognition Attendance System.")
                    self.engine.runAndWait()
                    #messagebox.showinfo("Success", "Welcome!")
                    
                    # Destroy the login window after the new window is created
                    self.root.withdraw()  # Hide the login window (keep the app running)

                conn.close()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}")
    
    
    def forgot_password_window(self):
        email = self.var_email.get().strip()
        if email == "":
            self.engine.say("Please enter the email address to reset the password.")
            self.engine.runAndWait()
            messagebox.showerror("Error", "Please enter the email address to reset the password.")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="admin@2309", database="face_recognizer"
                )
                my_cursor = conn.cursor()
                query = "SELECT * FROM register WHERE email=%s"
                value = (email,)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                if row is None:
                    self.engine.say("Please enter a valid email address for reset the password.")
                    self.engine.runAndWait()
                    messagebox.showerror("Error", "Please enter a valid email address for reset the password.")
                else:
                    conn.close()

                    # Open the password reset window
                    self.root2 = Toplevel(self.root)
                    self.root2.title("Reset Password")
                    self.root2.geometry("400x500+550+150")
                    self.root2.config(bg="#f5f5f5")  # Soft gray background


                    

                    title = Label(
                        self.root2, 
                        text="Reset Your Password", 
                        font=("Helvetica", 18, "bold"), 
                         bg="white", fg="#3b5998"
                    )
                    title.pack(pady=20)

                    # Security Question
                    security_q = Label(
                        self.root2, 
                        text="Select Security Question:", 
                        font=("Arial", 15), 
                        fg="#333333", 
                        bg="#f5f5f5"
                    )
                    security_q.pack(pady=(10, 5))
                    self.combo_security_q = ttk.Combobox(
                        self.root2, font=("Arial", 12), state="readonly", width=30
                    )
                    self.combo_security_q["values"] = (
                        "Select", "Your Birth Place?", "Your Favourite dishes?", "Your Favorite Languages?"
                    )
                    self.combo_security_q.current(0)
                    self.combo_security_q.pack(pady=5)

                    # Security Answer
                    security_a = Label(
                        self.root2, 
                        text="Security Answer:", 
                        font=("Arial", 15), 
                        fg="#333333", 
                        bg="#f5f5f5"
                    )
                    security_a.pack(pady=(10, 5))
                    self.txt_security = ttk.Entry(self.root2, font=("Arial", 12), width=30)
                    self.txt_security.pack(pady=5)

                    # New Password
                    new_password = Label(
                        self.root2, 
                        text="New Password:", 
                        font=("Arial", 15), 
                        fg="#333333", 
                        bg="#f5f5f5"
                    )
                    new_password.pack(pady=(10, 5))
                    self.txt_new_password = ttk.Entry(
                        self.root2, font=("Arial", 12), show="*", width=30
                    )
                    self.txt_new_password.pack(pady=5)

                    # Show Password Checkbox
                    def toggle_password_visibility():
                        if self.txt_new_password.cget('show') == '*':
                            self.txt_new_password.config(show='')
                        else:
                            self.txt_new_password.config(show='*')

                    show_password = Checkbutton(
                        self.root2, 
                        text="Show Password", 
                        font=("Arial", 10), 
                        bg="#f5f5f5", 
                        command=toggle_password_visibility
                    )
                    show_password.pack(pady=5)

                    
                    
                    
                    
                    
                    # Reset Button
                    btn = Button(
                        self.root2, 
                        text="Reset Password", 
                        command=self.reset_pass, 
                        font=("poppins", 15, "bold"), 
                        fg="white", 
                        bg="#3b5998", 
                        activebackground="#218838", 
                        activeforeground="white"
                    )
                    btn.pack(pady=20)

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}")

# ReSet Password Function (unchanged)
    def reset_pass(self):
        if self.combo_security_q.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_new_password.get() == "":
            messagebox.showerror("Error", "Please enter the new password!", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="admin@2309", database="face_recognizer"
                )
                my_cursor = conn.cursor()
                
                # Clean the inputs by stripping spaces and normalizing to lowercase
                security_answer = self.txt_security.get().strip().lower()  # Trim and lower-case the answer
                security_question = self.combo_security_q.get().strip()  # Trim the question too
                email = self.var_email.get().strip()  # Trim the email
            
                
                query = "SELECT * FROM register WHERE email=%s AND security_q=%s AND security_a=%s"
                values = (self.var_email.get(), self.combo_security_q.get(), self.txt_security.get())
                print(f"Query: {query}")
                print(f"Values: {values}")
                my_cursor.execute(query, values)
                row = my_cursor.fetchone()

                if row is None:
                    print("Debug: No matching record found.")
                    messagebox.showerror("Error", "Incorrect security answer", parent=self.root2)
                else:
                    update_query = "UPDATE register SET password=%s WHERE email=%s"
                    update_values = (self.txt_new_password.get(), self.var_email.get())
                    my_cursor.execute(update_query, update_values)
                    conn.commit()
                    messagebox.showinfo("Success", "Password reset successfully. Please login with the new password.", parent=self.root2)
                    self.root2.destroy()

            except Exception as es:
                messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root2)
            finally:
                conn.close()

    

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1100x750+200+50")
        self.var_email = StringVar()
        self.var_password = StringVar()
          # Register the validate_contact_input function for validation
        self.validate_contact = root.register(self.validate_contact_input)
        # Variables for form fields
        self.var_contact = StringVar()

        # Text-to-Speech
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[1].id)

        # Variables for Form Fields
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_security_q = StringVar()
        self.var_security_a = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.show_password = IntVar(value=0)  # 0 means password is hidden
        self.show_confirm_password = IntVar(value=0)
        
        
        
        # Background Gradient Frame
        bg_frame = Frame(self.root, bg="#f0f8ff")
        bg_frame.place(x=200, y=100, width=750, height=550)

       
        # Main Frame for Form Fields (No background image, just a frame)
        frame = tk.Frame(self.root, bg="#f0f8ff", highlightbackground="#3b5998", highlightthickness=3)
        frame.place(x=200, y=100, width=750, height=550)

        register_lbl = tk.Label(frame, text="Register Here:", font=("Arial", 25, "bold"), bg="#f0f8ff", fg="#0047ab")
        register_lbl.place(x=20, y=20)

        # First Name
        fname = tk.Label(frame, text="First Name:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        fname.place(x=50, y=100)
        fname_entry = tk.Entry(frame, textvariable=self.var_fname, font=("Arial", 14), relief="flat")  # Use tk.Entry instead of ttk.Entry
        fname_entry.place(x=50, y=130, width=250, height=30)

        # Last Name
        l_name = tk.Label(frame, text="Last Name:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        l_name.place(x=370, y=100)
        lname_entry = tk.Entry(frame, textvariable=self.var_lname, font=("Arial", 14), relief="flat")  # Use tk.Entry instead of ttk.Entry
        lname_entry.place(x=370, y=130, width=250, height=30)

        # Contact
        contact = tk.Label(frame, text="Contact:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        contact.place(x=50, y=170)
        self.entry_contact = tk.Entry(frame, textvariable=self.var_contact, font=("Arial", 14), relief="flat", validate="key", validatecommand=(self.validate_contact, "%P"))  # Use tk.Entry instead of ttk.Entry
        self.entry_contact.place(x=50, y=200, width=250, height=30)
    
        # Email
        email_lbl = tk.Label(frame, text="E-mail:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        email_lbl.place(x=370, y=170)
        txt_email = tk.Entry(frame, textvariable=self.var_email, font=("Arial", 14), relief="flat")  # Use tk.Entry instead of ttk.Entry
        txt_email.place(x=370, y=200, width=250, height=30)

        # Security Question
        security_q = tk.Label(frame, text="Select Security Question:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        security_q.place(x=50, y=240)
        self_combo_security_q = ttk.Combobox(frame, textvariable=self.var_security_q, font=("Arial", 12), state="readonly", width=28)
        self_combo_security_q["values"] = ("Select", "Your Birth Place?", "Your Favourite dishes?", "Your Favourite Languages?")
        self_combo_security_q.place(x=50, y=270)
        self_combo_security_q.current(0)

        # Security Answer
        security_a = tk.Label(frame, text="Security Answer:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        security_a.place(x=370, y=240)
        self.txt_security = tk.Entry(frame, textvariable=self.var_security_a, font=("Arial", 14), relief="flat")  # Use tk.Entry instead of ttk.Entry
        self.txt_security.place(x=370, y=270, width=250, height=30)

        # Password
        password = tk.Label(frame, text="Password:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        password.place(x=50, y=310)
        self.txt_password = tk.Entry(frame, textvariable=self.var_password, font=("Arial", 14), show="*", relief="flat")  # Use tk.Entry instead of ttk.Entry
        self.txt_password.place(x=50, y=340, width=250, height=30)

        # Confirm Password
        confirm_password = tk.Label(frame, text="Confirm Password:", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
        confirm_password.place(x=370, y=310)
        self.txt_confirm_password = tk.Entry(frame, textvariable=self.var_confirm_password, font=("Arial", 14), show="*", relief="flat")  # Use tk.Entry instead of ttk.Entry
        self.txt_confirm_password.place(x=370, y=340, width=250, height=30)

        # Terms and Conditions Checkbox
        self.var_check = IntVar()
        checkbutton = tk.Checkbutton(frame, variable=self.var_check, text="I agree to the terms & conditions", font=("Arial", 12), bg="#f0f8ff", fg="#333", onvalue=1, offvalue=0)
        checkbutton.place(x=50, y=390)

        # Register Button
        b1 = tk.Button(frame, text="Register", command=self.register_data, font=("roboto", 14, "bold"), bg="#0047ab", fg="white", relief="flat", width=20, height=2)
        b1.place(x=50, y=440)

        # Login Button
        b2 = tk.Button(frame, text="Already have an account?", command=self.return_login, font=("roboto", 12, "bold"), bg="#f0f8ff", fg="#0047ab", relief="flat", width=20, height=2)
        b2.place(x=370, y=440)
        
        

    def register_data(self):
        try:
            # Ensure all fields are filled out
            if not all([self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), self.var_email.get(), self.var_security_q.get(), self.var_security_a.get(), self.var_password.get(), self.var_confirm_password.get()]):
                self.engine.say("All fields are required")
                self.engine.runAndWait()
                messagebox.showerror("Error", "All fields are required.")
                return

            # Email validation
            if not re.match(r"[^@]+@[^@]+\.[^@]+", self.var_email.get()):
                self.engine.say("Please enter a valid email address.")
                self.engine.runAndWait()

                messagebox.showerror("Error", "please enter a valid email address.")
                return


             # Contact Number Validation (Must be exactly 10 digits and numeric)
            contact_number = self.var_contact.get()
            if not contact_number.isdigit() or len(contact_number) != 10:
                self.engine.say("Please enter a valid 10-digit contact number.")
                self.engine.runAndWait()
                messagebox.showerror("Error", "Contact number must be a 10-digit number.")
                return
                
                
                
            # Password strength check (Example: At least 8 characters)
            if len(self.var_password.get()) < 8:
                self.engine.say("Password must be atleast 8  characters long.")
                self.engine.runAndWait() 

                messagebox.showerror("Error", "Password must be atleast 8 characters long.")
                return

            # Password and Confirm Password match check
            if self.var_password.get() != self.var_confirm_password.get():
                self.engine.say("Password do not match.")
                self.engine.runAndWait() 
                messagebox.showerror("Error", "Password do not match.")
                return

            # Terms and Conditions
            if not self.var_check.get():
                self.engine.say("You must agree to the terms & conditions.")
                self.engine.runAndWait()

                messagebox.showerror("Error", "You must agree to the terms & conditions.")
                return

            # If all checks pass, you can proceed to register the user (e.g., save to database)
            self.engine.say("Registration Successfully.")
            self.engine.runAndWait()

            messagebox.showinfo("Success", "Registration Successfully.")



                # Database connection and insertion


            conn = mysql.connector.connect(host="localhost", username="root", password="admin@2309", database="face_recognizer")
            my_cursor = conn.cursor()
            query = ("SELECT * FROM register WHERE email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            
            if row is not None:
                self.engine.say("User already exists. Please try another email address")
                self.engine.runAndWait()
                   # messagebox.showerror("Error", "User already exists. Please try another email address.")
                return
            else:
                my_cursor.execute("INSERT INTO register (fname, lname, contact, email, security_q, security_a, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_security_q.get(),
                    self.var_security_a.get(),
                    self.var_password.get()
                ))

            conn.commit()
            self.engine.say("Registered Successfully")
            self.engine.runAndWait()
               # messagebox.showinfo("Success", "Registered Successfully!")
            self.clear_form()
            self.root.destroy()  # Close the registration window after successful registration

        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Database Error: {str(err)}")

        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

        finally:
            if conn is not None and conn.is_connected():
                conn.close()
    
    
    def validate_contact_input(self, new_value):
        # Allow only digits and check length for 10 digits
        if new_value.isdigit() and len(new_value) <= 10:
            return True
        elif new_value == "":  # Empty string is allowed
            return True
        else:
            return False        
   


    def return_login(self):
        self.root.destroy()    


    def clear_form(self):
        self.var_fname.set("")
        self.var_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_security_q.set("")
        self.var_security_a.set("")
        self.var_password.set("")
        self.var_confirm_password.set("")
        self.var_check.set(0)
   
        
#creating objects

if __name__ == "__main__":
    main()