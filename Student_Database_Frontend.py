#Frontend

from tkinter import*
import tkinter.messagebox
#import stdDatabase

class Student:
    def __init__(self,root):
        self.root = root
        self.root.title("Student DataBase Management System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="cadet blue")
        
        StdID = StringVar()
        Firstname = StringVar()
        CifID = StringVar()
        Surname = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        #=================Functions===========================

        def iExit():
            iExit=tkinter.messagebox.askyesno("Student Database Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        #================Frames=======================
        MainFrame = Frame(self.root,bg="cadet blue")
        MainFrame.grid()
        
        TitFrame = Frame(MainFrame,bd=2,padx=54,pady=8,bg="Ghost White",relief=RIDGE)
        TitFrame.pack(side=TOP)
        
        self.lblTit = Label(TitFrame,font=('arial',47,'bold'),text="Student Database Management System",bg="Ghost White")
        self.lblTit.grid()
        
        ButtonFrame = Frame(MainFrame,bd=2,width=1350,height=70,padx=18,pady=10,bg="Ghost White",relief = RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(MainFrame,width=1300,height=400,padx=20,pady=20,bg="Ghost White", relief=RIDGE)
        DataFrame.pack(side=LEFT)
        
        DataFrameLEFT = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="Student Info\n")
        DataFrameLEFT.pack(side=LEFT)
        
        DataFrameRIGHT = LabelFrame(DataFrame,bd=1,width=450,height=300,padx=31,pady=3,relief=RIDGE,bg="Ghost White",font=('arial',20,'bold'),text="Student Details\n")
        DataFrameRIGHT.pack(side=RIGHT)
        
        #====================================Labels and Entries======================================
        self.lblStdID = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Student ID",padx=2,pady=2,bg="Ghost White")
        self.lblStdID.grid(row=0,column=0,sticky=W)
        self.txtStdID = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=StdID,width =39)
        self.txtStdID.grid(row=0,column=1)
        
        self.lblfna = Label(DataFrameLEFT,font=('arial',20,'bold'),text="First Name",padx=2,pady=2,bg="Ghost White")
        self.lblfna.grid(row=1,column=0,sticky=W)
        self.txtfna = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Firstname,width =39)
        self.txtfna.grid(row=1,column=1)
        
        self.lblsna = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Last Name",padx=2,pady=2,bg="Ghost White")
        self.lblsna.grid(row=2,column=0,sticky=W)
        self.txtsna = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Surname,width =39)
        self.txtsna.grid(row=2,column=1)
        
        self.lbldob = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Date of Birth",padx=2,pady=2,bg="Ghost White")
        self.lbldob.grid(row=3,column=0,sticky=W)
        self.txtdob = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=DoB,width =39)
        self.txtdob.grid(row=3,column=1)
        
        self.lblage = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Age",padx=2,pady=2,bg="Ghost White")
        self.lblage.grid(row=4,column=0,sticky=W)
        self.txtage = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Age,width =39)
        self.txtage.grid(row=4,column=1)
        
        self.lblgen = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Gender",padx=2,pady=2,bg="Ghost White")
        self.lblgen.grid(row=5,column=0,sticky=W)
        self.txtgen = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Gender,width =39)
        self.txtgen.grid(row=5,column=1)
        
        self.lbladd = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Address",padx=2,pady=2,bg="Ghost White")
        self.lbladd.grid(row=6,column=0,sticky=W)
        self.txtadd = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Address,width =39)
        self.txtadd.grid(row=6,column=1)
        
        self.lblphn = Label(DataFrameLEFT,font=('arial',20,'bold'),text="Phone No",padx=2,pady=2,bg="Ghost White")
        self.lblphn.grid(row=7,column=0,sticky=W)
        self.txtphn = Entry(DataFrameLEFT,font=('arial',20,'bold'),textvariable=Mobile,width =39)
        self.txtphn.grid(row=7,column=1)
        #====================================ListBox and ScrollBar Widget===========================================
        scrollbar=Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        studentlist = Listbox(DataFrameRIGHT,width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        studentlist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=studentlist.yview)
        
        #==============================Button Widget==========================
        self.btnAddDate = Button(ButtonFrame,text="Add New",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=1)
        
        self.btnAddDate = Button(ButtonFrame,text="Display",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=2)
        
        self.btnAddDate = Button(ButtonFrame,text="Clear",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=3)
        
        self.btnAddDate = Button(ButtonFrame,text="Delete",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=4)
        
        self.btnAddDate = Button(ButtonFrame,text="Search",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=5)
        
        self.btnAddDate = Button(ButtonFrame,text="Update",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=6)
        
        self.btnAddDate = Button(ButtonFrame,text="Exit",font=('arial',20,'bold'),height=1,width=10,bd=4)
        self.btnAddDate.grid(row=0,column=7)
        
if __name__ == '__main__':
    root = Tk()
    application = Student(root)
    root.mainloop()