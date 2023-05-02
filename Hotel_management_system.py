#all modules needed imported 
from tkinter import *
from subprocess import call

#all the functions to call program based on choice 
def check_in_call():
    call(["python","/Users/savilledsilva/Downloads/hotel_management_system-main/check_in.py"])
def check_out_call():
    call(["python","/Users/savilledsilva/Downloads/hotel_management_system-main/check_out.py"])
def restaurent_call():
    call(["python","Users/savilledsilva/Downloads/hotel_management_system-main/restaurant.py"])
def guest_list():
    call(["python","/Users/savilledsilva/Downloads/hotel_management_system-main/show_guest_list.py"])

#basic defination of tkinter window
root = Tk()
root.title("Hotel Mangement System")
root.iconbitmap("/Users/savilledsilva/Downloads/hotel_management_system-main/hotel.ico")
root.geometry("650x650")

#Topmost label
myLabel= Label(root,text="WELCOME TO HOTEL MANGEMENT SYSTEM !!!",font="Courier 20 bold")
myLabel.pack()

#Check in button
mybutton = Button(root,text="1. CHECK INN", padx=91, pady=30,bg='blue', fg='white',font="Courier 20 bold",command=check_in_call)
mybutton.pack()

#show all the guest list button
mybutton2 = Button(root,text="2. SHOW GUEST LIST",padx=43, pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=guest_list)
mybutton2.pack()

#function call to check out the guest 
mybutton3= Button(root,text= "3. CHECK OUT",padx=91, pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=check_out_call)
mybutton3.pack()

#restaurent button
mybutton5=Button(root,text="5 . RESTAURENT",padx=75,pady=30,bg='navy blue', fg='white',font="Courier 20 bold",command=restaurent_call)
mybutton5.pack()

#exit button 
mybutton6= Button(root,text= "5. EXIT",padx=130, pady=30 ,bg='navy blue', fg='white',font="Courier 20 bold",command=root.destroy)
mybutton6.pack()

#infinite loop for GUI to work 
root.mainloop()
