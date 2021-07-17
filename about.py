from tkinter import*
from PIL import Image,ImageTk     #pip install pillow
from tkinter import ttk
import random
from datetime import datetime
from time import strftime
import mysql.connector
from tkinter import messagebox


class about:
    def __init__(self,root):
      self.root=root  
      self.root.title("Hotel Management System")
      self.root.geometry("1550x800+0+0")


      img1=Image.open(r"E:\hms\about.jpg")
      img1=img1.resize((900,1200),Image.ANTIALIAS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
      lblimg.place(x=0,y=0,width=1400,height=1100)

if __name__ == "__main__":
 root=Tk()
 obj=about(root)
 root.mainloop()