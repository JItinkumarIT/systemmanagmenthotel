from tkinter import*
from PIL import Image,ImageTk     #pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import re
class Cust_Win:
    def __init__(self,root):
      self.root=root  
      self.root.title("Hotel Management System")
      self.root.geometry("1130x480+230+220")

      #=========== variable======================
      self.var_ref=StringVar()
      x=random.randint(1000,9999)
      self.var_ref.set(str(x))

      self.var_cust_name=StringVar()
      self.var_father=StringVar()
      self.var_gender=StringVar()
      self.var_post=StringVar()
      self.var_mobile=StringVar()
      self.var_email=StringVar()
      self.var_nationality=StringVar()
      self.var_id_proof=StringVar()
      self.var_id_number=StringVar()
      self.var_address=StringVar()
       



      
         # ==============title============

      lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
      lbl_title.place(x=0,y=0,width=1130,height=50)

       # ==================logo==========================

      img2=Image.open(r"E:\hms\logo1.jpg")
      img2=img2.resize((100,40),Image.ANTIALIAS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
      lblimg.place(x=5,y=2,width=100,height=50)

      #=============label frame=============
      labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",fg="red",font=("times new roman",15,"bold"),padx=2)
      labelframeleft.place(x=5,y=50,width=425,height=420)

      #=================label and entry=====================
      #cust ref
      lbl_cust_ref=Label(labelframeleft,text="Customer Ref",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lbl_cust_ref.grid(row=0,column=0,sticky=W)

      enty_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref ,state="readonly",font=("arial",10,"bold"))
      enty_ref.grid(row=0,column=1)

      #cust name
      cname=Label(labelframeleft,text="Customer Name",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      cname.grid(row=1,column=0,sticky=W)

      txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial",10,"bold"))
      txtcname.grid(row=1,column=1)
      #bind and validation register
      validate_name=self.root.register(self.checkname)
      txtcname.config(validate='key',validatecommand=(validate_name,'%P'))

      btnFetchData=Button(labelframeleft,command=self.validation,text="Check",font=("arial",10,"bold"),bg="red",fg="lime",width=8)
      btnFetchData.place(x=330,y=320)


      
      #father name
      lblfname=Label(labelframeleft,text="Father Name",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblfname.grid(row=2,column=0,sticky=W,)

      txtfname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_father,font=("arial",10,"bold"))
      txtfname.grid(row=2,column=1)
      #bind and validation register
      validate_name=self.root.register(self.checkname)
      txtfname.config(validate='key',validatecommand=(validate_name,'%P'))
      #gender combox
      label_gender=Label(labelframeleft,text="Gender",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      label_gender.grid(row=3,column=0,sticky=W)

      combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",10,"bold"),width=27,state="readonly")
      combo_gender["value"]=("Male","Female","Other")
      combo_gender.current(0)
      combo_gender.grid(row=3,column=1)


      #postcode
      lblPostCode=Label(labelframeleft,text="PostCode",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblPostCode.grid(row=4,column=0,sticky=W)

      txtPostCode=ttk.Entry(labelframeleft,width=29,textvariable=self.var_post,font=("arial",10,"bold"))
      txtPostCode.grid(row=4,column=1)
      validate_contact=self.root.register(self.checkpost)
      txtPostCode.config(validate='key',validatecommand=(validate_contact,'%P'))
      #mobile number
      lblMobile=Label(labelframeleft,text="Mobile",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblMobile.grid(row=5,column=0,sticky=W)

      txtMobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial",10,"bold"))
      txtMobile.grid(row=5,column=1)

      validate_contact=self.root.register(self.checkcontact)
      txtMobile.config(validate='key',validatecommand=(validate_contact,'%P'))

      #email
      lblEmail=Label(labelframeleft,text="Email",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblEmail.grid(row=6,column=0,sticky=W)

      txtEmail=ttk.Entry(labelframeleft,width=29,textvariable=self.var_email,font=("arial",10,"bold"))
      txtEmail.grid(row=6,column=1)

      #nationality
      lblNationality=Label(labelframeleft,text="Nationality",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblNationality.grid(row=7,column=0,sticky=W)

      combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",10,"bold"),width=27,state="readonly")
      combo_Nationality["value"]=("Indian","American","Israel","british","Thailand","Europe","Other")
      combo_Nationality.current(0)
      combo_Nationality.grid(row=7,column=1)


      # id proof type combox
      lblIdProof=Label(labelframeleft,text="Id Proof Type",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblIdProof.grid(row=8,column=0,sticky=W)

      combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",10,"bold"),width=27,state="readonly")
      combo_id["value"]=("AdharCard","Pancard","draving Licence","Votercard","Other")
      combo_id.current(0)
      combo_id.grid(row=8,column=1)


      # id number
      lblIdNumber=Label(labelframeleft,text="Id Number",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblIdNumber.grid(row=9,column=0,sticky=W)

      txtIdNumber=ttk.Entry(labelframeleft,width=29,textvariable=self.var_id_number,font=("arial",10,"bold"))
      txtIdNumber.grid(row=9,column=1)

      # address
      lblAddress=Label(labelframeleft,text="Address",fg="green",font=("arial",10,"bold"),padx=2,pady=6)
      lblAddress.grid(row=10,column=0,sticky=W)

      txtAddress=ttk.Entry(labelframeleft,width=29,textvariable=self.var_address,font=("arial",10,"bold"))
      txtAddress.grid(row=10,column=1)

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

      









      #=====================Table frame and search system=======================

      Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View And Search Details",fg="red",font=("times new roman",15,"bold"),padx=2)
      Table_Frame.place(x=435,y=50,width=690,height=420)

      lblSearchBy=Label(Table_Frame,text="Search By",bg="black",fg="gold",font=("arial",10,"bold"))
      lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

      self.search_var=StringVar()
      combo_Search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",10,"bold"),width=22,state="readonly")
      combo_Search["value"]=("Name","Ref","Email")
      combo_Search.current(0)
      combo_Search.grid(row=0,column=1)

      self.txt_search=StringVar()
      txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=22,font=("arial",10,"bold"))
      txtSearch.grid(row=0,column=2,padx=2)

      btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",10,"bold"),bg="black",fg="gold",width=11)
      btnSearch.grid(row=0,column=3,padx=1)

      btnShowAll=Button(Table_Frame,text="Show All",command=self.fetch_data,font=("arial",10,"bold"),bg="black",fg="gold",width=12)
      btnShowAll.grid(row=0,column=4,padx=1)

      #=================== show data table=================

      details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
      details_table.place(x=0,y=50,width=670,height=300)

      scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

      self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","father","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.Cust_Details_Table.xview)
      scroll_y.config(command=self.Cust_Details_Table.yview)

      self.Cust_Details_Table.heading("ref",text="Refer No")
      self.Cust_Details_Table.heading("name",text="Name")
      self.Cust_Details_Table.heading("father",text="Father Name")
      self.Cust_Details_Table.heading("gender",text="Gender")
      self.Cust_Details_Table.heading("post",text="Post Code")
      self.Cust_Details_Table.heading("mobile",text="Mobile")
      self.Cust_Details_Table.heading("email",text="Email")
      self.Cust_Details_Table.heading("nationality",text="Nationality")
      self.Cust_Details_Table.heading("idproof",text="Id Proof")
      self.Cust_Details_Table.heading("idnumber",text="Id Number")
      self.Cust_Details_Table.heading("address",text="Address")

      self.Cust_Details_Table["show"]="headings"

      self.Cust_Details_Table.column("ref",width=100)
      self.Cust_Details_Table.column("name",width=100)
      self.Cust_Details_Table.column("father",width=100)
      self.Cust_Details_Table.column("gender",width=100)
      self.Cust_Details_Table.column("post",width=100)
      self.Cust_Details_Table.column("mobile",width=100)
      self.Cust_Details_Table.column("email",width=100)
      self.Cust_Details_Table.column("nationality",width=100)
      self.Cust_Details_Table.column("idproof",width=100)
      self.Cust_Details_Table.column("idnumber",width=100)
      self.Cust_Details_Table.column("address",width=100)
      self.Cust_Details_Table.pack(fill=BOTH,expand=1)
      self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cuersor)
      self.fetch_data()
#add data
    def add_data(self):

        if self.var_mobile.get()=="" or self.var_father.get()=="":

          messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
          try:                      
              conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                              self.var_ref.get(),
                                                                              self.var_cust_name.get(),
                                                                              self.var_father.get(),
                                                                              self.var_gender.get(),
                                                                              self.var_post.get(),
                                                                              self.var_mobile.get(),
                                                                              self.var_email.get(),
                                                                              self.var_nationality.get(),
                                                                              self.var_id_proof.get(),
                                                                              self.var_id_number.get(),
                                                                              self.var_address.get() 
                                                                                                  ))
              conn.commit()
              self.fetch_data()
              conn.close()                                                                
              messagebox.showinfo("sucess","customer has been added",parent=self.root)
          except Exception as es:
            messagebox.showwarning("warning",f"some thing went wrong:{str(es)}",parent=self.root)
           
    def fetch_data(self):
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          my_cursor.execute("select * from customer")
          rows=my_cursor.fetchall()
          if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())            
            for i in rows:
              self.Cust_Details_Table.insert("",END,values=i)
            conn.commit()
          conn.close()
                 
    def get_cuersor(self, event=""):
        cusrsor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cusrsor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_father.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])

    def update(self):
      if self.var_mobile.get()=="":
        messagebox.showerror("Error","Please enter mobile number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("update customer set Name=%s,Father=%s,Gender=%s,Post=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(
                                                                                                                                                                  
                                                                                                                                                                  self.var_cust_name.get(),
                                                                                                                                                                  self.var_father.get(),
                                                                                                                                                                  self.var_gender.get(),
                                                                                                                                                                  self.var_post.get(),
                                                                                                                                                                  self.var_mobile.get(),
                                                                                                                                                                  self.var_email.get(),
                                                                                                                                                                  self.var_nationality.get(),
                                                                                                                                                                  self.var_id_proof.get(),
                                                                                                                                                                  self.var_id_number.get(),
                                                                                                                                                                  self.var_address.get(),
                                                                                                                                                                  self.var_ref.get()
                                                                                                                                                                         ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","Customer Details has been Updated successfully",parent=self.root)    


    def mDelete(self):
      mDelete=messagebox.askyesno("Hotel Management System","Do you want delete this Person",parent=self.root)
      if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
          my_cursor=conn.cursor()
          query="delete from customer where Ref=%s"
          value=(self.var_ref.get(),)
          my_cursor.execute(query,value)
      else:
          if not mDelete:
            return
            
      conn.commit()
      self.fetch_data()
      conn.close()      
    
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_father.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")

        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="DOB10jun@123",database="management")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
                conn.commit()
                conn.close()
                  
    #Callback function
    def checkname(self,name):
      if name.isalpha():
        return True
      if name=='':
        return True
      else:
        messagebox.showerror('Invalid','Not Allowed '+name[-1],parent=self.root)
      return False   


      #check contact
    def checkcontact(self,contact):
      if contact.isdigit():
        return True
      if len(str(contact))==0:
        return True
      else:
        messagebox.showerror("Ivalid",'Invalid Entry',parent=self.root)
        return False


        #postcode
    def checkpost(self,post):
      if post.isdigit():
        return True
      if len(str(post))==0:
        return True
      else:
        messagebox.showerror("Ivalid",'Invalid Entry',parent=self.root)
        return False


        # check mail    
    def checkemail(self,email):
      if len(email)>7:
        if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
          return True
        else:
          messagebox.showwarning('Alert','Invalid email enter valid user email (example:Xyz12345@gmail.com)')
          return False
      else:
        messagebox.showinfo('Invaild','Email lenght is too smail')      


    #  validation
    def validation(self):
      if self.var_cust_name.get()=='':
        messagebox.showerror('Error','Please enter your Customer Name',parent=self.root)

      elif self.var_father.get()=='':
        messagebox.showerror('Error','Please enter your Father Name',parent=self.root)

      elif self.var_post.get()=='':
        messagebox.showerror('Error','Please enter your Post Code',parent=self.root)

      elif self.var_mobile.get()=='':
        messagebox.showerror('Error','Please enter your Contact Number',parent=self.root)

      elif self.var_email.get()=='':
        messagebox.showerror('Error','Please enter your Email id',parent=self.root)

      elif self.var_id_number.get()=='':
        messagebox.showerror('Error','Please enter your Id Number',parent=self.root)

      elif self.var_address.get()=='':
        messagebox.showerror('Error','Please enter your Address',parent=self.root)

      elif self.var_email.get()!=None:
        x=self.checkemail(self.var_email.get())
      if (x==True):
        messagebox.showinfo('sucess','All entry are Succesfully Checked')










       


        








if __name__ == "__main__":
 root=Tk()
 obj=Cust_Win(root)
 root.mainloop()