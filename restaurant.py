from tkinter import *
from subprocess import call
def total_bill():
    tea=e1.get()
    breakfast=e2.get()
    lunch=e3.get()
    dinner=e4.get()
    total=((int(tea)*50)+(int(breakfast)*300)+(int(lunch)*400)+(int(dinner)*500))
    #print(total)
    label20=Label(text="YOUR TOTAL BILL IS Rs:",font="times 30 bold")
    label20.place(x=100,y=350)
    labelmain=Label(root,text=total,font="times 30 bold")
    labelmain.place(x=600,y=350)


root=Tk()
root.geometry("900x500")
root.title("resturent")
root.iconbitmap("/Users/savilledsilva/Downloads/hotel_management_system-main/hotel.ico")
labelmain=Label(root,text='   ITALINOIC  RESTAURENT ',font="times 30 bold")
labelmain.place(x=500,y=20,anchor="center")
#------------menu card ---------

label1=Label(root,text="MENU",font="Courier 35 bold")
label1.place(x=600,y=70)


label2=Label(root,text="Tea        | RS=50",font="Courier 20 bold")
label2.place(x=500,y=140)


label3=Label(root,text="Coffee     | RS=50",font="Courier 20 bold")
label3.place(x=500,y=170)


label3=Label(root,text="Breakfast  | RS=300",font="Courier 20 bold")
label3.place(x=500,y=200)


label4=Label(root,text="Lunch      | RS=400",font="Courier 20 bold")
label4.place(x=500,y=230)


label5=Label(root,text="Dinner     | RS=500",font="Courier 20 bold")
label5.place(x=500,y=260)




#----------billling system--------
label7=Label(root,text="Enter the number of items ",font="times 20 bold")
label7.place(x=70,y=70)

label8=Label(root,text="Tea/Coffee : ",font="times 20 bold")
label8.place(x=20,y=120)

e1=Entry(root,font="times 15 bold")
e1.place(x=20,y=150)

label9=Label(root,text="Breakfast :  ",font="times 20 bold")
label9.place(x=250,y=120)

e2=Entry(root,font="times 15 bold")
e2.place(x=250,y=150)

label10=Label(root,text="Lunch : ",font="times 20 bold")
label10.place(x=20,y=180)

e3=Entry(root,font="times 15 bold")
e3.place(x=20,y=210)

label9=Label(root,text="Dinner : ",font="times 20 bold")
label9.place(x=250,y=180)

e4=Entry(root,font="times 15 bold")
e4.place(x=250,y=210)

bill=Button(text="Total Bill",font="times 25 bold",bg='red',command=total_bill )
bill.place(x=120,y=250)


root.mainloop()
