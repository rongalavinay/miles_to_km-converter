import tkinter

window=tkinter.Tk()
window.title('miles to km converter')
window.config(padx=50,pady=50)

# labels

label2=tkinter.Label(text='Miles')
label2.grid(column=2,row=0)

label3=tkinter.Label(text='is equal to')
label3.grid(column=0,row=1)

label4=tkinter.Label(text='KM')
label4.grid(column=2,row=1)

km=tkinter.Label(text='0')
km.grid(column=1,row=1)

# entry

input1=tkinter.Entry(width=10)
input1.grid(column=1,row=0)
input1.get()


# button
def button_clicked():
    miles=input1.get()
    kms=float(miles)*1.6
    km.config(text=f'{kms}')
button=tkinter.Button(text='Calculate',command=button_clicked)
button.grid(column=1,row=2)

window.mainloop()