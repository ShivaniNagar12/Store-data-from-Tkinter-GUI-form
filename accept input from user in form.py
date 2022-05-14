#how to use checkbox , take input from user
from tkinter import *
root = Tk()
def getvals():
    print("Submitting Form")
    #logic of the submission
    #namevalue.set() #to set the value
    #namevalue.get() #to get the value, print
    print(f"{namevalue.get() ,gendervalue.get(), phonevalue.get(), emailvalue.get(),paymentvalue.get(), foodservicevalue.get()} ")

#a- append mode , it'll added all words
    with open ("E:/Minor project 1/Tkinter GUI 1/form data store in file/records.txt", "a") as f: #open a file in write mode
        f.write(f"{namevalue.get() ,gendervalue.get(), phonevalue.get(), emailvalue.get(),paymentvalue.get(), foodservicevalue.get()}\n")

root.geometry("644x344")
Label(root, text="Welcome to the shivani travel ", font="itali 13 bold", pady=15, bg="red",relief=SUNKEN).grid(row=0, column=3)

#entry widget, text for our form
name = Label(root, text="Name")
gender = Label(root, text="Gender")
phone = Label(root, text= "Phone")
email = Label(root, text="Email")
payment = Label(root, text="Payment Mode")

#pack text for our form
name.grid(row=1, column=2)
gender.grid(row=2, column=2)
phone.grid(row=3, column=2)
email.grid(row=4, column=2)
payment.grid(row=5, column=2)

#Tkinter variables for storing entries
namevalue = StringVar()
gendervalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
paymentvalue = StringVar()
#checkbox , maybe 0 or 1
foodservicevalue = IntVar()

#to make entries for our form
nameentry = Entry(root , textvariable=namevalue)
genderentry = Entry(root , textvariable=gendervalue)
phoneentry = Entry(root , textvariable=phonevalue)
emailentry = Entry(root , textvariable=emailvalue)
paymententry = Entry(root , textvariable=paymentvalue)

#make entry class, checkbox , button
#packing entries
nameentry.grid(row=1, column=3)
genderentry.grid(row=2, column=3)
phoneentry.grid(row=3, column=3)
emailentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

#checkbox adding and packing it, checkbutton
foodservice = Checkbutton(text="Want to prebook your meal?????", variable=foodservicevalue)
foodservice.grid(row=6, column=3, pady=7)

#adding button and packing it

Button(text="SUBMIT", command=getvals).grid(row=7, column=3)   #functions getvals, lets create a def vals



root.mainloop()