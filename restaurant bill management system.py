from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import math,random 

def btn_is_clicked():
    messagebox.showinfo("ALOO TIKKI BURGER", "It consists of a toasted bun with a potato patty topped fresh tomato,and tandoori Mayo!")

def btn_is_clicked2():
    messagebox.showinfo("VEGGIE BURGER", "It consists of a fried patty of ground vegetables, with lettuce,ketchup and mayo in a wholewheat bun!")

def btn_is_clicked3():
    messagebox.showinfo("CHICKEN BURGER", "Crispy seasoned chicken breast, topped with melted cheese and piled on wholewheat bun with onion, lettuce, tomato and garlic mayo!")

def btn_is_clicked5():
    messagebox.showinfo("CHICKEN POPCORN", "It consists of small, bite-sized pieces of chicken breast that have been breaded and fried!")

def btn_is_clicked4():
    messagebox.showinfo("FRIES", "These are thin, salted slices of deep fried potatoes served at room temperature!")

def btn_is_clicked6():
    messagebox.showinfo("COLD COFFEE", "It is a beverage served chilled and includes cream,coco powder or coffee beans!")

def btn_is_clicked7():
    messagebox.showinfo("COLD DRINKS", "750ml of COKE,SPRITE,PEPSI,MOUNTAIN DEW,FANTA,APPY FIZ ETC. ask the counter for available options!")

def btn_is_clicked8():
    messagebox.showinfo("ICE CREAM FLOAT", "IT is a chilled beverage that consists of ice cream in either COKE,SPRITE OR FANTA!")

def btn_is_clicked9():
    messagebox.showinfo("MOJITO", "It is a chilled combination of sweetness,citrus and herbaceous mint flavors and consists of lime juice,soda water,and mint!")

def btn_is_clicked10():
    messagebox.showinfo("ICE CREAM", "200ml of vanilla or strawberry ice cream served in cup or choco cone with customizable toppings!")

user_entry = []
food_items = []

def clear_entry():
    value1.set(0)
    value2.set(0)
    value3.set(0)
    value4.set(0)
    value5.set(0)
    value6.set(0)
    value7.set(0)
    value8.set(0)
    value9.set(0)
    value10.set(0)
    Lbl_bill.pack_forget()
    return()


def calculate_bill():
    global Lbl_bill
    aloo_tikki_burger=entry_atburger.get()
    veggie_burger=entry_vegburger.get()
    chicken_burger=entry_chickenburger.get()
    fries=entry_fries.get()
    chicken_popcorn=entry_chickenpopcorn.get()
    cold_coffee=entry_coldcoffee.get()
    cold_drink=entry_colddrink.get()
    icecream_float=entry_float.get()
    mojito=entry_mojito.get()
    icecream=entry_icecream.get()
    total=((int(aloo_tikki_burger)*30)+(int(veggie_burger)*50)+(int(chicken_burger)*70)+(int(fries)*40)+(int(chicken_popcorn)*70)+(int(cold_coffee)*50)+(int(cold_drink)*40)+(int(icecream_float)*50)+(int(mojito)*40)+(int(icecream)*40))
    Lbl_bill = Label(btnrow5, text=total,width=10, bg="#262525", fg="gold", font=("seoge ui black bold", 20))
    Lbl_bill.pack(side=LEFT, anchor="center", pady=30)

def adlogin():
    top = Toplevel()
    top.title("LOGIN")
    top.geometry("700x500")
    framelogin1 = Frame(top, bg="#262525")
    framelogin1.pack(fill="both")
    framelogin2 = Frame(top, bg="#262525")
    framelogin2.pack(fill="both")
    framelogin3 = Frame(top, bg="#262525")
    framelogin3.pack(fill="both", expand=True)
    Lbl_bill = Label(framelogin1, text="USER-ID", bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)
    Lbl_bill = Label(framelogin2, text="PASSWORD", bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=LEFT, anchor="nw", pady=20)

    for x in range(1):
        value1 = StringVar()
        entry_userid = Entry(framelogin1, textvariable=value1, width=40)
        entry_userid.pack(side=LEFT, anchor="nw", padx=90, pady=35)
        user_entry.append(entry_userid)

    for x in range(1):
        value1 = StringVar()
        entry_userid = Entry(framelogin2, show="*",textvariable=value1, width=40)
        entry_userid.pack(side=LEFT, anchor="nw", padx=41, pady=35)
        user_entry.append(entry_userid)

    btnlogin = Button(framelogin3, border=0, text="LOG-IN", bg="#262525", fg="gold", compound=TOP,
                   font=("gill sans ultra bold condensed", 20),borderwidth=5, command=top.destroy)
    btnlogin.pack(side=TOP, anchor="sw", padx=200, pady=0)


