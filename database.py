from tkinter.filedialog import *
from tkinter import *
from tkinter.ttk import Combobox

def temp_text(event):
    """function that gets called whenever sname is clicked"""
    if sname.get() == 'Rupesh Kumar Mahato':
        sname.delete(0, "end")  # delete all the text in the sname
        sname.insert(0, '')  # Insert blank for user input
        sname.config(fg='black')


def temp_text2(event):
    """function that gets called whenever sname is clicked"""
    if dobe.get() == '08-05-2001':
        dobe.delete(0, "end")  # delete all the text in the sname
        dobe.insert(0, '')  # Insert blank for user input
        dobe.config(fg='black')


def temp_text3(event):
    """function that gets called whenever sname is clicked"""
    if fname.get() == 'Rajdev Mahato':
        fname.delete(0, "end")  # delete all the text in the sname
        fname.insert(0, '')  # Insert blank for user input
        fname.config(fg='black')


def temp_text4(event):
    """function that gets called whenever sname is clicked"""
    if vcentry.get() == 'Bharatpur':
        vcentry.delete(0, "end")  # delete all the text in the sname
        vcentry.insert(0, '')  # Insert blank for user input
        vcentry.config(fg='black')

    # def save():


#	print("student's name: ", snamevalue.get(), classcombo.get(),  dobvalue.get(), vcvalue.get(), dcombo.get() , gendercombo.get(), bloodcombo.get(), fvalue.get()
# def save():
# 	file = open("database.txt" , 'a+')
# 	#file.write(f"𝗦𝘁𝘂𝗱𝗲𝗻𝘁'𝘀 𝗡𝗮𝗺𝗲\t\t|𝗖𝗹𝗮𝘀𝘀\t\t|𝗗𝗮𝘁𝗲 𝗢𝗳 𝗕𝗶𝗿𝘁𝗵\t\t|𝗩𝗶𝗹𝗹𝗮𝗴𝗲/𝗖𝗶𝘁𝘆\t\t|𝗗𝗶𝘀𝘁𝗿𝗶𝗰𝘁\t\t|𝗚𝗲𝗻𝗱𝗲𝗿\t|𝗕𝗹𝗼𝗼𝗱\t\t|𝙁𝙖𝙩𝙝𝙚𝙧'𝙨 𝙉𝙖𝙢𝙚\t|\n")
# 	file.write(f'{snamevalue.get()}\t\t|{classcombo.get()}\t\t|{dobvalue.get()}\t
# \t|{vcvalue.get()}\t\t|{dcombo.get()}\t\t\t|{gendercombo.get()}\t\t|{bloodcombo.get()}\t\t|{fvalue.get()}\t\t|\n')
# 	file.close()
# 	savebutton.config(text="saved", bg='green', activebackground="skyblue")
# 	savebutton.after(3000,lambda:savebutton.config(text="Save", bg="red",activebackground="yellow"))

name_width = 31
class_width = 13
dob_width = 21
village_width = 21
dist_width = 21
gender_width = 13
blood_width = 13
father_width = 22


# popup_menu.add_checkbutton("ok")
def save():
    file = 'database.txt'
    data = [(snamevalue.get(), classcombo.get(), dobvalue.get(),
             vcvalue.get(), dcombo.get(), gendercombo.get(), bloodcombo.get(), fvalue.get())]

    with open(file, 'a+') as f:
        for row in data:
            f.write(f"{row[0]:{name_width}} | {row[1]:{class_width}} |"
                    f" {row[2]:{dob_width}} | {row[3]:{village_width}} |"
                    f" {row[4]:{dist_width}} | {row[5]:{gender_width}} | {row[6]:{blood_width}} | "
                    f"{row[7]:{father_width}}|\n")

    sname.delete(0, END)
    dobe.delete(0, END)
    fname.delete(0, END)
    vcentry.delete(0, END)
    classcombo.set('')
    dcombo.set('')
    gendercombo.set('')
    bloodcombo.set('')
    fvalue.set('')

    # show a confirmation message
    savebutton.config(text="saved", bg='green', activebackground="skyblue")
    savebutton.after(3000,lambda:savebutton.config(text="Save", bg="red",activebackground="yellow"))

