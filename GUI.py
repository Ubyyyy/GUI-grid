from tkinter import*

window = Tk()

titleLabel = Label(window,text="Sign in",font=("Arial",15)).grid(row=0,column=0,columnspan=2)

firstNameLabel = Label(window,text="First name: ",width=15).grid(row=1,column=0)
fisrtNameEntry = Entry(window).grid(row=1,column=1)

lastNameLabel = Label(window,text="Last name: ",width=15).grid(row=2,column=0)
lastNameEntry = Entry(window).grid(row=2,column=1)

emailNameLabel = Label(window,text="Email: ",width=15).grid(row=3,column=0)
emailNameEntry = Entry(window).grid(row=2,column=1)

submitButton = Button(window,text="Submit").grid(row=4,column=0,columnspan=2)

window.mainloop()