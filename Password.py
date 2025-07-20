from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import string,random

main = Tk()
main.geometry("450x450")
main.title("Password Generator by Priya")
main.config(bg="violet")
main.resizable(False,False)

def password_generate():
    try:
        length_password = int(solidboss.get())
        small_letters = string.ascii_lowercase
        capital_letters = string.ascii_uppercase
        digits = string.digits
        special_character = string.punctuation
        all_list = []
        all_list.extend(list(small_letters))
        all_list.extend(list(capital_letters))
        all_list.extend(list(digits))
        all_list.extend(list(special_character))
        random.shuffle(all_list)
        password.set("".join(all_list[0:length_password]))
    except:
        messagebox.showerror("Invalid Input", "Please select a valid password length.")



all_no = {"1": "1","2" : "2","3" : "3","4" : "4","5" : "5","6" : "6","7" : "7","8" : "8","9" : "9","10" : "10",
"11" : "11","12" : "12","13" : "13","14" : "14","15" : "15",
"16" : "16","17" : "17","18" : "18","19" : "19","20" : "20",
"21" : "21","22" : "22","23" : "23","24" : "24","25" : "25","26" : "26","27" : "27","28" : "28","29" : "29","30" : "30"}
Title = Label(main, text = " PASSWORD GENERATOR",bg="blue",fg ="black",font=("futura",15,"bold"))
Title.place(x=100,y=20)

length_label = Label(main, text = "Select the length of your password:-", fg="darkgreen",bg="beige",font=("ubuntu",12))
length_label.place(x =20, y=80)

solidboss = StringVar()
Selector = Combobox(main, textvariable = solidboss, state="readonly")
Selector['value'] = [l for l in all_no.keys()]
Selector.current(7)
Selector.place(x=280, y= 80)

def on_enter(e):
    generate_btn['bg'] = "grey"
    generate_btn['fg'] = "white"

def on_leave(e):
    generate_btn['bg'] = "orange"
    generate_btn['fg'] = "black"

def clear_password():
    password.set("")
clear_btn = Button(main, text = "Clear", command =clear_password, bg="red", fg="white", font=("ubuntu",12))
clear_btn.place(x=200,y=270)

generate_btn = Button(main, text="Generate Password 🔐",bg ="green",fg="black", font=("ubuntu", 15), cursor="hand2", command = password_generate)
generate_btn.bind("<Enter>", on_enter)
generate_btn.bind("<Leave>", on_leave)
generate_btn.place(x=120,y=140)

result_lable = Label(main, text = "Generated Password Here 🔑:- ", bg="beige", fg ="red",font=("ubuntu", 12))
result_lable.place( x=20, y= 200)

password = StringVar()
password_final = Entry(main, textvariable = password, state="readonly", fg="green", font=("ubuntu",15),width=30)
password_final.place(x=50,y=230)

main.mainloop()