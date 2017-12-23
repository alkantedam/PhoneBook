from tkinter import *

def delete():
	index = contacts.curselection()[0]
	contacts.delete(index)

def add():
	name = entry_name.get()
	phone = entry_phone.get()
	if name == "" or phone == "":
		error.config(text = "Field are empty")
	else:
		contacts.insert(END, name + " - " + phone)
		entry_name.delete(0, END)
		entry_phone.delete(0, END)
		error.config(text = "")

def edit():
	index = contacts.curselection()[0]
	name = entry_name.get()
	phone = entry_phone.get()

	if name == "" or phone == "":
		error.config(text = "Field are empty")
	else:
		contacts.delete(index)
		contacts.insert(index, name + " - " + phone)
		entry_name.delete(0, END)
		entry_phone.delete(0, END)

wn = Tk()
wn.title('Phone Book')
wn.geometry('330x500')

frame1= Frame(wn)
frame1.pack()

label_name = Label(frame1, text = "Name")
label_name.grid(row = 0, column = 0)

entry_name = Entry(frame1)
entry_name.grid(row=0, column = 1)

label_phone = Label(frame1, text = "Telephone")
label_phone.grid(row = 1, column = 0)

entry_phone = Entry(frame1)
entry_phone.grid(row=1, column = 1)

frame2 = Frame(wn)
frame2.pack()

btn_add = Button(frame2, text = "Add button", command = add)
btn_add.grid(row = 0, column = 1)

btn_del = Button(frame2, text = "Delete button", command = delete)
btn_del.grid(row = 0, column = 2)

btn_edit = Button(frame2, text = "Edit button", command = edit)
btn_edit.grid(row = 0, column = 3)

frame3 = Frame(wn)
frame3.pack()

error = Label(frame3, text = "", fg = "red")
error.pack()

scroll = Scrollbar(frame3)
scroll.pack(side = RIGHT)

contacts = Listbox(frame3, yscrollcommand = scroll.set)
scroll.config(command = contacts.yview)
contacts.pack()

contacts.insert(END, 'Alina', 'Bill', 'Dasha')

wn.mainloop()