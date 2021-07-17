
from tkinter import*
from PIL import Image,ImageTk     #pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime

import mysql.connector
from tkinter import messagebox

class Roombooking:
    def __init__(self,root):
      self.root=root  
      self.root.title("Hotel Management System")
      self.root.geometry("1130x480+230+220")

    #======================= Variable ==================
      self.var_contact=StringVar()
      self.var_checkindate=StringVar()
      self.var_checkoutdate=StringVar()
      self.var_roomtype=StringVar()
      self.var_roomavailable=StringVar()
      self.var_meal=StringVar()
      self.var_noofdays=StringVar()
      self.var_paidtax=StringVar()
      self.var_actualtotal=StringVar()
      self.var_total=StringVar()
      



    # ==============title===================================================================================================

      lbl_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1130,height=50)

    # ==================logo==========================

      img2=Image.open(r"E:\hms\logo1.jpg")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=40)

      #=============label frame=============
      labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",fg="red",font=("times new roman",15,"bold"),padx=2)
      labelframeleft.place(x=5,y=50,width=425,height=420)

       #=================label and entry=====================
      #customer contact
      lbl_cust_contact=Label(labelframeleft,text="Customer contact",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lbl_cust_contact.grid(row=0,column=0,sticky=W)

      enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",10,"bold"))
      enty_contact.grid(row=0,column=1,sticky=W)
      validate_contact=self.root.register(self.checkcontact)
      enty_contact.config(validate='key',validatecommand=(validate_contact,'%P'))
      # fetch data button
      btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="gold",width=8)
      btnFetchData.place(x=270,y=4)
  
       #check in date
      check_in_date=Label(labelframeleft,text="check_in_date",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      check_in_date.grid(row=1,column=0,sticky=W)

      txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkindate,width=29,font=("arial",10,"bold"))
      txtcheck_in_date.grid(row=1,column=1)


      
      #check_out_date
      lbl_check_out=Label(labelframeleft,text="Check_out Date",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lbl_check_out.grid(row=2,column=0,sticky=W)

      txt_check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkoutdate,width=29,font=("arial",10,"bold"))
      txt_check_out.grid(row=2,column=1)

      #Room_type
      label_Room_type=Label(labelframeleft,text="Room Type",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      label_Room_type.grid(row=3,column=0,sticky=W)
      conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
      my_cursor=conn.cursor()
      my_cursor.execute("select RoomType from details")
      Ide=my_cursor.fetchall()
      combo_Room_type=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",10,"bold"),width=27,state="readonly")
      combo_Room_type["value"]=Ide
      combo_Room_type.current(0)
      combo_Room_type.grid(row=3,column=1)


      #RoomAvailable
      lblRoomAvailable=Label(labelframeleft,text="Available Room",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblRoomAvailable.grid(row=4,column=0,sticky=W)

      #txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",10,"bold"))
      #txtRoomAvailable.grid(row=4,column=1)
      conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
      my_cursor=conn.cursor()
      my_cursor.execute("select RoomNo from details")
      rows=my_cursor.fetchall()
      combo_Room_type=ttk.Combobox(labelframeleft,textvariable=self.var_roomavailable,font=("arial",10,"bold"),width=27,state="readonly")
      combo_Room_type["value"]=rows
      combo_Room_type.current(0)
      combo_Room_type.grid(row=4,column=1)
      #Meal
      lblMeal=Label(labelframeleft,text="Meal",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblMeal.grid(row=5,column=0,sticky=W)

      txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",10,"bold"))
      txtMeal.grid(row=5,column=1)

      #No Of Days
      lblNoOfDays=Label(labelframeleft,text="No Of Days",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblNoOfDays.grid(row=6,column=0,sticky=W)

      txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",10,"bold"))
      txtNoOfDays.grid(row=6,column=1)

      #Paid tax
      lblNoOfDays=Label(labelframeleft,text="Paid Tax",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblNoOfDays.grid(row=7,column=0,sticky=W)
      txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",10,"bold"))
      txtNoOfDays.grid(row=7,column=1)

      


      # Sub Total
      lblNoOfDays=Label(labelframeleft,text="Sub Total",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblNoOfDays.grid(row=8,column=0,sticky=W)

      txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",10,"bold"))
      txtNoOfDays.grid(row=8,column=1)


      # Total Cost
      lblNoOfDays=Label(labelframeleft,text="Total Cost",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblNoOfDays.grid(row=9,column=0,sticky=W)

      txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",10,"bold"))
      txtNoOfDays.grid(row=9,column=1)

       #===========Bill Button++=========================
     
      btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnBill.grid(row=10,column=0,padx=1,sticky=W)


 #=================Button==================

      btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
      btn_frame.place(x=0,y=360,width=412,height=33)

      btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnAdd.grid(row=0,column=0,padx=1)

      btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnUpdate.grid(row=0,column=1,padx=1)

      btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnDelete.grid(row=0,column=2,padx=1)

      btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",10,"bold"),bg="black",fg="gold",width=12)
      btnReset.grid(row=0,column=3,padx=1)


      #===============right side image====================
      img3=Image.open(r"E:\hms\bed.jpg")
      img3=img3.resize((420,250),Image.ANTIALIAS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
      lblimg.place(x=700,y=55,width=420,height=250)



#=====================Table frame search system=======================

      Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View And Search Details",fg="red",font=("times new roman",15,"bold"),padx=2)
      Table_Frame.place(x=435,y=280,width=690,height=260)

      lblSearchBy=Label(Table_Frame,text="Search By",bg="black",fg="gold",font=("arial",10,"bold"))
      lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

      self.search_var=StringVar()
      combo_Search=ttk.Combobox(Table_Frame,font=("arial",10,"bold"),width=22,state="readonly")
      combo_Search["value"]=("contact","Room",)
      combo_Search.current(0)
      combo_Search.grid(row=0,column=1)

      txtSearch=ttk.Entry(Table_Frame,width=22,font=("arial",10,"bold"))
      txtSearch.grid(row=0,column=2,padx=2)

      self.txt_search=StringVar()
      btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnSearch.grid(row=0,column=3,padx=1)

      btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=12)
      btnShowAll.grid(row=0,column=4,padx=1)

   #=================== show data table================= 

      details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
      details_table.place(x=0,y=50,width=670,height=120)

      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

      self.room_table=ttk.Treeview(details_table,column=("contact","checkinDate","checkoutDate","roomtype","roomavailable","meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.room_table.xview)
      scroll_y.config(command=self.room_table.yview)

      self.room_table.heading("contact",text="Contact")
      self.room_table.heading("checkinDate",text="CheckinDate")
      self.room_table.heading("checkoutDate",text="CheckoutDate")
      self.room_table.heading("roomtype",text="Roomtype")
      self.room_table.heading("roomavailable",text="Roomavailable")
      self.room_table.heading("meal",text="Meal")
      self.room_table.heading("noofdays",text="Noofdays")
     
      self.room_table["show"]="headings"

      self.room_table.column("contact",width=100)
      self.room_table.column("checkinDate",width=100)
      self.room_table.column("checkoutDate",width=100)
      self.room_table.column("roomtype",width=100)
      self.room_table.column("roomavailable",width=100)
      self.room_table.column("meal",width=100)
      self.room_table.column("noofdays",width=100)
      self.room_table.pack(fill=BOTH,expand=1)

      self.room_table.bind("<ButtonRelease-1>",self.get_cuersor)

      self.fetch_data()
#add data
    def add_data(self):

        if self.var_contact.get()=="" or self.var_checkindate.get()=="":

          messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
          try:                      
              conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                                                          self.var_contact.get(),
                                                          self.var_checkindate.get(),
                                                          self.var_checkoutdate.get(),
                                                          self.var_roomtype.get(),
                                                          self.var_roomavailable.get(),
                                                          self.var_meal.get(),
                                                          self.var_noofdays.get()                                                                             
                                                                               ))                                                                             
              conn.commit()
              self.fetch_data()
              conn.close()                                                                
              messagebox.showinfo("sucess","Your Room Booked",parent=self.root)
          except Exception as es:
            messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
#fethch data
    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from room")
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

            self.var_contact.set(row[0])
            self.var_checkindate.set(row[1])
            self.var_checkoutdate.set(row[2])
            self.var_roomtype.set(row[3])
            self.var_roomavailable.set(row[4])
            self.var_meal.set(row[5])
            self.var_noofdays.set(row[6])

    def update(self):
      if self.var_contact.get()=="":
          messagebox.showerror("Error","Please enter mobile number",parent=self.root)
      else:
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                                                                                                                                                                  
                                                                                                                                    self.var_checkindate.get(),
                                                                                                                                    self.var_checkoutdate.get(),
                                                                                                                                    self.var_roomtype.get(),
                                                                                                                                    self.var_roomavailable.get(),
                                                                                                                                    self.var_meal.get(),
                                                                                                                                    self.var_noofdays.get(),
                                                                                                                                    self.var_contact.get()
                                                                                                                                                                  
                                                                                                                                    ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Update","Room Details has been Updated successfully",parent=self.root)

    def mDelete(self):
      mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this Person",parent=self.root)
      if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          query="delete from room where contact=%s"
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
      else:
          if not mDelete:
            return
            
      conn.commit()
      self.fetch_data()
      conn.close()

    def reset(self):
         self.var_contact.set("")
         self.var_checkindate.set("")
         self.var_checkoutdate.set("")
         self.var_roomtype.set("")
         self.var_roomavailable.set("")
         self.var_meal.set("")
         self.var_noofdays.set("")
         self.var_paidtax.set("")
         self.var_actualtotal.set("")
         self.var_total.set("")

         

#===================All data Fetch===========================

    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=250,height=180)

                lblNmae=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblNmae.place(x=0,y=0)

                lb1=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb1.place(x=90,y=0)
                 #============gender======

                conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb2.place(x=90,y=30)

                #=============email=========
                conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)

                lb3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb3.place(x=90,y=60)

                #=========nationality===============
                conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblNationality.place(x=0,y=90)

                lb4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb4.place(x=90,y=90)

                #============Address+=====================
                conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=90)

                lb5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lb5.place(x=90,y=90)

#search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
                conn.commit()
        conn.close()


    def total(self):
      inDate=self.var_checkindate.get()
      outDate=self.var_checkoutdate.get()
      inDate=datetime.strptime(inDate,"%d/%m/%Y")       
      outDate=datetime.strptime(outDate,"%d/%m/%Y")    
      self.var_noofdays.set(abs(outDate-inDate).days) 

      if(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Laxary"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
      
                      
      elif(self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)
        
      elif(self.var_meal.get()=="BreakFast" and self.var_roomtype.get()=="Duplex"):
        q1=float(500)
        q2=float(1000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        Tax="Rs."+str("%.2f"%((q5)*0.09))
        ST="Rs."+str("%.2f"%((q5)))
        TT="Rs."+str("%.2f"%(q5+((q5)*0.9)))
        self.var_paidtax.set(Tax)
        self.var_actualtotal.set(ST)
        self.var_total.set(TT)

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
 obj=Roombooking(root)
 root.mainloop()