from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x8000")
root.configure(bg='#808080')
root.title("Restaurant Management System")

rand = StringVar()
Fries = StringVar()
Noodles = StringVar()
Soup = StringVar()
SubTotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Soft_Drinks = StringVar()
Tax = StringVar()
Cost = IntVar()
Burger = StringVar()
Sandwich = StringVar()



# ToDO Menu
def Menu():

    x = random.randint(10908, 500876)
    randomRef = str(x)
    rand.set(randomRef)

    # ToDO File - Data.txt
    file = open("MyData.txt", "at")

    if (Fries.get() == ""):
        CoFries = 0
    else:
        CoFries = float(Fries.get())

    if (Noodles.get() == ""):
        CoNoodles = 0
    else:
        CoNoodles = float(Noodles.get())

    if (Soup.get() == ""):
        CoSoup = 0
    else:
        CoSoup = float(Soup.get())

    if (Burger.get() == ""):
        CoBurger = 0
    else:
        CoBurger = float(Burger.get())

    if (Sandwich.get() == ""):
        CoSandwich = 0
    else:
        CoSandwich = float(Sandwich.get())

    if (Soft_Drinks.get() == ""):
        CoD = 0
    else:
        CoD = float(Soft_Drinks.get())

    CostofFries = CoFries * 140
    CostofDrinks = CoD * 65
    CostofNoodles = CoNoodles * 90
    CostofSoup = CoSoup * 140
    CostBurger = CoBurger * 260
    CostSandwich = CoSandwich * 300

    CostofMeal = "Rs.", str('%.2f' % (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich))

    PayTax = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) * 0.2)

    TotalCost = (CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich)

    Ser_Charge = ((CostofFries + CostofDrinks + CostofNoodles + CostofSoup + CostBurger + CostSandwich) / 99)

    Service = "Rs.", str('%.2f' % Ser_Charge)

    OverAllCost = "Rs.", str('%.2f' % (PayTax + TotalCost + Ser_Charge))
    to = str(OverAllCost)
    PaidTax = "Rs.", str('%.2f' % PayTax)
    file.write(to)
    Service_Charge.set(Service)
    Cost.set(CostofMeal)
    Tax.set(PaidTax)
    SubTotal.set(CostofMeal)
    Total.set(OverAllCost)
    file.write(CostofMeal)
    file.close()
    file.close()


# ToDO Reset Value
def Reset():
    rand.set("")
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Soft_Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")


# ToDO Exit System
def Window_Exit():
    root.destroy()