def view_cart():

    def generate_bill():
        bill_number=random.randint(100,1000)
        bill_number_tk=StringVar()
        bill_number_tk.set(bill_number)
        txtReceipt.insert(END, "\t\tMADHIT CAFE")
        txtReceipt.insert(END, "\n*************************************************")
        txtReceipt.insert(END, "ORDER NUMBER :"+ bill_number_tk.get())
        txtReceipt.insert(END, "\n*************************************************")
        txtReceipt.insert(END, '\n ITEMS\t\t' +"PRICE\t\t" + "QUANTITY ")
        txtReceipt.insert(END, "\n*************************************************")
        aloo_tikki_burger = entry_atburger.get()
        if int(aloo_tikki_burger)!=0:
            txtReceipt.insert(END, 'Aloo Tikki Burger\t\t' "30/-\t\t" + entry_atburger.get() + "\n")
        veggie_burger = entry_vegburger.get()
        if int(veggie_burger)!=0:
            txtReceipt.insert(END, 'Veggie Burger\t\t' "50/-\t\t" + entry_vegburger.get() + "\n")
        chicken_burger = entry_chickenburger.get()
        if int(chicken_burger)!=0:
            txtReceipt.insert(END, 'Chicken Burger\t\t' "70/-\t\t" + entry_chickenburger.get() + "\n")
        fries = entry_fries.get()
        if int(fries)!=0:
            txtReceipt.insert(END, 'Fries\t\t' "40/-\t\t" + entry_fries.get() + "\n")
        chicken_popcorn = entry_chickenpopcorn.get()
        if int(chicken_popcorn)!=0:
            txtReceipt.insert(END, 'Chicken Popcorn\t\t' "70/-\t\t" + entry_chickenpopcorn.get() + "\n")
        cold_coffee = entry_coldcoffee.get()
        if int(cold_coffee)!=0:
            txtReceipt.insert(END, 'Cold Coffee\t\t' "50/-\t\t" + entry_coldcoffee.get() + "\n")
        cold_drink = entry_colddrink.get()
        if int(cold_drink)!=0:
            txtReceipt.insert(END, 'Cold Drink\t\t' "40/-\t\t"+ entry_colddrink.get() + "\n")
        icecream_float = entry_float.get()
        if int(icecream_float)!=0:
            txtReceipt.insert(END, 'Ice Cream Float\t\t' "50/-\t\t" + entry_float.get() + "\n")
        mojito = entry_mojito.get()
        if int(mojito)!=0:
            txtReceipt.insert(END, 'Mojito\t\t' "40/-\t\t" + entry_mojito.get() + "\n")
        icecream = entry_icecream.get()
        if int(icecream)!=0:
            txtReceipt.insert(END, 'Ice Cream\t\t' "40/-\t\t" + entry_icecream.get() + "\n")
        total = ((int(aloo_tikki_burger) * 30) + (int(veggie_burger) * 50) + (int(chicken_burger) * 70) + (
                    int(fries) * 40) + (int(chicken_popcorn) * 70) + (int(cold_coffee) * 50) + (
                             int(cold_drink) * 40) + (int(icecream_float) * 50) + (int(mojito) * 40) + (
                             int(icecream) * 40))
        txtReceipt.insert(END, "*************************************************")
        if str(total)!=0:
            txtReceipt.insert(END, 'Total Amount To Be Paid\t\t\t\t' + str(total) + "")
        txtReceipt.insert(END, "\n*************************************************")
        txtReceipt.insert(END, '\t\t\tTHANK YOU\t\t')
        txtReceipt.insert(END, '\t\t\tHOPE TO SEE U BACK SOON!!')
        txtReceipt.insert(END, "\n*************************************************")
        txtReceipt.insert(END, "\n*************************************************")


    global photo_paytm
    global photo_otherpayment
    top=Toplevel()
    top.title("CART")
    top.geometry("1500x800")
    frame = Frame(top, bg="#262525")
    frame.pack(fill="both")
    frame2 = Frame(top, bg="#262525")
    frame2.pack(fill="both")
    frame3 = Frame(top, bg="#262525")
    frame3.pack( fill="both",expand=True)
    # frame4 = Frame(top, bg="#262525")
    # frame4.pack(expand=True,fill="both")


    btn12 = Button(frame, border=0, text="BACK", bg="#262525", fg="gold", compound=TOP,font=("gill sans ultra bold condensed", 20),borderwidth=5,command=top.destroy)
    btn12.pack(side=LEFT, anchor="nw", padx=115, pady=30)
    btn13 = Button(frame, border=0, text="GENERATE BILL", bg="#262525", fg="gold", compound=TOP,font=("gill sans ultra bold condensed", 20),borderwidth=5,command=generate_bill)
    btn13.pack(side=RIGHT, anchor="nw", padx=30, pady=30)

    txtReceipt = Text(frame2, height=25, width=43, font=("comic sans ms", 10))
    txtReceipt.pack(side=RIGHT, padx=50, pady=0)

    Lbl_bill = Label(frame2, text="PAYMENT MODE",bg="#262525", fg="gold", font=("eras bold itc", 20))
    Lbl_bill.pack(side=TOP, anchor="nw", pady=0)

    image_paytm = Image.open("IMG_6959.jpg")
    photo_paytm = ImageTk.PhotoImage(image_paytm)

    btn_paytm = Button(frame2, image=photo_paytm,bg="#262525",fg="gold",borderwidth=5, text='scan the code'+"\n"+ 'to pay via paytm', compound=TOP,font=("eras bold itc", 14))

    btn_paytm.pack(side=LEFT, anchor="nw", padx=20, pady=30)

    image_otherpayment = Image.open("payment options.png")
    photo_otherpayment = ImageTk.PhotoImage(image_otherpayment)

    btn_otherpayment = Button(frame2, image=photo_otherpayment, text='visit the counter'+"\n"+ 'to pay using card'+"\n" 'or cash or for any other'+"\n"'order realted queries',
                       compound=TOP,font=("eras bold itc", 14),bg="#262525",fg="gold",borderwidth=5)

    btn_otherpayment.pack(side=LEFT, anchor="nw", padx=20, pady=30)


