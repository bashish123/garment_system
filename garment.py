from tkinter import *
from tkinter import ttk
from time import strftime
import pymysql
from tkinter import messagebox
import numpy
class Garment:
    def __init__(self, root):
        self.root = root
        self.root.title("Management System")
        self.root.geometry("1420x700+0+0")
        self.No= StringVar()
        # self.DateTime = StringVar()
        self.Style_No = StringVar()
        self.Party_Name = StringVar()
        self.Quantity = StringVar()
        self.challan_No = StringVar()
        self.Laundry_Name = StringVar()
        self.ProgramStatus = StringVar()
        self.Note = StringVar()

        self.search_by=StringVar()
        self.search_text=StringVar()


        title = Label(self.root,text = "Garment Management System", bd = 10, relief = GROOVE, font = ("times new roman",24, "bold"), bg = "black", fg = "red")
        title.pack(side = TOP, fill = X)

        "=========top Frame==========="

        top_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "white")
        top_Frame.place(x = 10, y = 70, width = 1345, height = 666)

        "========manage frame========="

        manage_Frame = Frame(self.root, bd = 4, relief = RIDGE, bg = "light gray")
        manage_Frame.place(x = 20, y = 80, width = 1326, height = 280)

        manage_Frame1 = Frame(self.root, bd = 4, relief = RIDGE, bg = "white")
        manage_Frame1.place(x = 30, y = 125, width = 525, height = 230)

        m_title=Label(manage_Frame, text = "Received Challan", font = ("times new roman", 20, "bold"), bg = "black", fg = "white")
        m_title.grid(row = 0, columnspan = 1,padx = 400)

        "=====time Frame======"

        def time():
            string = strftime('%d-%m-%y %H:%M:%S %p')
            s_datetime.config(text = string)
            s_datetime.after(1000, time)

        s_datetime = Label(manage_Frame, font = ("times new roman", 15, "bold"), bg = "light gray", fg = "black")
        s_datetime.grid(row = 0, columnspan = 3, padx = 970)
        time()

        m_date = Label(manage_Frame, text = "Date", font = ("times new roman", 15, "bold"), bg = "light gray", fg = "black")
        m_date.grid(row = 0, columnspan = 2, padx = 920)

        "===No. Frame======="
        lblF_no = LabelFrame(manage_Frame,font = ("times new roman", 18, "bold"), bg = "light gray", fg = "light gray")
        lblF_no.place(x = 10, width = 190, height = 40)

        txt_no = Entry(lblF_no, textvariable = self.No, font = ("times new roman", 12, "bold"), bd = 5, relief = GROOVE)
        txt_no.grid( row = 0 , column = 1 , pady = 5 , padx = 5 , sticky = "w" )

        "======manage_Frame1==========="

        lbl_stylno=Label(manage_Frame1,text="Style No.",font=("times new roman",18,"bold"),bg="white",fg="black")
        lbl_stylno.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        txt_stylno=Entry(manage_Frame1,textvariable=self.Style_No,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_stylno.grid(row=0,column=1,pady=10,padx=10,sticky="w")

        lbl_partyname=Label(manage_Frame1, text="Party Name", font=("times new roman", 18, "bold"), bg="white",fg="black")
        lbl_partyname.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_partyname = Entry(manage_Frame1,textvariable=self.Party_Name, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_partyname.grid(row=1, column=1, pady=10, padx=10, sticky="w")

        lbl_Quantity = Label(manage_Frame1, text="Quantity", font=("times new roman", 18, "bold"), bg="white",fg="black")
        lbl_Quantity.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Quantity = Entry(manage_Frame1,textvariable=self.Quantity,font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_Quantity.grid(row=2, column=1, pady=10, padx=10, sticky="w")

        lbl_challanno = Label(manage_Frame1, text="P. Challan No.", font=("times new roman", 18, "bold"), bg="white",fg="black")
        lbl_challanno.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_challanno = Entry(manage_Frame1,textvariable=self.challan_No, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_challanno.grid(row=3, column=1, pady=10, padx=10, sticky="w")

        "======manage_Frame-2==========="

        manage_Frame2= Frame(self.root, bd=4, relief=RIDGE, bg="white")
        manage_Frame2.place(x=560, y=125, width=560, height=180)

        lbl_laundryname = Label(manage_Frame2, text="Laundry Name", font=("times new roman", 18, "bold"), bg="white",fg="black")
        lbl_laundryname.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        txt_laundryname = Entry(manage_Frame2,textvariable=self.Laundry_Name, font=("times new roman", 18, "bold"), bd=5, relief=GROOVE)
        txt_laundryname.grid(row=0, column=1, pady=10, padx=10, sticky="w")

        lbl_pgmst = Label(manage_Frame2, text="program Status", font=("times new roman", 18, "bold"),
                          bd=5, bg="white",fg="black")
        lbl_pgmst.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        lbl_Note = Label(manage_Frame2, text="Note", font=("times new roman", 18, "bold"), bg="white",fg="black")
        lbl_Note.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_Note=Entry(manage_Frame2,textvariable=self.Note,font=("",20),bd=5)
        txt_Note.grid(row=2,column=1,pady=10,padx=10,sticky="w")

        combo_pgmst=ttk.Combobox(manage_Frame2, text=self.ProgramStatus, font=("times new roman", 16, "bold"))
        combo_pgmst['values']=("Yes","No")
        combo_pgmst.grid(row=1,column=1,pady=10,padx=10,sticky="w")

        "======BUTTON FRAME=========="

        btn_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=1128, y=125, width=200, height=225)

        addnewbtn=Button(btn_Frame,text="Add",width=15,command=self.add_received,font=("times new roman", 13, "bold")).grid(row=0,column=0,padx=20,pady=5)
        clearbtn = Button(btn_Frame, text="Clear", width=15,command=self.clear,font=("times new roman", 13, "bold")).grid(row=2, column=0, padx=20, pady=4)
        updatebtn = Button(btn_Frame, text="Update", width=15,command=self.update_data,font=("times new roman", 13, "bold")).grid(row=3, column=0, padx=20, pady=3)
        deletebtn = Button(btn_Frame, text="Delete", width=15,command=self.delete_data,font=("times new roman", 13, "bold")).grid(row=4, column=0, padx=20, pady=4)
        # exitbtn = Button(btn_Frame, text="Exit", width=15).grid(row=5, column=0, padx=20, pady=0)
        #

        "=========Detail Frame==========="

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="yellow")
        Detail_Frame.place(x=20, y=367, width=1326, height=326)

        lbl_search=Label(Detail_Frame,text="Search By:",bg="yellow",fg="black",font=("times new roman", 18, "bold"))
        lbl_search.grid(row=0,column=0,pady=0,padx=0,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=13,font=("times new roman", 16, "bold"))
        combo_search['values'] = ("No","Style_No", "Party_Name","challan_No.","Laundry_Name","Note")
        combo_search.grid(row=0, column=1, pady=0, padx=0, sticky="w")

        txt_text =Entry(Detail_Frame, width=30,font=("times new roman", 10),textvariable=self.search_text)
        txt_text.grid(row=0, column=2, pady=0, padx=10,ipady=10, sticky="w")

        searchbtn = Button(Detail_Frame,command=self.search_data, text="Search", width=15, font=("times new roman", 13, "bold"))\
            .grid(row=0, column=3,padx=20, pady=5)
        showallbtn = Button(Detail_Frame,command=self.fetch_data, text="Show All", width=15, font=("times new roman", 13, "bold"))\
            .grid(row=0,column=4,padx=20,pady=2)

        clear2btn = Button(Detail_Frame, text="Clear",command=self.clear2, width=15, font=("times new roman", 13, "bold")).grid(row=0,
                                                                                                          column=5,
                                                                                                          padx=20,
                                                                                                          pady=2)

        "=====Table Frame========="
        table_frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=50,width=1310,height=260)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.table=ttk.Treeview(table_frame,columns=("no", "style_no", "quantity", "programStatus", "note", "challan_No", "party_Name", "laundry_Name"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)
        self.table.heading("no", text="No")
        # table.heading("Date & Time",text="Date & Time")
        self.table.heading("style_no", text="Style_No")
        self.table.heading("quantity", text="Quantity")
        self.table.heading("programStatus", text="ProgramStatus")
        self.table.heading("note", text="Note")
        self.table.heading("challan_No", text="challan_No")
        self.table.heading("party_Name", text="Party_Name")
        self.table.heading("laundry_Name", text="Laundry_Name")
        self.table['show']='headings'
        self.table.column("no", width=50)
        self.table.column("challan_No",width=120)
        # table.column("Style No.", width=120)
        # # table.column("Party Name", width=100)
        # # table.column("Quantity", width=100)
        # # table.column("Laundry Name", width=100)
        self.table.column("programStatus", width=120)
        # # table.column("Note", width=200)

        self.table.pack(fill=BOTH,expand=1)
        self.table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_received(self):
        if self.No.get()=="" or self.Style_No.get()=="" or self.Quantity.get()=="" or self.ProgramStatus.get()=="" or self.Note.get()=="" or self.challan_No.get()=="" or self.Party_Name.get()=="" or self.Laundry_Name.get()=="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=pymysql.connect(host="localhost",port=3306,user="root",password="",database="received_challan")
            cur=con.cursor()
            cur.execute("insert into received_challan values(%s,%s,%s,%s,%s,%s,%s,%s)", (self.No.get(),  self.Style_No.get(), self.Quantity.get(), self.ProgramStatus.get(), self.Note.get(), self.challan_No.get(), self.Party_Name.get(), self.Laundry_Name.get(),))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record Has Been Inserted")

    def fetch_data(self):
        con = pymysql.connect(host='localhost', port=3306, user="root", password="", database="received_challan")
        cur = con.cursor()
        cur.execute("select * from received_challan")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for row in rows:
                self.table.insert('',END,values=row)
            con.close()

    def clear(self):
        self.No.set("")
        self.Style_No.set("")
        self.Party_Name.set("")
        self.Quantity.set("")
        self.challan_No.set("")
        self.Laundry_Name.set("")
        self.ProgramStatus.set("")
        self.Note.set("")

    def clear2(self):
        self.search_text.set("")
        self.search_by.set("")

        self.fetch_data()


    def get_cursor(self,ev):
        cursor_row=self.table.focus()
        content=self.table.item(cursor_row)
        row=content['values']
        self.No.set(row[0])
        self.Style_No.set(row[1])
        self.Party_Name.set(row[6])
        self.Quantity.set(row[2])
        self.challan_No.set(row[5])
        self.Laundry_Name.set(row[7])
        self.ProgramStatus.set(row[3])
        self.Note.set(row[4])

    def update_data(self):
         con = pymysql.connect(host="localhost", port=3306, user="root", password="", database="received_challan");
         cur = con.cursor()
         cur.execute("UPDATE received_challan SET Style_No = %s, Quantity = %s,ProgramStatus = %s,Note=%s,challan_No = %s, Party_Name = %s, Laundry_Name = %s  WHERE No=%s",(self.Style_No.get(),self.Quantity.get(),
                                                                                                                                                                   self.ProgramStatus.get(),
                                                                                                                                                                   self.Note.get(),
                                                                                                                                                                   self.challan_No.get(),
                                                                                                                                                                   self.Party_Name.get(),
                                                                                                                                                                   self.Laundry_Name.get(),
                                                                                                                                                                   self.No.get()
                                                                                                                                                                          ))
         con.commit()
         self.fetch_data()
         self.clear()
         con.close()

    def delete_data(self):
        con = pymysql.connect(host='localhost', port=3306, user="root", password="", database="received_challan")
        cur = con.cursor()
        cur.execute("delete from received_challan WHERE No=%s",self.No.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()


    def search_data(self):
            con = pymysql.connect(host='localhost', port=3306, user="root", password="", database="received_challan")
            cur = con.cursor()
            cur.execute("select * from received_challan WHERE "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
            rows=cur.fetchall()
            if len(rows)!=0:
                self.table.delete(*self.table.get_children())
                for row in rows:
                    self.table.insert('',END,values=row)
                con.commit()
            con.close()

root=Tk()
ob=Garment(root)
root.mainloop()