from tkinter import*
from PIL import Image,ImageTk     #pip install pillow
from tkinter import ttk
import random
from datetime import datetime
from time import strftime
import mysql.connector
from tkinter import messagebox

class Detailsroom:
    def __init__(self,root):
      self.root=root  
      self.root.title("Hotel Management System")
      self.root.geometry("1130x480+230+220")

    # ==============title===================================================================================================

      lbl_title=Label(self.root,text="ROOM ADD ",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1130,height=50)

    # ==================logo==========================

      img2=Image.open(r"E:\hms\logo1.jpg")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=40)

      #=============label frame=============
      labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",fg="red",font=("times new roman",15,"bold"),padx=2)
      labelframeleft.place(x=5,y=50,width=520,height=350)

#      floor

      lbl_floor=Label(labelframeleft,text="Floor",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lbl_floor.grid(row=0,column=0,sticky=W)
      self.var_floor=StringVar()
      enty_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,width=20,font=("arial",10,"bold"))
      enty_floor.grid(row=0,column=1,sticky=W)
      validate_contact=self.root.register(self.checkcontact)
      enty_floor.config(validate='key',validatecommand=(validate_contact,'%P'))
#      RoomNo

      lb1_RoomNo=Label(labelframeleft,text="Room No",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lb1_RoomNo.grid(row=1,column=0,sticky=W)
      self.var_roomno=StringVar()
      enty_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomno,width=20,font=("arial",10,"bold"))
      enty_RoomNo.grid(row=1,column=1,sticky=W)
      validate_contact=self.root.register(self.checkcontact)
      enty_RoomNo.config(validate='key',validatecommand=(validate_contact,'%P'))
#      RoomType

      lbl_RoomType=Label(labelframeleft,text="Room Type",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lbl_RoomType.grid(row=2,column=0,sticky=W)
      self.var_RoomType=StringVar()
      enty_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",10,"bold"))
      enty_RoomType.grid(row=2,column=1,sticky=W)

#=================Button==================

      btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
      btn_frame.place(x=0,y=200,width=412,height=33)

      btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnAdd.grid(row=0,column=0,padx=1)

      btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnUpdate.grid(row=0,column=1,padx=1)

      btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnDelete.grid(row=0,column=2,padx=1)

      btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=12)
      btnReset.grid(row=0,column=3,padx=1)

#=====================Table frame search system=======================

      Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",fg="red",font=("times new roman",15,"bold"),padx=2)
      Table_Frame.place(x=600,y=55,width=500,height=350)

# show data

      scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

      self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.room_table.xview)
      scroll_y.config(command=self.room_table.yview)

      self.room_table.heading("floor",text="Floor")
      self.room_table.heading("roomno",text="Room No")
      self.room_table.heading("roomtype",text="Roomtype")
    
     
      self.room_table["show"]="headings"

      self.room_table.column("floor",width=100)
      self.room_table.column("roomno",width=100)
      self.room_table.column("roomtype",width=100)
      self.room_table.pack(fill=BOTH,expand=1)
      self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)
      self.fetch_data()
#add data
    def add_data(self):

        if self.var_floor.get()=="" or self.var_RoomType.get()=="":

          messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
          try:                      
              conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                              self.var_floor.get(),
                                                                              self.var_roomno.get(),
                                                                              self.var_RoomType.get()  

                                                                            ))                                                                             
              conn.commit()
              #self.fetch_data()
              conn.close()                                                                
              messagebox.showinfo("sucess","New Room Added successfully",parent=self.root)
          except Exception as es:
            messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from details")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
              self.room_table.delete(*self.room_table.get_children())            
              for i in rows:
               self.room_table.insert("",END,values=i)
              conn.commit()
          conn.close()
# getcuersor
    def get_cuersor(self, event=""):
            cusrsor_row=self.room_table.focus()
            content=self.room_table.item(cusrsor_row)
            row=content["values"]

            self.var_floor.set(row[0])
            self.var_roomno.set(row[1])
            self.var_RoomType.set(row[2])

    def update(self):
      if self.var_floor.get()=="":
          messagebox.showerror("Error","Please enter Floor number",parent=self.root)
      else:
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                                                                                                                                                                  
                                                                                                                                   
                                                                                  self.var_floor.get(),
                                                                                  self.var_RoomType.get(),
                                                                                  self.var_roomno.get()
                                                                                  ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Update","New Room Details has been Updated successfully",parent=self.root)          
   
    def mDelete(self):
      mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this Room",parent=self.root)
      if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          query="delete from details where RoomNo=%s"
          value=(self.var_roomno.get(),)
          my_cursor.execute(query,value)
      else:
          if not mDelete:
            return
            
      conn.commit()
      self.fetch_data()
      conn.close()

    def reset(self):
         self.var_floor.set("")
         self.var_RoomType.set("")
         self.var_roomno.set("")

    def checkcontact(self,contact):
      if contact.isdigit():
        return True
      if len(str(contact))==0:
        return True
      else:
        messagebox.showerror("Ivalid",'Invalid Entry',parent=self.root)
        return False
       

if __name__ == "__main__":
 root=Tk()
 obj=Detailsroom(root)
 root.mainloop()