root = Tk()
root.title("MADHIT CAFE")
loginrow= Frame(root,bg="#262525")
loginrow.pack(fill = "both")

title_label = Label(loginrow,text ="PLACE YOUR ORDER",bg ="#262525",fg ="gold", padx= 600, pady =10, font=("eras bold itc",14))
title_label.pack(side=BOTTOM)

title_label = Label(loginrow,text ="MADHIT CAFE",bg ="gold",fg ="#262525", padx= 800, pady =10, font=("eras bold itc",30))
title_label.pack(side=BOTTOM,anchor="e")

btnlogin = Button(loginrow,text="ADMIN LOGIN",bg ="#262530",fg ="gold", compound=RIGHT, font=("gill sans ultra bold", 12),borderwidth=5, command=adlogin)
btnlogin.pack(side=TOP, anchor="e", padx=0, pady=0)

btnrow1 = Frame(root,bg="#262525")
btnrow1.pack(fill = "both")

btnrow2 = Frame(root,bg="#262525")
btnrow2.pack( fill = "both")

btnrow3 = Frame(root,bg="#262525")
btnrow3.pack(fill = "both")

btnrow4 = Frame(root,bg="#262525")
btnrow4.pack(fill = "both")

btnrow5 = Frame(root,bg="#262525")
btnrow5.pack(fill = "both",expand=True)

