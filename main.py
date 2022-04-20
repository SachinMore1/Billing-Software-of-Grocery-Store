from cgitb import text
from fileinput import filename
from http.client import FOUND
import string
from time import strftime
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
import random,os
from tkinter import messagebox

from setuptools import Command
import tempfile
from time import strftime



class Bill_App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1530x800+0+0")
        self.master.title("bILLING SOFTWARE")

        # ==================== Variables =======================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)

        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()


        # Image1
        img_1 = Image.open("image/b2.jpg")
        img_1 = img_1.resize((510, 130), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_img_1 = Label(self.master, image=self.photoimg_1)
        lbl_img_1.place(x=0, y=0, width=513, height=130)

        # Image 2
        img_2 = Image.open("image/b3.jpg")
        img_2 = img_2.resize((510, 130), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_img_2 = Label(self.master, image=self.photoimg_2)
        lbl_img_2.place(x=510, y=0, width=513, height=130)

        # Image 3
        img_3 = Image.open("image/mall.jpg")
        img_3 = img_3.resize((510, 130), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)

        lbl_img_3 = Label(self.master, image=self.photoimg_3)
        lbl_img_3.place(x=1020, y=0, width=514, height=130)

        #    Name of software
        lbl_title = Label(self.master, text="शिवानंद किराणा स्टोअर", font=(
            "Aparajita", 36, "bold"), fg="red", bg="white")
        lbl_title.place(x=0, y=130, width=1540, height=60)


        # ======== TIME =============
        def time():
            string = strftime('%I:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)
        lbl = Label(lbl_title, font= ('times new roman',16,'bold'), background='white', foreground='blue')
        lbl.place(x=0,y=0, width=120,height=45)
        time()

        Main_Frame = Frame(self.master, bd=5, relief=GROOVE,bg="white")
        Main_Frame.place(x=0,y=175,width=1530,height=620)
            


        # --------------- ADDING LISTS IN EACH MENU ----------------------------
        #  LIST OF PRODUCT CATEGORY
        self.Category = ["Select Option", "General Products", "Footware", "Bakery Products","Coldrinks", "Stationary", "Mobile Accessories"]

        self.SubCatGeneral_Products = ["Normal Products","Cereals", "Spices", "Washing Products", "Pulses","Other"]
        self.SubCatFootware = ["Shoes", "sleepar", "Sandle", "Chapal"]
        self.SubCatMobile =["Simcards","Earphone", "Cover", "Mobiles"]
        self.SubBakery_Products = ["Bread","Butter","cake","Choklets","cream products"]
        self.SubColdrinks=["ice-cream","Thumps-Up","Juice","Milk-Shakes","Water-Bottle"]
        self.SubStationary=["NoteBook","Books","Pens","SchoolBox","SchoolBags"]

        #  Main Frame
        Main_Frame = Frame(self.master, bd=5, relief=GROOVE, bg='#dcf7f5')
        Main_Frame.place(x=0, y=180, width=1540, height=625)

        # customer frame
        Cust_Frame = LabelFrame(Main_Frame, text="Customer Details", font=(
            "Aparajita", 15, "bold"), fg="red", bg="#dcf7f5", bd=4)
        Cust_Frame.place(x=10, y=5, width=350, height=100)

        # Customer name field
        self.lbl_CustName = Label(Cust_Frame, text="Customer Name", font=(
            "Aparajita", 15, "bold"), bg="#dcf7f5")
        self.lbl_CustName.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.entry_CustName = ttk.Entry(Cust_Frame,textvariable=self.c_name, font=(
            "Times New Roman", "12", "bold"), width=24)
        self.entry_CustName.grid(row=0, column=1)
        # mobile field
        self.lbl_Mob = Label(Cust_Frame, text="Mobile No.", font=(
            "Aparajita", 15, "bold"), bg="#dcf7f5")
        self.lbl_Mob.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.entry_mob = ttk.Entry(Cust_Frame,textvariable=self.c_phone, font=(
            "Times New Roman", "12", "bold"), width=24)
        self.entry_mob.grid(row=1, column=1)

        # Product Frame
        Product_Frame = LabelFrame(Main_Frame, text="Product Details", font=(
            "Aparajita", 15, "bold"), fg="red", bg="#dcf7f5", bd=4)
        Product_Frame.place(x=370, y=5, width=700, height=100)

        # Select Category
        self.lbl_Category = Label(Product_Frame, text="Select Categories", font=(
            "Aparajita", 15, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_Category.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Category = ttk.Combobox(Product_Frame, value = self.Category, font=(
            "Aparajita", "10", "bold"), width=25, state="readonly")
        self.Combo_Category.current(0)   
        self.Combo_Category.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.categories)

        # Product Name
        self.lbl_Product = Label(Product_Frame, text="Product Name", font=(
            "Aparajita", 15, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_Product.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.Combo_Product = ttk.Combobox(
            Product_Frame, textvariable=self.product, font=("Aparajita", "13", "bold"), width=25)
        self.Combo_Product.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.Combo_Product.bind("<<ComboboxSelected>>", self.productprice)

        # Price
        self.lbl_ammount = Label(Product_Frame, text="Price", font=(
            "Aparajita", 15, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_ammount.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.entry_ammount = ttk.Entry(
            Product_Frame, textvariable=self.prices, font=("Aparajita", "13", "bold"), width=25)
        self.entry_ammount.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        # Product Quantity
        self.lbl_quantity = Label(Product_Frame, text="Product Quantity", font=(
            "Aparajita", 15, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_quantity.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.entry_quantity = ttk.Entry(
            Product_Frame, textvariable=self.qty, font=("Aparajita", "13", "bold"), width=27)
        self.entry_quantity.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        # Middle Frame
        Middle_Frame = Frame(Main_Frame, bg="#dcf7f5", bd=10)
        Middle_Frame.place(x=10, y=110, width=1100, height=400)

        # image 4
        img_4 = Image.open("image/good.jpg")
        img_4 = img_4.resize((549, 400), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        lbl_img_4 = Label(Middle_Frame, image=self.photoimg_4)
        lbl_img_4.place(x=0, y=0, width=549, height=400)

        # image 5
        img_5 = Image.open("image/market.jpg")
        img_5 = img_5.resize((549, 400), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        lbl_img_5 = Label(Middle_Frame, image=self.photoimg_5)
        lbl_img_5.place(x=551, y=0, width=549, height=400)

        # Search Bar
        Search_Frame = Frame(Main_Frame, bd=2, bg="#dcf7f5")
        Search_Frame.place(x=1115, y=5, width=400, height=40)

        self.lbl_Bill = Label(Search_Frame,text="Bill Number", font=(
            "Aparajita", 14, "bold"), bg="red", fg='white')
        self.lbl_Bill.grid(row=0, column=0, sticky=W, padx=1)

        self.entry_Bill = ttk.Entry(Search_Frame,  textvariable=self.search_bill,font=(
            "Aparajita", 14, "bold"), width=25)
        self.entry_Bill.grid(row=0, column=1, sticky=W, padx=2)

        self.BtnSearch = Button(Search_Frame, command=self.find_bill ,text="Search", height=1, font=(
            "Aparajita", 13, "bold"), bg="#a1200e", fg="white", cursor='hand2', width=12)
        self.BtnSearch.grid(row=0, column=4)

        # Right Frame Billing Area
        Right_Frame = LabelFrame(Main_Frame, text="Bill Area", font=(
            "Aparajita", 15, "bold"), fg="red", bg="#dcf7f5", bd=4)
        Right_Frame.place(x=1115, y=40, width=400, height=440)

        # Scroll Bar
        scroll_y = Scrollbar(Right_Frame, orient=VERTICAL)
        self.textarea = Text(Right_Frame, yscrollcommand=scroll_y.set,
                             bg="white", fg="blue", font=("Aparajita", 12, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        # Attach text field with scrollbar use method config
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand=1)

        # Bill Counter
        BillCounter_Frame = LabelFrame(Main_Frame, text="Bill Counter", font=(
            "Aparajita", 15, "bold"), fg="red", bg="#dcf7f5", bd=4)
        BillCounter_Frame.place(x=10, y=480, width=1505, height=125)

        # SubTotal
        self.lbl_SubTotal = Label(BillCounter_Frame, text="SubTotal", font=(
            "Aparajita", 13, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_SubTotal.grid(row=0, column=0, sticky=W, padx=5, pady=1)

        self.entry_SubTotal = ttk.Entry(
            BillCounter_Frame, textvariable=self.sub_total, font=("Aparajita", "10", "bold"), width=26)
        self.entry_SubTotal.grid(row=0, column=1)

        #  Gov Tax
        self.lbl_GovTax = Label(BillCounter_Frame, text="Gov Tax", font=(
            "Aparajita", 13, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_GovTax.grid(row=1, column=0, sticky=W, padx=5, pady=1)

        self.entry_GovTax = ttk.Entry(BillCounter_Frame, textvariable=self.tax_input, font=(
            "Aparajita", "10", "bold"), width=26)
        self.entry_GovTax.grid(row=1, column=1)

        # Total
        self.lbl_Total = Label(BillCounter_Frame, text="Total", font=(
            "Aparajita", 13, "bold"), bg="#dcf7f5", bd=4)
        self.lbl_Total.grid(row=2, column=0, sticky=W, padx=5, pady=1)

        self.entry_Total = ttk.Entry(BillCounter_Frame, textvariable=self.total, font=(
            "Aparajita", "10", "bold"), width=26)
        self.entry_Total.grid(row=2, column=1)

        #  Button Frame
        Btn_Frame = Frame(BillCounter_Frame, bd=2, bg="#dcf7f5")
        Btn_Frame.place(x=280, y=0)

        # Add To Cart
        self.BtnAddToCart = Button(Btn_Frame,command=self.AddItem,text="Add To Cart", height=1, font=(
            "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        self.BtnAddToCart.grid(row=2, column=0, padx=1, pady=25)

        # # Purches
        # self.BtnPurches = Button(Btn_Frame, text="Purches", height=1, font=(
        #     "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        # self.BtnPurches.grid(row=2, column=1, padx=1, pady=25)

        # Generate Bill
        self.BtnGenerateBill = Button(Btn_Frame, command = self.gen_bill, text="Generate Bill",  height=1, font=(
            "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        self.BtnGenerateBill.grid(row=2, column=2, padx=1, pady=25)

        # Save Bill
        self.BtnSaveBill = Button(Btn_Frame, command=self.save_bill, text="Save Bill", height=1, font=(
            "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        self.BtnSaveBill.grid(row=2, column=3, padx=1, pady=25)

        # Print
        self.BtnPrint = Button(Btn_Frame, command=self.iprint, text="Print", height=1, font=(
            "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        self.BtnPrint.grid(row=2, column=4, padx=1, pady=25)

        # Clear
        self.BtnClear = Button(Btn_Frame, command=self.Clear,text="Clear", height=1, font=(
            "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        self.BtnClear.grid(row=2, column=5, padx=1, pady=25)

        # #  Stock
        # self.BtnStock = Button(Btn_Frame, text="Stock", height=1, font=(
        #     "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        # self.BtnStock.grid(row=2, column=6, padx=1, pady=25)

        # Exit
        self.BtnExit = Button(Btn_Frame, command=self.master.destroy,text="Exit", height=1, font=(
            "Aparajita", 15, "bold"), bg="#a1200e", fg="#b6f2d1", width=10, cursor='hand2')
        self.BtnExit.grid(row=2, column=7, padx=1, pady=25)

        self.WelCome()

        self.l=[]

    # ======================== Function Declaration ========================
   
        # ========= Add to Cart =========
    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please Select the Product!")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t\t{self.qty.get()}\t\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l)) - (self.prices.get()))*Tax)/100)))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))
        
        # === Generate Bill ===
    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            sam=self.textarea.get(8.0,(10.0+float(len(self.l))))
            self.WelCome()
            self.textarea.insert(END,sam)
            self.textarea.insert(END,"\n====================================================\n")
            self.textarea.insert(END,f"\n Sub Ammount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Ammount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Ammount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,"\n====================================================\n")

        # ==== Save Bill =====
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('BILLS/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill No:{self.bill_no.get()} Saved Successfully ")
            f1.close() 

        # ==== Print Button =====
    def iprint(self):
        p = self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(p)
        os.startfile(filename,"print")

        # ==== Search Bill ====
    def find_bill(self):
        found= "no"
        for i in os.listdir("BILLS/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found =='no': 
            messagebox.showerror("Error","Invalid Bill No")


        # ===== Clear Button =========
    def Clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.bill_no.set("")
        z=random.randint(1000,9999)
        self.bill_no.set(z)

        self.search_bill.set("")
        self.product.set("")
        self.prices.set(0)
        self.qty.set(1)
        self.l=[0]
        self.sub_total.set("")
        self.tax_input.set('')
        self.total.set("")
        self.WelCome()

    # ========== Welcome containt =============
    def WelCome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t WEL-COME TO SHIVANAND KIRANA STORE")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")

        self.textarea.insert(END,"\n====================================================")
        self.textarea.insert(END,f"\n Products\t\t\tQTY\t\t\tPrice")
        self.textarea.insert(END,"\n====================================================\n")

    def categories(self,event=""):
        if self.Combo_Category.get()=="General Products":
            self.Combo_Product.config(value=self.SubCatGeneral_Products)
            self.Combo_Product.current(0)

        if self.Combo_Category.get()=="Bakery Products":
            self.Combo_Product.config(value=self.SubBakery_Products)
            self.Combo_Product.current(0)

        if self.Combo_Category.get()=="Coldrinks":
            self.Combo_Product.config(value=self.SubColdrinks)
            self.Combo_Product.current(0)

        if self.Combo_Category.get()=="Stationary":
            self.Combo_Product.config(value=self.SubStationary)
            self.Combo_Product.current(0)

        if self.Combo_Category.get()=="Footware":
            self.Combo_Product.config(value=self.SubCatFootware)
            self.Combo_Product.current(0)

        if self.Combo_Category.get()=="Mobile Accessories":
            self.Combo_Product.config(value=self.SubCatMobile)
            self.Combo_Product.current(0)

    def productprice(self,event=""):
        
        # General Product
        if  self.Combo_Product.get()=="Normal Products":
            self.prices.set(0)
            self.qty.set(1)
        
        if  self.Combo_Product.get()=="Cereals":
            self.prices.set(0)
            self.qty.set(1)
        
        if  self.Combo_Product.get()=="Spices":
            self.prices.set(0)
            self.qty.set(1)
        
        if  self.Combo_Product.get()=="Washing Products":
            self.prices.set(0)
            self.qty.set(1)
        
        if  self.Combo_Product.get()=="Pulses":
            self.prices.set(0)
            self.qty.set(1)
        
        if  self.Combo_Product.get()=="Other":
            self.prices.set(0)
            self.qty.set(1)

        
        # Footware
        if  self.Combo_Product.get()=="Shoes":
            self.prices.set(0)
            self.qty.set(1)
        
        if  self.Combo_Product.get()=="sleepar":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Sandle":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Chapal":
            self.prices.set(0)
            self.qty.set(1)

        # Mobile
        if  self.Combo_Product.get()=="Simcards":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Cover":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Earphone":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Mobiles":
            self.prices.set(0)
            self.qty.set(1)

        #  Bakery

        if  self.Combo_Product.get()=="Bread":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Butter":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="cake":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Choklets":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="cream products":
            self.prices.set(0)
            self.qty.set(1)

        # Coldrinks

        if  self.Combo_Product.get()=="ice-cream":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Thumps-Up":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Juice":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Milk-Shakes":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Water-Bottle":
            self.prices.set(0)
            self.qty.set(1)

        # Stationary

        if  self.Combo_Product.get()=="NoteBook":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Books":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="Pens":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="SchoolBox":
            self.prices.set(0)
            self.qty.set(1)
            
        if  self.Combo_Product.get()=="SchoolBags":
            self.prices.set(0)
            self.qty.set(1)

        if  self.Combo_Product.get()=="":
            self.prices.set(0)
            self.qty.set(1)


    
        
        
                

if __name__ == '__main__':
    master = Tk()
    obj = Bill_App(master)
    master.mainloop()

