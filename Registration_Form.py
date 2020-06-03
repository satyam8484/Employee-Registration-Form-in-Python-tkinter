from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter
import os
import random


def Clear():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    number_entry.delete(0, END)
    mail_entry.delete(0, END)
    v.set(0)


def quit_win():
    bl = messagebox.askquestion("Question", "Do you want to quit")
    if (bl == 'yes'):
        window.quit()


def insert_data():
    fw = open("Registration_Information.txt", 'a')
    name = name_entry.get()

    age = age_entry.get()
    if (not (age.isnumeric() and (int(age) in range(1, 100)))):
        messagebox.showerror("Error", 'Please enter a Valid Age')
        raise Exception("Please enter a Valid Age")

    gen_val = v.get()

    gender = ''
    if gen_val == 1:
        gender = 'male'
    else:
        gender = 'female'

    ph_no = number_entry.get()
    if (not (ph_no.isnumeric() and len(ph_no) == 10)):
        messagebox.showerror("Error", 'Please enter a Valid Number')
        raise Exception("Please enter a Valid Number")

    mail = mail_entry.get()
    if (not ("@" in mail)):
        messagebox.showerror("Error", 'Please enter a Valid Mail Id')
        raise Exception("Please Enter Valid Mail Id")

    out_line = name + "\t" + age + "\t" + gender + "\t" + ph_no + "\t" + mail + "\n"
    fw.write(out_line)
    fw.close()
    messagebox.showinfo("Congratulation", 'Record Inserted Successfully')


def Insert_Data():
    flag = 0

    try:
        fr = open("Registration_Information.txt", 'r')
        email_set = set()
        for line in fr:
            email_str = line.split("\t")[4]
            email_set.add(email_str.strip())

        if (mail_entry.get() in email_set):
            flag = 1

        fr.close()
    except Exception as e:
        print(e)

    if flag == 1:
        messagebox.showerror("Error", "User Already Exists")
    else:
        insert_data()


window = tkinter.Tk()
# window.geometry('500x300')
window.resizable(0, 0)
window.title('Employee Registration Form')
window.iconbitmap(r'icon.ico')

## Create a Labels

name_label = ttk.Label(text='Name :')
age_label = ttk.Label(text='Age :')
gender_label = ttk.Label(text='Gender :')
number_label = ttk.Label(text='Phone Number :')
mail_label = ttk.Label(text='Email id :')

val_x = 0
val_y = 5

name_label.grid(row=0, column=1, sticky=W, pady=val_y, padx=val_x)
age_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
gender_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
number_label.grid(row=4, column=1, sticky=W, pady=val_y, padx=val_x)
mail_label.grid(row=5, column=1, sticky=W, pady=val_y, padx=val_x)

## Create a Entry Fields And Radio Button For Form

name_entry = Entry()
age_entry = Entry()

v = IntVar()
gender1 = ttk.Radiobutton(text='Male', value=1, variable=v)
gender2 = ttk.Radiobutton(text='female', value=2, variable=v)

number_entry = Entry()
mail_entry = Entry()

val_x = 3
val_y = 3

name_entry.grid(row=0, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
age_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
gender1.grid(row=2, column=2, padx=(2, 15), sticky=W)
gender2.grid(row=3, column=2, padx=(2, 15), sticky=W)
number_entry.grid(row=4, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
mail_entry.grid(row=5, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)

## Create Buttons

submit = ttk.Button(text='Submit', command=Insert_Data, width=17, )
submit.grid(row=6, column=1, sticky=E + W, padx=2, ipadx=3, ipady=3)

clear = ttk.Button(text='Clear', command=Clear, )
clear.grid(row=6, column=2, sticky=E + W, pady=5, padx=(2, 15), ipadx=3, ipady=3)

exit = ttk.Button(text='Exit', command=quit_win, )
exit.grid(row=7, column=1, columnspan=2, sticky=W + E, padx=(2, 15), pady=(0, 15), ipadx=3, ipady=3)

# Add a Image

img_list = os.listdir(r'images')
random.shuffle(img_list)
file_name = random.choice(img_list)
file_path = r"images\\" + file_name

photo = PhotoImage(file=file_path)

img_lb = Label(image=photo)
img_lb.image = photo
img_lb.grid(row=0, column=0, rowspan=6)

window.mainloop()
