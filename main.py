from tkinter import *
import sqlite3 as db



mw=Tk()
mw.title("APS ASSIGNMENT SET-3")
#mw.geometry("680x480-8-200")
mw.config(bg="white")

conn=db.connect('Database.db')
c=conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS DATA
(
    date TEXT,    
    id TEXT,
    ic TEXT,
    ac_no TEXT,
    name TEXT,
    res TEXT,
    pan TEXT
     date_inc TEXT,    
    date_cmc TEXT,
    fax_no TEXT,
    st_no TEXT,
    cg_no TEXT,
    d_re1 TEXT,
    d_r2 TEXT,
    ie TEXT,
    vat TEXT,
    d_r3 TEXT,
    d_r4 TEXT,
    buv TEXT,
    twn TEXT,
    dis TEXT,
    sta TEXT,
    pin TEXT,
    coun TEXT,
    p_ad TEXT,
    p_twn TEXT,
    p_dis TEXT,
    p_sta TEXT,
    p_pin TEXT,
    p_coun TEXT
)''')

c.close()
conn.commit()
conn.close()



def submit():
    print("date", datevar.get())
    print("CUSTOMER Id", idvar.get())
    print("CUSTOMER IC", icvar.get())
    print("ACCOUNT NO.", ac_novar.get())
    print("Name", namevar.get())
    print("Register no.", resvar.get())
    print("Pan no.", panvar.get())
    print("Date of Incorporation", date_incvar.get())
    print("Date of Commencement of Bussiness", date_cmcvar.get())
    print("Fax NO.", fax_novar.get())
    print("Sales Tax Reg NO.", st_novar.get())
    print("CST/CGST Reg.NO", cg_novar.get())
    print("Date of Reg.", d_re1var.get())
    print("Date of Reg.", d_r2var.get())
    print("IE CODE", ievar.get())
    print("Vat Regn No.", vat_novar.get())
    print("Date of Registration", d_r3var.get())
    print("Date of Registration", d_r4var.get())
    print("Bussines Unit", buvar.get())
    print("CITY/TOWN", twnvar.get())
    print("District", disvar.get())
    print("State", stavar.get())
    print("PINCODE", pinvar.get())
    print("COUNTRY", counvar.get())
    print("Permanent Address", p_advar.get())
    print("CITY/TOWN", p_twnvar.get())
    print("District", p_disvar.get())
    print("State", p_stavar.get())
    print("PINCODE", p_pinvar.get())
    #print("COUNTRY", p_counvar.get())




    conn=db.connect('Database.db')
    c=conn.cursor()
    c.execute("Insert into DATA values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(datevar.get(), idvar.get(), icvar.get(), ac_novar.get(),namevar.get(),resvar.get(),panvar.get(),date_incvar.get(), date_cmcvar.get(), fax_novar.get(), st_novar.get(), cg_novar.get(), d_re1var.get(), d_r2var.get(), ievar.get(), vat_novar.get(), d_r3var.get(), d_r4var.get(), buvar.get(), twnvar.get(), disvar.get(), stavar.get(), pinvar.get(), counvar.get(), p_advar.get(), p_twnvar.get(), p_disvar.get(), p_stavar.get(), p_pinvar.get()))
    c.close()
    conn.commit()
    c.close()





datevar= StringVar()
lb=Label(mw, text="FOR OFFICE USE ONLY",font=('bold'), fg="red", bg="white").grid(row=0,column=0)
lb1=Label(mw, text="DATE", bg="white").grid(row=1,column=0,sticky="w")
en1=Entry(mw, textvariable=datevar).grid(row=1,column=1)

idvar= StringVar()
lb2=Label(mw, text="CUSTOMER ID", bg="white").grid(row=2,column=0,sticky="w")
en2=Entry(mw,  textvariable=idvar).grid(row=2, column=1)

icvar= StringVar()
lb3=Label(mw,text="CUSTOMER IC", bg="white").grid(row=1,column=2)
en3=Entry(mw, textvariable=icvar).grid(row=1, column=3)

ac_novar= StringVar()
lb4=Label(mw,text="ACCOUNT NO.", bg="white").grid(row=2,column=2)
en4 = Entry(mw, textvariable=ac_novar).grid(row=2, column=3)



nf=Label(mw,text="ACCOUNT OPTIONS:",font=('bold'),fg="red", bg="white").grid(row=3,column=0,sticky="w")
lbc=Label(mw, text="CURRENT ACCOUNT :", bg="white").grid(row=4,column=0,sticky="w")
rbv= IntVar()
rvb1=IntVar()
rvb2=IntVar()

r1=Checkbutton(mw, text="ORDINARY", bg="white"  )
r2=Checkbutton(mw, text="MULTICITY", bg="white" )

r1.grid(row=4, column=1, sticky="w")
r2.grid(row=4, column=2, sticky="w")

consti=Label(mw, text="CONSTITUTION:", fg="red", bg="white").grid(row=5, column=0, sticky="w")

r31 = Checkbutton(mw, text="SOLE PROPERIETER", bg="white" ).grid(row=5, column=1,sticky="w")
r32 = Checkbutton(mw, text="PARTNERSHIP", bg="white" ).grid(row=5, column=2,sticky="w")
r32 = Checkbutton(mw, text="LLP", bg="white" ).grid(row=5, column=3,sticky="w")
r33 = Checkbutton(mw, text="HLIF", bg="white" ).grid(row=5, column=4,sticky="w")
r34 = Checkbutton(mw, text="PRIVATE LTD COMPNY", bg="white" ).grid(row=5, column=5,sticky="w")
r35 = Checkbutton(mw, text="PUBLIC LTD COMPANY", bg="white" ).grid(row=5, column=6,sticky="w")
r36 = Checkbutton(mw, text="SOCIETY", bg="white" ).grid(row=5, column=7,sticky="w")
r37 = Checkbutton(mw, text="TRUST", bg="white" ).grid(row=5, column=8,sticky="w")
r38 = Checkbutton(mw, text="NGO/NPO", bg="white" ).grid(row=5, column=9,sticky="w")
r39 = Checkbutton(mw, text="ASSOCIATION/CLUB", bg="white" ).grid(row=6, column=1,sticky="w")
r311 = Checkbutton(mw, text="UNIVERSITY", bg="white" ).grid(row=6, column=2,sticky="w")
r312 = Checkbutton(mw, text="CENTRAL GOVERNMENT", bg="white" ).grid(row=6, column=3,sticky="w")
r313 = Checkbutton(mw, text="STATE GOVERNMENT", bg="white" ).grid(row=6, column=4,sticky="w")
r314 = Checkbutton(mw, text="CUASL GOVT", bg="white" ).grid(row=6, column=5,sticky="w")
r315 = Checkbutton(mw, text="FINANCIAL INST", bg="white" ).grid(row=6, column=6,sticky="w")
r316 = Checkbutton(mw, text="BANK", bg="white" ).grid(row=6, column=7,sticky="w")
r317 = Checkbutton(mw, text="STATUTARY BODY", bg="white" ).grid(row=6, column=8,sticky="w")




activity=Label(mw, text = "ACTIVITY",fg = "red", bg = "white").grid(row=7, column=0, sticky="w")
r41 = Checkbutton(mw, text="AVGI", bg="white").grid(row=7, column=1, sticky="w")
r42 = Checkbutton(mw, text="MFG", bg="white").grid(row=7, column=2, sticky="w")
r43 = Checkbutton(mw, text="TRADE", bg="white").grid(row=7, column=3, sticky="w")
r44 = Checkbutton(mw, text="FINANCE", bg="white").grid(row=7, column=4, sticky="w")
r45 = Checkbutton(mw, text="BANK", bg="white").grid(row=7, column=5, sticky="w")
r46 = Checkbutton(mw, text="TRANSPORT", bg="white").grid(row=7, column=6, sticky="w")
r47 = Checkbutton(mw, text="SERVICES", bg="white").grid(row=7, column=7, sticky="w")
r48 = Checkbutton(mw, text="GOVT", bg="white").grid(row=7, column=8, sticky="w")
r49 = Checkbutton(mw, text="REAL ESTATE", bg="white").grid(row=7, column=9, sticky="w")
r411 = Checkbutton(mw, text="STOCK BRICKER", bg="white").grid(row=7, column=10, sticky="w")
r412 = Checkbutton(mw, text="JEWELS/GEMS/PRECOUS METAL DEALER", bg="white").grid(row=8, column=1, sticky="w")
r413 = Checkbutton(mw, text="MONER SERVICES", bg="white").grid(row=8, column=2, sticky="w")
r414 = Checkbutton(mw, text="others", bg="white").grid(row=8, column=3, sticky="w")
lb414 = Label(mw,text="(specify)", bg="white").grid(row=8,column=4)
en414 = Entry(mw).grid(row=8, column=5)



lb_name = Label(mw, text="DETAILS OF BUSINESS UNIT",font=('bold'), fg="red", bg="white").grid(row=9,column=0)
lb_n1 = Label(mw,text="MESSERS", bg="white").grid(row=10,column=0)
namevar= StringVar()
lb_n2 = Label(mw,text="NAME:", bg="white").grid(row=10,column=1)
enn1 = Entry(mw, textvariable=namevar).grid(row=10, column=2)
lb_n3 = Label(mw,text="REGISTARATION NUMBER:", bg="white").grid(row=11,column=0)
lb_n4 = Label(mw,text="PAN NUMBER:", bg="white").grid(row=11,column=1)
lb_n4 = Label(mw,text="   FORM 60/61", bg="white").grid(row=11,column=3)
resvar= StringVar()
enn2 = Entry(mw, textvariable=resvar).grid(row=12, column=0)
panvar= StringVar()
enn3 = Entry(mw, textvariable=panvar).grid(row=12, column=1)
rn1 = Checkbutton(mw, text="Y", bg="white").grid(row=12, column=3, sticky="w")
rn2 = Checkbutton(mw, text="N", bg="white").grid(row=12, column=4, sticky="w")


cg_novar= StringVar()
d_re1var= StringVar()
d_r2var= StringVar()
date_incvar= StringVar()
date_cmcvar= StringVar()
fax_novar= StringVar()
st_novar= StringVar()
ievar= StringVar()
vat_novar= StringVar()
d_r3var= StringVar()
d_r4var= StringVar()
buvar= StringVar()
twnvar= StringVar()
disvar= StringVar()
stavar= StringVar()
pinvar= StringVar()
counvar= StringVar()
p_advar= StringVar()
p_twnvar= StringVar()
p_disvar= StringVar()
p_stavar= StringVar()
p_pinvar= StringVar()
#p_counvar= StringVar()

lb_n01=Label(mw,text="DATE OF INCORPORATION:", bg="white").grid(row=16,column=0)
lb_n02=Label(mw,text="DATE OF COMMENCEMENT OF BUSINESS:", bg="white").grid(row=16,column=1)
lb_n03=Label(mw,text="FAX NO.:", bg="white").grid(row=16,column=2)
enn01 = Entry(mw, textvariable=date_incvar).grid(row=17, column=0)
enn02 = Entry(mw, textvariable=date_cmcvar).grid(row=17, column=1)
enn03 = Entry(mw, textvariable=fax_novar).grid(row=17, column=2)

lb_n04=Label(mw,text="SALE TAX REGN NO.:", bg="white").grid(row=18,column=0)
lb_n05=Label(mw,text="CST/CGST REGN N0:", bg="white").grid(row=18,column=2)
enn04 = Entry(mw, textvariable=st_novar).grid(row=18, column=1)
enn05 = Entry(mw,textvariable=cg_novar).grid(row=18, column=3)

lb_n06=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=19,column=0)
lb_n07=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=19,column=2)
enn06 = Entry(mw, textvariable=d_re1var).grid(row=19, column=1)
enn07 = Entry(mw, textvariable=d_r2var).grid(row=19, column=3)

lb_n08=Label(mw,text="IE CODE:", bg="white").grid(row=20,column=0)
lb_n09=Label(mw,text="VAT REGN NO:", bg="white").grid(row=20,column=2)
enn08 = Entry(mw, textvariable=ievar).grid(row=20, column=1)
enn09= Entry(mw, textvariable=vat_novar).grid(row=20, column=3)

lb_n11=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=21,column=0)
lb_n12=Label(mw,text="DATE OF REGISTARATION:", bg="white").grid(row=21,column=2)
enn11 = Entry(mw, textvariable=d_r3var).grid(row=21, column=1)
enn12 = Entry(mw, textvariable=d_r4var).grid(row=21, column=3)


lb_n13=Label(mw,text="MAILIG ADDRESS:",font=('bold'),fg="red", bg="white").grid(row=22,column=0)
lb_n14=Label(mw,text="BUSINESS UNIT:", bg="white").grid(row=22,column=1)
enn13 = Entry(mw, textvariable=buvar).grid(row=23, column=1)
lb_n15=Label(mw,text="CITY/TOWN", bg="white").grid(row=24,column=0)
lb_n16=Label(mw,text="DISTRICT", bg="white").grid(row=25,column=0)
lb_n17=Label(mw,text="STATE", bg="white").grid(row=26,column=0)
lb_n18=Label(mw,text="PINCODE", bg="white").grid(row=25,column=2)
lb_n19=Label(mw,text="COUNTRY", bg="white").grid(row=26,column=2)
enn14 = Entry(mw, textvariable=twnvar).grid(row=24, column=1)
enn15 = Entry(mw, textvariable=disvar).grid(row=25, column=1)
enn16 = Entry(mw, textvariable=stavar).grid(row=25, column=3)
enn17 = Entry(mw, textvariable=pinvar).grid(row=26, column=1)
enn18 = Entry(mw, textvariable=counvar).grid(row=26, column=3)


lb_n21=Label(mw,text="PERMANENT ADDRESS:",font=('bold'),fg="red", bg="white").grid(row=27,column=0)
lb_n22=Label(mw,text="(IF DIFFERENT FROM ABOVE)", bg="white").grid(row=27,column=1)
enn19 = Entry(mw, textvariable=p_advar).grid(row=28, column=0)
lb_n23=Label(mw,text="CITY/TOWN", bg="white").grid(row=29,column=0)
lb_n24=Label(mw,text="DISTRICT", bg="white").grid(row=30,column=0)
lb_n25=Label(mw,text="STATE", bg="white").grid(row=31,column=0)
lb_n26=Label(mw,text="PINCODE", bg="white").grid(row=30,column=2)
lb_n27=Label(mw,text="COUNTRY", bg="white").grid(row=31,column=2)
enn21 = Entry(mw, textvariable=p_twnvar).grid(row=29, column=1)
enn22= Entry(mw, textvariable=p_disvar).grid(row=30, column=1)
enn23 = Entry(mw, textvariable=p_stavar).grid(row=30, column=3)
enn24 = Entry(mw, textvariable=p_pinvar).grid(row=31, column=1)
enn25 = Entry(mw).grid(row=31, column=3)




b1=Button(mw, text="SUMMIT", padx=10, pady=5, bg="red",command= submit).grid(row=32, column=1)



mainloop()