if __name__ == '__main__':

    # ToDO For hostel detail
    Tops = Frame(root, width=1600, relief=SUNKEN)
    Tops.pack(side=TOP)

    # ToDO Frame create
    frame = Frame(root, width=800, height=700, relief=SUNKEN)
    frame.pack(side=LEFT)

    # ToDO local time
    localtime = time.asctime(time.localtime(time.time()))

    # ToDO Title
    lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="5 Star Hotel", fg="Black", bd=10, anchor='w')
    lblInfo.grid(row=0, column=0)
    lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, fg="Steel Blue", bd=10, anchor='w')
    lblInfo.grid(row=1, column=0)

    # ToDO Refrence
    lblReference = Label(frame, font=('arial', 16, 'bold'), text="Reference ID", bd=16, anchor="w")
    lblReference.grid(row=1, column=0)
    txtReference = Entry(frame, font=('arial', 16, 'bold'), textvariable=rand, bd=10, insertwidth=4, bg="yellow",  justify='right')
    txtReference.grid(row=1, column=1)

    # ToDO Fries
    lbl_Fries = Label(frame, font=('arial', 16, 'bold'), text="Fries", bd=16, anchor="w")
    lbl_Fries.grid(row=2, column=0)
    txt_Fries = Entry(frame, font=('arial', 16, 'bold'), textvariable=Fries, bd=10, insertwidth=4, bg="#ffffff",  justify='right')
    txt_Fries.grid(row=2, column=1)

    # ToDO Noodles
    lbl_Noodles = Label(frame, font=('arial', 16, 'bold'), text="Noodles", bd=16, anchor="w")
    lbl_Noodles.grid(row=3, column=0)
    txt_Noodles = Entry(frame, font=('arial', 16, 'bold'), textvariable=Noodles, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_Noodles.grid(row=3, column=1)

    # ToDO Soup
    lbl_Soup = Label(frame, font=('arial', 16, 'bold'), text="Soup", bd=16, anchor="w")
    lbl_Soup.grid(row=4, column=0)
    txt_Soup = Entry(frame, font=('arial', 16, 'bold'), textvariable=Soup, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_Soup.grid(row=4, column=1)

    # ToDO Burger
    lbl_Burger = Label(frame, font=('arial', 16, 'bold'), text="Burger", bd=16, anchor="w")
    lbl_Burger.grid(row=5, column=0)
    txt_Burger = Entry(frame, font=('arial', 16, 'bold'), textvariable=Burger, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_Burger.grid(row=5, column=1)

    # ToDO Sandwich
    lbl_Sandwich = Label(frame, font=('arial', 16, 'bold'), text="Sandwich", bd=16, anchor="w")
    lbl_Sandwich.grid(row=6, column=0)
    txt_Sandwich = Entry(frame, font=('arial', 16, 'bold'), textvariable=Sandwich, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_Sandwich.grid(row=6, column=1)

    # ToDO Soft Drink
    lbl_Drinks = Label(frame, font=('arial', 16, 'bold'), text="Soft Drinks", bd=16, anchor="w")
    lbl_Drinks.grid(row=1, column=2)
    txt_Drinks = Entry(frame, font=('arial', 16, 'bold'), textvariable=Soft_Drinks, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_Drinks.grid(row=1, column=3)

    # ToDO meal cost
    lbl_Cost = Label(frame, font=('arial', 16, 'bold'), text="Cost of Meal", bd=16, anchor="w")
    lbl_Cost.grid(row=2, column=2)
    txt_Cost = Entry(frame, font=('arial', 16, 'bold'), textvariable=Cost, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_Cost.grid(row=2, column=3)

    # ToDO Service charge
    lbl_Service = Label(frame, font=('arial', 16, 'bold'), text="Service Charge", bd=16, anchor="w")
    lbl_Service.grid(row=3, column=2)
    txt_Service = Entry(frame, font=('arial', 16, 'bold'), textvariable=Service_Charge, bd=10, insertwidth=4,  bg="#ffffff",  justify='right')
    txt_Service.grid(row=3, column=3)

    # ToDO State Txt
    lbl_StateTax = Label(frame, font=('arial', 16, 'bold'), text="GST txt", bd=16, anchor="w")
    lbl_StateTax.grid(row=4, column=2)
    txt_StateTax = Entry(frame, font=('arial', 16, 'bold'), textvariable=Tax, bd=10, insertwidth=4, bg="#ffffff",  justify='right')
    txt_StateTax.grid(row=4, column=3)

    # ToDO SubTotal
    lbl_SubTotal = Label(frame, font=('arial', 16, 'bold'), text="Sub Total", bd=16, anchor="w")
    lbl_SubTotal.grid(row=5, column=2)
    txt_SubTotal = Entry(frame, font=('arial', 16, 'bold'), textvariable=SubTotal, bd=10, insertwidth=4, bg="#ffffff",  justify='right')
    txt_SubTotal.grid(row=5, column=3)

    # ToDO Cost
    lbl_TotalCost = Label(frame, font=('arial', 16, 'bold'), text="Total Cost", bd=16, anchor="w")
    lbl_TotalCost.grid(row=6, column=2)
    txt_TotalCost = Entry(frame, font=('arial', 16, 'bold'), textvariable=Total, bd=10, insertwidth=4, bg="#ffffff", justify='right')
    txt_TotalCost.grid(row=6, column=3)

    #ToDO buttount Total
    btn_Total = Button(frame, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=6, text="Total", bg="powder blue", command=Menu).grid(row=8, column=1)
    # ToDO buttount Reset
    btn_Reset = Button(frame, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=6, text="Reset",  bg="powder blue", command=Reset).grid(row=8, column=2)
    # ToDO buttount Exit
    btn_Exit = Button(frame, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=6, text="Exit",   bg="powder blue", command=Window_Exit).grid(row=8, column=3)

root.mainloop()