Lbl = Label(btnrow1,text="BURGERS",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=LEFT,anchor="nw")

Lbl = Label(btnrow1,text="SIDES",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=RIGHT,anchor="nw")

Lbl = Label(btnrow2,text="QUANTITY",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=LEFT,anchor="nw",pady=6)

Lbl = Label(btnrow3,text="BEVRAGES",bg = "#262525" , fg = "gold", font=("eras bold itc",16))
Lbl.pack(side=LEFT,anchor="nw",pady=15)

Lbl = Label(btnrow3, text="DESSERTS", bg="#262525", fg="gold", font=("eras bold itc", 16))
Lbl.pack(side=RIGHT, anchor="nw", pady=15)

Lbl = Label(btnrow4, text="QUANTITY", bg="#262525", fg="gold", font=("eras bold itc", 16))
Lbl.pack(side=LEFT, anchor="nw", pady=0)

for x in range(1):
    value1 = IntVar()
    entry_atburger = Entry(btnrow2, textvariable=value1,width=20)
    entry_atburger.pack(side=LEFT, anchor="nw", padx=8, pady=10)
    food_items.append(entry_atburger)

for x in range(1):
    value2 = IntVar()
    entry_vegburger= Entry(btnrow2, textvariable=value2,width=20)
    entry_vegburger.pack(side=LEFT, anchor="nw", padx=95, pady=10)
    food_items.append(entry_vegburger)

for x in range(1):
    value3 = IntVar()
    entry_chickenburger = Entry(btnrow2, textvariable=value3,width=20)
    entry_chickenburger.pack(side=LEFT, anchor="nw", padx=9, pady=10)
    food_items.append(entry_chickenburger)

for x in range(1):
    value4 = IntVar()
    entry_fries = Entry(btnrow2,textvariable=value4,width=20)
    entry_fries.pack(side=RIGHT, anchor="nw", padx=76, pady=10)
    food_items.append(entry_fries)

for x in range(1):
    value5 = IntVar()
    entry_chickenpopcorn = Entry(btnrow2, textvariable=value5,width=20)
    entry_chickenpopcorn.pack(side=RIGHT, anchor="nw", padx=11, pady=10)
    food_items.append(entry_chickenpopcorn)

for x in range(1):
    value6 = IntVar()
    entry_coldcoffee = Entry(btnrow4, textvariable=value6,width=20)
    entry_coldcoffee.pack(side=LEFT, anchor="nw", padx=13, pady=3)
    food_items.append(entry_coldcoffee)

for x in range(1):
    value7 = IntVar()
    entry_colddrink = Entry(btnrow4, textvariable=value7,width=20)
    entry_colddrink.pack(side=LEFT, anchor="nw", padx=73, pady=3)
    food_items.append(entry_colddrink)

for x in range(1):
    value8 = IntVar()
    entry_float = Entry(btnrow4, textvariable=value8,width=20)
    entry_float.pack(side=LEFT, anchor="nw", padx=11, pady=3)
    food_items.append(entry_float)

for x in range(1):
    value9 = IntVar()
    entry_mojito = Entry(btnrow4, textvariable=value9,width=20)
    entry_mojito.pack(side=LEFT, anchor="nw", padx=73, pady=3)
    food_items.append(entry_mojito)

for x in range(1):
    value10 = IntVar()
    entry_icecream = Entry(btnrow4, textvariable=value10, width=20)
    entry_icecream.pack(side=RIGHT, anchor="nw", padx=123, pady=3)
    food_items.append(entry_icecream)

def change(e):
    image = Image.open("clickme.jpg")
    photo = ImageTk.PhotoImage(image)
    btn.config(image=photo)
    btn.image=photo

def change_back(e):
    image = Image.open("aloo tiki burger.jpg")
    photo = ImageTk.PhotoImage(image)
    btn.config(image=photo)
    btn.image = photo

