import tkinter as tk
from tkinter.ttk import *
from random import choice

window = tk.Tk()

window.configure(bg='#856ff8')
# Tilte
window.title("Arnav Password Generator")
window.geometry("800x600")
photo = tk.PhotoImage(file = "password.png")
window.iconphoto(False, photo)

# Heading
heading1 = Label(window, text = "Password Generator", font=("Arial", 50), background="#856ff8").pack(side = tk.TOP)
heading2 = Label(window, text = "Made By Arnav", font = ("Arial", 10), background="#856ff8").pack(side = tk.TOP,pady= 15)



char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ111222333444555666777888999000!!!@@@###$$$%%%^&&&***???//'
password = ''
# button to save password

# save password
def ask_to_save(password):
    ask_to_save = tk.Tk()
    ask_to_save.resizable(0, 0)
    ask_to_save.configure(bg='white')
    ask_to_save.title("Info")
    Width = 850
    Height = 200
    positionRight = int(ask_to_save.winfo_screenwidth() / 2 - Width / 2)
    positionDown = int(ask_to_save.winfo_screenheight() / 2 - Height / 2)
    ask_to_save.geometry("+{}+{}".format(positionRight, positionDown))
    ask_to_save.geometry("400x100")
    label = Label(ask_to_save,text = "Do you want to save Password?",font=("Arial",20),background = "white").pack(side = tk.TOP)
    Yes = tk.Button(ask_to_save,text = "yes", command=lambda:save_password(password), font=("Arial",10) , background = "gray").place(x=80,y=55)
    No = tk.Button(ask_to_save,text= "No",command=ask_to_save.destroy ,font = ("Arial",10),background = "gray").place(x = 270,y=55)
def save_password(password):
    name_of_file = tk.Tk()
    name_of_file.resizable(0,0)
    name_of_file.configure(bg='white')
    name_of_file.title("Name the File")
    Width = 850
    Height = 200
    positionRight = int(name_of_file.winfo_screenwidth() / 2 - Width / 2)
    positionDown = int(name_of_file.winfo_screenheight() / 2 - Height / 2)
    name_of_file.geometry("+{}+{}".format(positionRight, positionDown))
    name_of_file.geometry("400x150")
    label1 = Label(name_of_file,text="Enter the file name",font=("Arial", 20), background="white",foreground ="black")
    label1.pack(side=tk.TOP)
    saved = tk.Label(name_of_file,text="password saved",font=("Arial", 10), background="white",foreground ="black")
    file_name = tk.Entry(name_of_file, font=("Arial", 15), width=20,background = 'white',foreground="black")
    file_name.pack(side=tk.TOP,pady = 10)
    save = tk.Button(name_of_file,text="save",command= lambda : creat_file(password)).place(x=150,y=100)
    def creat_file(password):
        try:
            name = file_name.get()
            f = open(name, "w+")
            f.write("Your Password-"+password)
            f.close()
            saved.place(x=130, y=70)
        except FileNotFoundError:
            f = open("paswrd","w+")
            f.write("Your Password-"+ password)
            f.close()
            saved.place(x=130, y=70)
# Popup window(error)
def popup(t):
    # window ,title and position
    popup = tk.Tk()
    popup.resizable(0, 0)
    popupWidth = 850
    popupHeight = 200
    positionRight = int(popup.winfo_screenwidth() / 2 - popupWidth / 2)
    positionDown = int(popup.winfo_screenheight() / 2 - popupHeight / 2)
    popup.geometry("+{}+{}".format(positionRight, positionDown))
    popup.geometry("300x100")
    popup.configure(bg='white')
    popup.title("Error")

    # message , button and error image


    warning = Label(popup,text = t,font=("Arial",20),background = "white").pack(side = tk.TOP)
    ok = tk.Button(popup,text = "OK",command=popup.destroy,background = "gray",foreground="black",font=("Arial Bold",15))
    ok.pack(side=tk.TOP,pady=20)

def generate(length):
    global password
    global output
    output.delete('1.0', tk.END)
    try:
        length = int(length)
        for i in range(length):
            r = choice(char)
            password += r
        ask_to_save(password)
    except ValueError as e:
        popup("Invalid Input")




# genrated password
def show_password():
    global password
    global output
    output.insert(tk.END, password)
    password = ''

# Number of letters
ask = tk.Label(window, text = 'Enter the Length of Password', font = ("Arial", 13))
ask.pack(side = tk.TOP,pady=15)
enter = tk.Entry(window, font=("Arial", 50), width=2,background = 'white',foreground="black")
enter.pack(side=tk.TOP)
def take_input():
    global length
    length = enter.get()
take_input()

# Button to generate password
btn = tk.Button(window, text = "Generate Password", command = lambda : [take_input(),generate(length),show_password()], font=("Arial",50)).pack(side=tk.BOTTOM,pady = 50)

output = tk.Text(window, height=1, width=22, font=("Helvetica", 20), background = "white",foreground="red")
paswrd = tk.Label(window, text = 'Your Password',font=("Arial",13))
output.pack(side=tk.BOTTOM)
paswrd.pack(side=tk.BOTTOM)
window.mainloop()
