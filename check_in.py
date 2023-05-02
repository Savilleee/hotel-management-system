#all modules needed
from tkinter import *
from subprocess import call

#function to print the bill whem pressed print button 
def print_bill():
    import csv
    import random
    if dul.get()==1:
        room="DELUXE"
        day_stay=e5.get()
        total=int(day_stay)*2500
    elif ultdul.get()==1:
        room="ULTRA DELUXE"
        day_stay=e5.get()
        total=int(day_stay)*3000
    elif gen.get()==1:
        room="GENERAL"
        day_stay=e5.get()
        total=int(day_stay)*2000
    elif suite.get()==1:
        room="EXECUTIVE SUITE"
        day_stay=e5.get()
        total=int(day_stay)*5000

        
    if paycash.get()==1:
        payment="Cash/Check"
    elif paycard.get()==1:
        payment="Credit Card/Debit Card"
    name=e1.get()
    address=e2.get()
    phone_no=int(e3.get())
    email_id=e4.get()
    bill_no=random.randint(898464,946523)
    # Open a file for writing
    with open("output.txt", "w") as f:
        # Write the output to the file
        f.write("#####################    WELCOME TO ITALIONIC HOTEL   #####################\n")
        f.write("                   "+name + "'s BILL\n")
        f.write(" \n                        BILL NO." + str(bill_no))
        f.write("   \n              COSTUMER'S NAME     :" + name)
        f.write("   \n              COSTUMER'S PHONE NO. :" + str(phone_no))
        f.write("   \n              COSTUMER'S EMAIL_ID  :" + email_id)
        f.write("    \n             COSTUMER'S ADDRESS   :" + address)
        f.write("     \n            COSTUMER'S ROOM TYPE :" + room)
        f.write("     \n            BILL PAYMENT METHOD  :" + payment)
        f.write("      \n             TOTAL BILL         :" + str(total) + "appox.")
        f.write("\n##################### THANK YOU !!! VISIT US AGIAN ########################")


#function to get all the data from the user to import into the files 
def get_data():
    import csv
    import random
    gs=[]
    f=open("guest_list.csv","a")
    file=open("gueat_list_all.csv","a")
    if dul.get()==1:
        room_type="DELUXE"
        day_stay=e5.get()
        total=int(day_stay)*2500
    elif ultdul.get()==1:
        room_type="ULTRA DELUXE"
        day_stay=e5.get()
        total=int(day_stay)*3000
    elif gen.get()==1:
        room_type="GENERAL"
        day_stay=e5.get()
        total=int(day_stay)*2000
    elif suite.get()==1:
        room_type="EXECUTIVE SUITE"
        day_stay=e5.get()
        total=int(day_stay)*5000


        
    if paycash.get()==1:
        payment="Cash/Check"
    elif paycard.get()==1:
        payment="Credit Card/Debit Card"
    name=e1.get()
    address=e2.get()
    phone_no=int(e3.get())
    email_id=e4.get()
    room_no=random.randint(1,250)
    
    from datetime import datetime
    from datetime import date

    today=date.today()
    d1=today.strftime("%d/%m/%Y")
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")

    #write all data to csv file 
    gst=csv.writer(f)
    gst.writerow([name,address,phone_no,email_id,room_no,room_type,payment,total,d1,current_time])
    gst_main=csv.writer(file)
    gst_main.writerow([name,address,phone_no,email_id,room_no,room_type,payment,total,d1,current_time])
    f.close()
    file.close()

    #display all data that is given by the user 
    label17=Label(root,text="(data updated as :)",font="times 15 bold")
    label17.place(x=50,y=485)
    
    label10=Label(root,text="COSTOMER's ROOM NO  :",font="times 18 bold")
    label10.place(x=50,y=510)
    
    label11=Label(root,text=room_no,font="times 18 bold")
    label11.place(x=400,y=510)

    label12=Label(root,text="COSTUMER'S NAME     :",font="times 18 bold")
    label12.place(x=50,y=540)

    label13=Label(root,text=name,font="times 18 bold")
    label13.place(x=400,y=540)

    label14=Label(root,text="COSTOMER'S ADDRESS  :",font="times 18 bold")
    label14.place(x=50,y=570)

    label15=Label(root,text=address,font="times 18 bold")
    label15.place(x=400,y=570)

    label16=Label(root,text="COSTOMER'S PHONE_NO :",font="times 18 bold")
    label16.place(x=50,y=600)

    label17=Label(root,text=phone_no,font="times 18 bold")
    label17.place(x=400,y=600)

    label18=Label(root,text="ROOM TYPE :",font="times 18 bold")
    label18.place(x=50,y=630)

    label19=Label(root,text=room_type,font="times 18 bold")
    label19.place(x=400,y=630)

    label20=Label(root,text="PAYMENT METHOD  :",font="times 18 bold")
    label20.place(x=50,y=660)

    label21=Label(root,text=payment,font="times 18 bold")
    label21.place(x=400,y=660)
    
