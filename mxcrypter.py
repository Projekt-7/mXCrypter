import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image

def new_file():
    key_value_input.delete(1.0, tk.END)
    plan_text_input.delete(1.0, tk.END)
    ciphertext.delete(1.0, tk.END)
    key_value_input2.delete(1.0, tk.END)
    encrypt_text.delete(1.0, tk.END)
    plan_text2.delete(1.0, tk.END)
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    name_encryption_algorithm.config(text='Wybierz algorytm, którym chcesz zaszyfrować lub zdeszyfrować dane')

def open_file_encrypt():
    filename = fd.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])  # wywołanie okna dialogowego open file

    if filename:
        with open(filename, "r", -1, "utf-8") as file:
            all_lines = file.readlines()
            new_file()
            key_value_input.insert(tk.END, all_lines[0])
            plan_text_input.insert(1.0,  all_lines[1])
            ciphertext.insert(1.0,  all_lines[2])


def open_file_decrypt():
    filename = fd.askopenfilename(filetypes=[("Plik tekstowy", "*.txt")])  # wywołanie okna dialogowego open file

    if filename:
        with open(filename, "r", -1, "utf-8") as file:
            all_lines = file.readlines()
            new_file()
            key_value_input2.insert(tk.END, all_lines[0])
            encrypt_text.insert(1.0, all_lines[1])
            plan_text2.insert(1.0, all_lines[2])

def file_save_encrypt():
    filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")],
                                    defaultextension="*.txt")  # wywołanie okna dialogowego save file

    if filename:
        with open(filename, "w", -1, "utf-8") as file:
            file.truncate(0)
            file.write(key_value_input.get(1.0, tk.END))
            file.write(plan_text_input.get(1.0, tk.END))
            file.write(ciphertext.get(1.0, tk.END))


def file_save_decrypt():
    filename = fd.asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")],
                                    defaultextension="*.txt")  # wywołanie okna dialogowego save file

    if filename:
        with open(filename, "w", -1, "utf-8") as file:
            file.truncate(0)
            file.write(key_value_input2.get(1.0, tk.END))
            file.write(encrypt_text.get(1.0, tk.END))
            file.write(plan_text2.get(1.0, tk.END))

def encryptCaesar():
    zaszyfrowny = ""
    a = int(key_value_input.get("1.0",END))

    b = str(plan_text_input.get("0.0", "end"))

    for i in range(len(b)):
        if ord(b[i]) > 122 + a:
            zaszyfrowny += chr(ord(b[i]) + a - 26)
        else:
            zaszyfrowny += chr(ord(b[i]) + a)
    ciphertext.insert(1.0, zaszyfrowny[0:-1])

def decryptCaesar():
    zdeszyfrowny = ""
    a = int(key_value_input2.get("1.0", END))
    b = str(encrypt_text.get("0.0", "end"))
    for i in range(len(b)):
        if ord(b[i]) > 122 + a:
            zdeszyfrowny += chr(ord(b[i]) - a - 26)
        else:
            zdeszyfrowny += chr(ord(b[i]) - a)
    plan_text2.insert(1.0, zdeszyfrowny[0:-1])

def encryptVerman():
    result = ""
    a = str(key_value_input.get("1.0", END))


    b = str(plan_text_input.get("0.0", "end"))


    answer = ""
    p = 0
    for char in b:
        answer += chr(ord(char) ^ ord(a[p]))
        p += 1
        if p == len(a):
            p = 0
    ciphertext.insert(1.0, answer[0:-1])

def decryptVerman():
    a = str(key_value_input2.get("1.0", END))


    b = str(encrypt_text.get("0.0", "end"))

    answer = ""
    p = 0
    for char in b:
        answer += chr(ord(char) ^ ord(a[p]))
        p += 1
        if p == len(a):
            p = 0
    plan_text2.insert(1.0, answer[0:-1])

def encryptVigenere():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    enc_string = ""
    enc_key = str(key_value_input.get("1.0", END)).lower()
    input_string = str(plan_text_input.get("0.0", "end")).lower()
    string_length = len(input_string)
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            position = alphabet.find(letter)
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter

    ciphertext.insert(1.0, enc_string)
def decryptVigenere():
    a = str(key_value_input2.get("1.0", END))


    b = str(encrypt_text.get("0.0", "end"))


    key_length = len(a)
    key_as_int = [ord(i) for i in a]
    ciphertext_int = [ord(i) for i in b]
    plaintextver = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintextver += chr(value + 65)

    plan_text2.insert(1.0, plaintextver)

def selectCaesar():
    encrypt_button.configure(command=encryptCaesar)
    decrypt_button.configure(command=decryptCaesar)
    name_encryption_algorithm.config(text='Szyfr Cezara')
    button1.configure(state=DISABLED)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
def selectVernam():
    encrypt_button.configure(command=encryptVerman)
    decrypt_button.configure(command=decryptVerman)
    name_encryption_algorithm.config(text='Szyfr Vernama')
    button1.configure(state=NORMAL)
    button2.configure(state=DISABLED)
    button3.configure(state=NORMAL)
def selectVigenere():
    encrypt_button.configure(command=encryptVigenere)
    decrypt_button.configure(command=decryptVigenere)
    name_encryption_algorithm.config(text="Szyfr Vigenere'a")
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=DISABLED)

root = Tk(className='mXCrypter')
root.configure(bg="black")
root.geometry("1280x720")
root.resizable(False, False)

# Należy podmienić ścieżke do loga programu w 237 i 238 linijce

p1 = PhotoImage(file='C:\\Users\\Mateusz\\Desktop\\mXCrypter\\logo.png')
logo_path = "C:\\Users\\Mateusz\\Desktop\\mXCrypter\\logo.png"