root = Tk()
root.geometry("583x585")
root.resizable(0, 0)
root.title("Project-I")

intro = Label(root, text="N.G. Academy", font=("Arial", 25), bg="chartreuse2", fg="red").grid(sticky=NSEW, columnspan=5,
                                                                                              rowspan=3, row=0)
introupdate = Label(root,
                    text="                                                                                                                    ",
                    font="bold", bg="skyblue", fg="red").grid(columnspan=5, row=3)
intro2 = Label(root, text="Siraha", bg="CadetBlue4", font=("Arial", 20), fg="red").grid(sticky=NSEW, columnspan=5,
                                                                                        row=3, rowspan=2)

sname1 = Label(root, text="Enter Student's name:", bg="skyblue").grid(row=7, sticky=NSEW)

snamevalue = StringVar()
sname = Entry(root, textvariable=snamevalue)
sname.insert(0, "Rupesh Kumar Mahato")
sname.bind("<FocusIn>", temp_text)
sname.grid(row=7, column=2, sticky=NSEW)

classname = Label(root, text="Class:", bg="skyblue").grid(row=7, column=3, sticky=NSEW)

classes = ['-', 'Nursary', 'L.K.G.', 'U.K.G.', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', "11", "12", "13",
           "14", "15"]
classcombo = Combobox(root, values=classes, width=10)
classcombo.current(0)
classcombo.grid(row=7, column=4, sticky=NSEW)

style1 = Label(root, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="skyblue").grid(row=8, columnspan=5,
                                                                                        sticky=NSEW)

dob = Label(root, text="Date of Birth:", bg="skyblue")
dob.grid(row=9, sticky=NSEW)
dobvalue = StringVar()
dobe = Entry(root, textvariable=dobvalue)
dobe.insert(0, "08-05-2001")
dobe.bind("<FocusIn>", temp_text2)
dobe.grid(row=9, column=2, sticky=NSEW)

fnamee = Label(root, text="Faher's name:", bg="skyblue").grid(row=9, column=3, sticky=NSEW)
fvalue = StringVar()
fname = Entry(root, textvariable=fvalue)
fname.insert(0, "Rajdev Mahato")
fname.bind("<FocusIn>", temp_text3)
fname.grid(row=9, column=4, sticky=NSEW)

style2 = Label(root, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="skyblue").grid(row=10, columnspan=5,
                                                                                        sticky=NSEW)

vcname = Label(root, text="Village/City:", bg="skyblue").grid(row=11, sticky=NSEW)
vcvalue = StringVar()
vcentry = Entry(root, textvariable=vcvalue)
vcentry.insert(0, "Bharatpur")
vcentry.bind("<FocusIn>", temp_text4)
vcentry.grid(row=11, column=2, sticky=NSEW)

districtname = Label(root, text="District:", bg="skyblue").grid(row=11, column=3, sticky=NSEW)

districts = ['Achham', 'Arghakhachi', 'Baglung', 'Baitadi', 'Bajhang', 'Bajura', 'Banke', 'Bara', 'Bardiya',
             'Bhaktapur', 'Bhojpur', 'Chitwan', 'Dadeldhura', 'Dailekh', 'Dang', 'Darchula', 'Dhading', 'Dhankutta',
             'Dhanusha', 'Dolakha', 'Dolpa', 'Doti', 'Eastern', 'Rukum', 'Gorkha', 'Gulmi', 'Humla', 'Illam',
             'Jajarkot', 'Jhapa', 'Jumla', 'Kailali', 'Kalikot', 'Kanchanpur', 'Kapilwastu', 'Kaski', 'Kathmandu',
             'Kavreplanchok', 'Khotang', 'Lalitpur', 'Lamjung', 'Mahotari', 'Makwanpur', 'Manang', 'Morang', 'Mugu',
             'Mustang', 'Myagdi', 'Nawalpur', 'Nuwakot', 'Okhaldhunga', 'Palpa', 'Panchthar', 'Parasi', 'Parbat',
             'Parsa', 'Pyuthan', 'Ramechhap', 'Rasuwa', 'Rauthat', 'Rolpa', 'Rupandehi', 'Salyan', 'Sankhuwasabha',
             'Saptari', 'Sarlahi', 'Sindhuli', 'Sindhupalchok', 'Siraha', 'Solukhumbu', 'Sunsari', 'Surkhet', 'Syangja',
             'Tanahu', 'Taplejung', 'Tehrathum', 'Udayapur', 'Western', 'Rukum']
