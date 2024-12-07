from tkinter import *
from PIL import Image, ImageTk


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")

        # Title Label
        title_lbl = Label(
            self.root,
            text="H E L P   D E S K",
            font=("Roboto", 38, "bold"),  # Increased font size for better visibility
            bg="#e6f7ff",  # A vibrant blue background
            fg="#003366",  # White text for high contrast
            relief="raised",  # Slight 3D effect
            bd=3,  # Thicker border for emphasis
            padx=10,  # Add horizontal padding for a spacious look
            pady=5  # Add vertical padding for balance
        )
        title_lbl.place(x=0, y=0, width=1530, height=60)  # Increased height for a prominent display


        # First Image
        img_top = Image.open(r"C:\Users\HP\Desktop\facial_recognition system\college_images\help.png")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=720)

       # Contact Frame
        contact_frame = Frame(f_lbl, bg="#f7f7f7", bd=3, relief="ridge")
        contact_frame.place(x=500, y=590, width=450, height=120)

        # Contact Frame Title
        contact_title = Label(
            contact_frame,
            text="Contact Information",
            font=("Roboto", 18, "bold"),
            bg="#003366",
            fg="white",
            anchor="center"
        )
        contact_title.pack(fill="x")  # Stretch title across the frame

        # First Email
        contact_label_1 = Label(
            contact_frame,
            text="📧 rabinbhattarai44@gmail.com",
            font=("Roboto", 16, "bold"),
            bg="#e6f7ff",  # Light blue background for a clean, fresh look
            fg="#003366",  # Deep blue text for excellent contrast
            anchor="w",
            padx=10  # Add left padding for spacing
        )
        contact_label_1.pack(fill="x", pady=5)

        # Second Email
        contact_label_2 = Label(
            contact_frame,
            text="📧 arjunrawal67890@gmail.com",
            font=("Roboto", 16, "bold"),
            bg="#e6f7ff",  # Light blue background for a clean, fresh look
            fg="#003366",  # Deep blue text for excellent contrast
            anchor="w",
            padx=10  # Add left padding for spacing
        )
        contact_label_2.pack(fill="x", pady=5)


        # Back Button
        back_btn = Button(
            self.root,
            text="⬅ Back",
            font=("Courier", 20, "bold"),
            fg="white",
            bg="#0047ab",
            activebackground="#003366",
            activeforeground="white",
            command=self.back_to_main,
            relief="raised",
            bd=3,
            cursor="hand2"
        )
        back_btn.place(x=0, y=5,width=120, height=50)

    def animate_title(self):
        # Scroll text for animation
        self.scrolling_text = self.scrolling_text[1:] + self.scrolling_text[0]
        self.title_lbl.config(text=self.scrolling_text)
        self.root.after(200, self.animate_title)

    def back_to_main(self):
        self.root.destroy()  # Close the Help window and return to the main window


# Create Application
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