root.iconphoto(False, p1)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Nowy", command=new_file)

submenu = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='Otwórz...', menu=submenu)
submenu.add_command(label="Szyfrowanie", command=open_file_encrypt)
submenu.add_command(label="Dezzyfrowanie", command=open_file_decrypt)

submenu2 = Menu(filemenu, tearoff=0)
filemenu.add_cascade(label='Zapisz...', menu=submenu2)
submenu2.add_command(label="Szyfrowanie", command=file_save_encrypt)
submenu2.add_command(label="Dezzyfrowanie", command=file_save_decrypt)

filemenu.add_separator()
filemenu.add_command(label="Zamknij", command=root.quit)
menubar.add_cascade(label="Plik", menu=filemenu)

algochoosemenu = Menu(menubar, tearoff=0)
algochoosemenu.add_radiobutton(label="Szyfr Cezara", command=selectCaesar)
algochoosemenu.add_radiobutton(label="Szyfr Vernama", command=selectVernam)
algochoosemenu.add_radiobutton(label="Szyfr Vigenere'a", command=selectVigenere)
menubar.add_cascade(label="Algorytm", menu=algochoosemenu)

frame1 = Frame(root, height=100, bg="black")
frame1.pack(fill=BOTH, side=LEFT, expand=True)

img = ImageTk.PhotoImage(Image.open(logo_path))

panelleft = Label(frame1, image=img)
panelleft.configure(bg="black")
panelleft.pack()
panelleft.place(x=40, y=0)

frame2 = Frame(root, width=200, bg="#222222")

encrypt_label = Label(frame2, text="Szyfrowanie", font=("Arial", 16),bg="#222222", fg="#ffffff",height=2)
encrypt_label.place(x=190,y=60)

key_value_label = Label(frame2, text="Szyfr", font=("Arial", 14),bg="#222222", fg="#ffffff")
key_value_label.place(x=220,y=120)

key_value_input = Text(frame2, width=10, height=1,bd=2)
key_value_input.place(x=210,y=160)

plan_text_label = Label(frame2, text="Tekst jawny", font=("Arial", 14),bg="#222222", fg="#ffffff")
plan_text_label.place(x=200,y=200)

plan_text_input = Text(frame2, width=40, height=4,bd=2)
plan_text_input.place(x=100,y=240)

encrypt_button = tk.Button(frame2, text='Szyfruj', height=1, width=15, bd = 5, bg="#ff7f00",font="Arial 10 bold",fg="#ffffff",command= '')
encrypt_button.place(x=190, y=340)
encrypt_button.pack

plan_text_label = Label(frame2, text="Dane zaszyfrowane", font=("Arial", 14),bg="#222222", fg="#ffffff")
plan_text_label.place(x=160,y=420)

ciphertext = Text(frame2, width=40, height=4,bd=2)
ciphertext.place(x=100,y=470)

frame2.pack(fill=BOTH, side=LEFT, expand=True)

frame3 = Frame(root, width=200, bg="#333333")
name_encryption_algorithm = Label(root, text="Wybierz algorytm, którym chcesz zaszyfrować lub zdeszyfrować dane", font=("Arial", 18),bg="#000000", fg="#ffffff",width=80, height=2)
name_encryption_algorithm.place(x=240,y=0)
name_encryption_algorithm.pack

decrypt_label = Label(frame3, text="Deszyfrowanie", font=("Arial", 16),bg="#333333", fg="#ffffff",height=2)
decrypt_label.place(x=170,y=60)

key_value_label = Label(frame3, text="Szyfr", font=("Arial", 14),bg="#333333", fg="#ffffff")
key_value_label.place(x=220,y=120)

key_value_input2 = Text(frame3, width=10, height=1,bd=2)
key_value_input2.place(x=210,y=160)

plan_text_label = Label(frame3, text="Dane zaszyfrowane", font=("Arial", 14),bg="#333333", fg="#ffffff")
plan_text_label.place(x=180,y=200)

encrypt_text = Text(frame3, width=40, height=4,bd=2)
encrypt_text.place(x=100,y=240)

decrypt_button = tk.Button(frame3, text='Deszyfruj', height=1, width=15, bd = 5, bg="#ff7f00",font="Arial 10 bold",fg="#ffffff",command= '')
decrypt_button.place(x=190, y=340)
decrypt_button.pack

plan_text_label = Label(frame3, text="Tekst jawny", font=("Arial", 14),bg="#333333", fg="#ffffff")
plan_text_label.place(x=210,y=420)

plan_text2 = Text(frame3, width=40, height=4,bd=2)
plan_text2.place(x=100,y=470)

frame3.pack(fill=BOTH, side=LEFT, expand=True)

frame1.pack(fill=BOTH, side=LEFT)

root.config(menu=menubar)

button1 = tk.Button(root, text='Szyfr Cezara', height=2, width=25, fg="#ffffff",bd = 5, bg="#ff7f00", font="Arial 10 bold", command=selectCaesar)
button1.place(x=40, y=200)
button1.pack

button2 = tk.Button(root, text='Szyfr Vernama', height=2, width=25, fg="#ffffff",bd = 5, bg="#ff7f00",font="Arial 10 bold", command=selectVernam)
button2.place(x=40, y=280)
button2.pack

button3 = tk.Button(root, text="Szyfr Vigenere'a", height=2, fg="#ffffff", width=25,bd = 5, bg="#ff7f00",font="Arial 10 bold", command=selectVigenere)
button3.place(x=40, y=360)
button3.pack

root.mainloop()
