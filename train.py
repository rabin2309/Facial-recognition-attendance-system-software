from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Facial Recognition System")
        
        # Title Label
        title_lbl = Label(
            self.root,
            text="🚀 T R A I N   D A T A   S E T 🚀",
            font=("Georgia", 38, "bold"),  # Slightly larger font for better visibility
            bg="#e6f7ff",  # Light blue background for a clean, fresh look
            fg="#003366",  # Deep blue text for excellent contrast
            relief="ridge",  # Adds a subtle border for emphasis
            bd=3,  # Border width to make the label stand out
            padx=10,  # Adds padding for a spacious appearance
            pady=5  # Adds padding for a balanced look
        )
        title_lbl.place(x=0, y=0, width=1530, height=60)  # Increased height for better spacing

        
        # Top Image
        img_top = Image.open(r"college_images/train1.png")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
       
       # Train Button
        b1_1 = Button(
            self.root,
            text="📊 TRAIN DATA",
            command=self.train_classifier,
            cursor="hand2",
            font=("Roboto", 30, "bold"),  # Retain the bold font for emphasis
            bg="green",  # Vibrant green (Bootstrap success green)
            fg="white",  # White text for contrast
            activebackground="#218838",  # Darker green for hover effect
            activeforeground="white",  # Keep text white on hover
            relief="raised",  # Slight 3D effect
            bd=3  # Slightly thicker border for better definition
        )
        b1_1.place(x=600, y=380, width=320, height=60)  # Adjusted size and position for better balance

       
        # Bottom Image
        img_bottom = Image.open(r"college_images/train4.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)
        
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
        back_btn.place(x=0, y=5, width=120, height=50)  # Adjusted position and size for better alignment


    def back_to_main(self):
        # Close the current window
        self.root.destroy()

    def train_classifier(self):
        # Directory containing training data
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith('.jpg')]

        if not path:
            messagebox.showerror("Error", "No training data found in 'data' folder!")
            return

        faces = []
        ids = []

        # Process each image in the folder
        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from filename
                faces.append(imageNp)
                ids.append(id)
            except Exception as e:
                print(f"Error processing image {image}: {e}")
                continue

        if not faces:
            messagebox.showerror("Error", "No valid images found for training!")
            return

        ids = np.array(ids)

        # Train the LBPH Face Recognizer
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)

        # Calculate training accuracy
        correct_predictions = 0
        for face, actual_id in zip(faces, ids):
            predicted_id, confidence = clf.predict(face)
            if predicted_id == actual_id:
                correct_predictions += 1

        accuracy = (correct_predictions / len(ids)) * 100

        # Save the trained model
        if os.path.exists("classifier.xml"):
            if not messagebox.askyesno("Overwrite?", "Classifier already exists. Overwrite?"):
                return
        clf.write("classifier.xml")

        # Show success message with accuracy
        messagebox.showinfo("Result", f"Training completed successfully!\nAccuracy: {accuracy:.2f}%")

# Run the application
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()