image = Image.open("aloo tiki burger.jpg")
photo = ImageTk.PhotoImage(image)

btn = Button(btnrow1,image=photo,text="Aloo Tiki Burger: 30/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked)

btn.pack(side=LEFT,anchor="nw",padx=20,pady=10)

btn.bind("<Enter>", change)
btn.bind("<Leave>", change_back)

def change2(e2):
    image2 = Image.open("clickme.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    btn2.config(image=photo2)
    btn2.image2=photo2

def change_back2(e2):
    image2 = Image.open("veggie burger.jpg")
    photo2 = ImageTk.PhotoImage(image2)
    btn2.config(image=photo2)
    btn2.image2 = photo2

image2 = Image.open("veggie burger.jpg")
photo2 = ImageTk.PhotoImage(image2)

btn2 = Button(btnrow1,image=photo2,text="Veggie Burger: 50/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked2)

btn2.pack(side=LEFT,anchor="nw",padx=20,pady=10)

btn2.bind("<Enter>", change2)
btn2.bind("<Leave>", change_back2)

def change3(e3):
    image3 = Image.open("clickme.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    btn3.config(image=photo3)
    btn3.image3=photo3

def change_back3(e3):
    image3 = Image.open("chicken burger.jpg")
    photo3 = ImageTk.PhotoImage(image3)
    btn3.config(image=photo3)
    btn3.image3 = photo3


image3 = Image.open("chicken burger.jpg")
photo3 = ImageTk.PhotoImage(image3)

btn3 = Button(btnrow1,image=photo3,text="Chicken Burger: 70/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked3)

btn3.pack(side=LEFT,anchor="nw",padx=20,pady=10)

btn3.bind("<Enter>", change3)
btn3.bind("<Leave>", change_back3)

def change4(e4):
    image4 = Image.open("clickme.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    btn4.config(image=photo4)
    btn4.image4=photo4

def change_back4(e4):
    image4 = Image.open("fries.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    btn4.config(image=photo4)
    btn4.image4 = photo4


image4 = Image.open("fries.jpg")
photo4 = ImageTk.PhotoImage(image4)

btn4 = Button(btnrow1,image=photo4,text="Fries: 40/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked4)

btn4.pack(side=RIGHT,anchor="nw",padx=10,pady=10)

btn4.bind("<Enter>", change4)
btn4.bind("<Leave>", change_back4)

def change5(e5):
    image5 = Image.open("clickme.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    btn5.config(image=photo5)
    btn5.image5=photo5

def change_back5(e5):
    image5 = Image.open("chicken popcorn.jpg")
    photo5 = ImageTk.PhotoImage(image5)
    btn5.config(image=photo5)
    btn5.image5 = photo5


image5 = Image.open("chicken popcorn.jpg")
photo5 = ImageTk.PhotoImage(image5)

btn5 = Button(btnrow1,image=photo5,text="Chicken Popcorn: 70/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked5)

btn5.pack(side=RIGHT,anchor="nw",padx=10,pady=10)

btn5.bind("<Enter>", change5)
btn5.bind("<Leave>", change_back5)

def change6(e6):
    image6 = Image.open("clickme.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    btn6.config(image=photo6)
    btn6.image6=photo6

def change_back6(e6):
    image6 = Image.open("cold coffee.jpg")
    photo6 = ImageTk.PhotoImage(image6)
    btn6.config(image=photo6)
    btn6.image6 = photo6


image6 = Image.open("cold coffee.jpg")
photo6 = ImageTk.PhotoImage(image6)

btn6 = Button(btnrow3,image=photo6,text="Cold Coffee: 50/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked6)

btn6.pack(side=LEFT,anchor="nw",padx=10,pady=25)

btn6.bind("<Enter>", change6)
btn6.bind("<Leave>", change_back6)

def change7(e7):
    image7 = Image.open("clickme.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    btn7.config(image=photo7)
    btn7.image7=photo7

def change_back7(e7):
    image7 = Image.open("cold drinks.jpg")
    photo7 = ImageTk.PhotoImage(image7)
    btn7.config(image=photo7)
    btn7.image7 = photo7

image7 = Image.open("cold drinks.jpg")
photo7 = ImageTk.PhotoImage(image7)

btn7 = Button(btnrow3,image=photo7,text="Cold Drinks: 40/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked7)

btn7.pack(side=LEFT,anchor="nw",padx=10,pady=25)

btn7.bind("<Enter>", change7)
btn7.bind("<Leave>", change_back7)


def change8(e8):
    image8 = Image.open("clickme.jpg")
    photo8 = ImageTk.PhotoImage(image8)
    btn8.config(image=photo8)
    btn8.image8=photo8

def change_back8(e8):
    image8 = Image.open("float.jpg")
    photo8 = ImageTk.PhotoImage(image8)
    btn8.config(image=photo8)
    btn8.image8 = photo8

image8 = Image.open("float.jpg")
photo8 = ImageTk.PhotoImage(image8)

btn8 = Button(btnrow3,image=photo8,text="Ice Cream Float: 50/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked8)

btn8.pack(side=LEFT,anchor="nw",padx=10,pady=25)

btn8.bind("<Enter>", change8)
btn8.bind("<Leave>", change_back8)

def change9(e9):
    image9 = Image.open("clickme.jpg")
    photo9 = ImageTk.PhotoImage(image9)
    btn9.config(image=photo9)
    btn9.image9=photo9

def change_back9(e9):
    image9 = Image.open("mo.jpg")
    photo9 = ImageTk.PhotoImage(image9)
    btn9.config(image=photo9)
    btn9.image9 = photo9

image9 = Image.open("mo.jpg")
photo9 = ImageTk.PhotoImage(image9)

btn9 = Button(btnrow3,image=photo9,text="Mojito: 40/-",compound=TOP, font=("gill sans ultra bold",10),command=btn_is_clicked9)

btn9.pack(side=LEFT,anchor="nw",padx=10,pady=25)


btn9.bind("<Enter>", change9)
btn9.bind("<Leave>", change_back9)

def change10(e10):
    image10 = Image.open("clickme.jpg")
    photo10 = ImageTk.PhotoImage(image10)
    btn10.config(image=photo10)
    btn10.image10=photo10

def change_back10(e10):
    image10 = Image.open("ice cream.jpg")
    photo10 = ImageTk.PhotoImage(image10)
    btn10.config(image=photo10)
    btn10.image10 = photo10

image10 = Image.open("ice cream.jpg")
photo10 = ImageTk.PhotoImage(image10)

btn10 = Button(btnrow3, image=photo10, text="Ice Cream: 40/-", compound=TOP, font=("gill sans ultra bold", 10), command=btn_is_clicked10)

btn10.pack(side=RIGHT, anchor="nw", padx=10, pady=25)

btn10.bind("<Enter>", change10)
btn10.bind("<Leave>", change_back10)

# image11 = Image.open("cort.jpg")
# photo11 = ImageTk.PhotoImage(image11)

btn11 = Button(btnrow5,border=0,text="VIEW CART",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=view_cart)

btn11.pack(side=RIGHT,anchor="nw",padx=30,pady=30)

# imageexit = Image.open("exit(1).png")
# photoexit = ImageTk.PhotoImage(imageexit)
# exitbtn = Button(btnrow5,border=0,text="EXIT",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=root.destroy)
#
# exitbtn.pack(side=RIGHT,anchor="nw",padx=0,pady=30)

total_btn = Button(btnrow5,border=0,width=10,height=0,text="TOTAL BILL",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=calculate_bill)

total_btn.pack(side=LEFT,anchor="center",padx=20,pady=30)


# imagereset = Image.open("trash(1).png")
# photoreset = ImageTk.PhotoImage(imagereset)
resetbtn = Button(btnrow5,border=0,text="CLEAR",bg="#262525",fg="gold",compound=TOP,font=("gill sans ultra bold condensed",20),borderwidth=5,command=clear_entry)

resetbtn.pack(side=RIGHT,anchor="nw",padx=10,pady=30)

root.mainloop()