#base for tkinter window 
root=Tk()
root.title("CHECK IN DETAILS")
root.geometry("1050x700")
root.iconbitmap(r"C:\Users\Max Gonsalves\max\hmsfinalproject\hotel.ico")

label1=Label(root,text="YOU CHOICE WAS :   CHECK_IN",font="times 30 bold")
label1.place(x=180,y=10)

label=Label(root,text="------------------------------------------------------------------------------------------------------------------------",font="times 25 bold")
label.place(x=0,y=50)

#for entering name 
label2=Label(root,text="ENTER YOU NAME               :",font="times 20 bold")
label2.place(x=50,y=90)

e1=Entry(root, width=35,font="times 18 bold")
e1.place(x=450,y=90)

#for entering address 
label3=Label(root,text="ENTER YOUR ADDRESS      :",font="times 20 bold")
label3.place(x=50,y=130)

e2=Entry(root, width=35,font="times 18 bold")
e2.place(x=450,y=130)

#for enterning phone number
label4=Label(root,text="ENTER YOUR PHONE NO.   :",font="times 20 bold")
label4.place(x=50,y=170)

e3=Entry(root, width=35,font="times 18 bold")
e3.place(x=450,y=170)

#for entering email_id
label_email=Label(root,text="ENTER EMAIL_ID                  :",font="times 20 bold")
label_email.place(x=50,y=210)

e4=Entry(root,width=35,font="times 18 bold")
e4.place(x=450,y=210)

#line divider 1
label_divider=Label(root,text="------------------------------------------------------------------------------------------------------------------------------------------------------------------",font="times 18 bold")
label_divider.place(x=0,y=250)

#room choice for the customer 
label5=Label(root,text="CHOOSE YOUR ROOM :",font="times 20 bold")
label5.place(x=50,y=280)

dul= IntVar()
label6=Checkbutton(root,text="DULUXE",font="times 18 bold",variable=dul)
label6.place(x=50,y=330)

ultdul=IntVar()
label7=Checkbutton(root,text="ULTRA DULUXE",font="times 18 bold",variable=ultdul)
label7.place(x=210,y=330)

gen=IntVar()
label8=Checkbutton(root,text="GENERAL",font="times 18 bold",variable=gen)
label8.place(x=50,y=380)

suite=IntVar()
label9=Checkbutton(root,text="EXECUTIVE SUITE",font="times 18 bold",variable=suite)
label9.place(x=210,y=380)

#line divider 2
label_line=Label(root,text='''                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |''',font="times 14 bold")
label_line.place(x=460,y=270)

label16=Label(root,text="----------------------------------------------------------------------------------------------------------------------------------------------------",font="times 20 bold")
label16.place(x=0,y=420)

#payment choice

label16=Label(root,text="PAYMENT METHOD :",font="times 20 bold")
label16.place(x=650,y=290)

paycash=IntVar()
label17=Checkbutton(root,text="CASH/CHECK",font="times 18 bold",variable=paycash)
label17.place(x=650,y=330)

paycard=IntVar()
label18=Checkbutton(root,text="CREDIT CARD/DEBIT CARD",font="times 18 bold",variable=paycard)
label18.place(x=650,y=380)


#days of stay
stay=Label(root,text="NO. OF DAYS WANT TO STAY :",font="times 20 bold")
stay.place(x=40,y=450)
e5=Entry(root,width=25,font="times 18 bold")
e5.place(x=460,y=455)
         

#button for getting all the data and calling the function getdata() 
button1=Button(root,text="OK",font="times 15 bold" , command=get_data,padx=25 ,pady=50)
button1.place(x=890,y=110)

#billbutton for printing the bill by calling function print_bill()
button2=Button(root,text=" PRINT BILL",font="times 15 bold",padx=25 ,pady=50,command=print_bill)
button2.place(x=790,y=520)
root.mainloop()