dcombo = Combobox(root, values=districts, width=10)
dcombo.current(68)
dcombo.grid(row=11, column=4, sticky=NSEW)

style3 = Label(root, text="~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", bg="skyblue").grid(row=12, columnspan=5,
                                                                                        sticky=NSEW)

Gender = Label(root, text="Gender:", bg="skyblue").grid(row=13, sticky=NSEW)
morf = ['-', 'Male', 'Female']
gendercombo = Combobox(root, values=morf, width=10)
gendercombo.current(0)
gendercombo.grid(row=13, column=2, sticky=NSEW)

bloodgroup = Label(root, text="BloodGroup:", bg="skyblue").grid(row=13, column=3, sticky=NSEW)
blood = ['-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
bloodcombo = Combobox(root, values=blood, width=10)
bloodcombo.current(0)
bloodcombo.grid(row=13, column=4, sticky=NSEW)

sname1 = Label(root, text="", bg="skyblue").grid(row=15, columnspan=5, sticky=NSEW)
sname2 = Label(root, text="", bg="skyblue").grid(row=16, columnspan=5, sticky=NSEW)
sname3 = Label(root, text="", bg="skyblue").grid(row=17, columnspan=5, sticky=NSEW)
sname4 = Label(root, text=" ", bg="skyblue").grid(row=17, columnspan=5, sticky=NSEW)
sname5 = Label(root, text="", bg="skyblue").grid(row=18, columnspan=5, sticky=NSEW)
sname6 = Label(root, text="", bg="skyblue").grid(row=19, columnspan=5, sticky=NSEW)
sname7 = Label(root, text="", bg="skyblue").grid(row=20, columnspan=5, sticky=NSEW)
sname8 = Label(root, text="", bg="skyblue").grid(row=21, columnspan=5, sticky=NSEW)
sname9 = Label(root, text="", bg="skyblue").grid(row=22, columnspan=5, sticky=NSEW)
sname10 = Label(root, text="", bg="skyblue").grid(row=23, columnspan=5, sticky=NSEW)
sname11 = Label(root, text="", bg="skyblue").grid(row=24, columnspan=5, sticky=NSEW)
sname12 = Label(root, text=" ", bg="skyblue").grid(row=25, columnspan=5, sticky=NSEW)
sname13 = Label(root, text="", bg="skyblue").grid(row=26, columnspan=5, sticky=NSEW)
sname14 = Label(root, text="", bg="skyblue").grid(row=27, columnspan=2, sticky=NSEW)
sname15 = Label(root, text="", bg="skyblue").grid(row=27, column=4, columnspan=2, sticky=NSEW)

savebutton = Button(root, text="save", state="normal", font=("Arial", 15, "bold"), bg="red", cursor="hand2",
                    relief=GROOVE, borderwidth=10, activebackground="yellow", activeforeground="blue",
                    disabledforeground="black", command=save)
savebutton.grid(row=27, column=2, columnspan=2, sticky=NSEW)

sname16 = Label(root, text="", bg="skyblue").grid(row=28, columnspan=2, sticky=NSEW)
sname17 = Label(root, text="", bg="skyblue").grid(row=28, column=4, columnspan=2, sticky=NSEW)

closebutton = Button(root, text="Close", state="normal", font=("Arial", 10, "bold"), bg="red3", cursor="hand2",
                     relief=GROOVE, borderwidth=10, activebackground="orange", activeforeground="yellow",
                     disabledforeground="brown", fg="green yellow", command=root.destroy).grid(row=28, column=2,
                                                                                               columnspan=2,
                                                                                               sticky=NSEW)
root.mainloop()
