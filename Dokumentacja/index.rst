.. DOC documentation master file, created by
   sphinx-quickstart on Fri Jun  4 20:51:51 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Dokumentacja mXCrypter!
===============================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

**Witamy w dokumentacji naszego programu :)**

O programie
############
* **mXCrypter jest programem szufrujacym w trzech szyfrach:**
* Szyfr Cezara,
* Szyfr Vermana,
* Szyfr Vigenere.

Jak zainstalować?
##############
* **Aby uruchomić nasz program wystaczy:**
* 1. *Skopjować kod programu do swojego IDE,*
* 2. *Zamienić scieżkę do loga programu, która znajduje się w linijce programu 235 i 236,*
* 3. *Uruchomić program.*



Jak używać?
###########

Aby użyć naszego programu wytsarczy wybrać szyfr który chcemy użyć, następnie cyfre szyfru i wpisać szyfr, nasz tekst zostanie zaszyfrowany lub odszyfrowany.

Schemat blokowy kodu
#################

.. figure:: C:\\Users\\Dell\\PycharmProjects\\pythonProject8\\zdjecie11.png


Przykładowe kody
###############

* ``def open_file_encrypt():``

   *#wywołanie okna dialogowego open file*

* ``def file_save_encrypt():``

   *#wywołanie okna dialogowego save file*

* ``menubar = Menu(root)``
* ``filemenu = Menu(menubar, tearoff=0)``
* ``filemenu.add_command(label="Nowy", command=new_file)``

   *#stworzenie menu programu*

* ``button1 = tk.Button(root, text='Szyfr Cezara', height=2, width=25, fg="#ffffff",bd = 5, bg="#ff7f00", font="Arial 10 bold", command=selectCaesar)``
* ``button1.place(x=40, y=200)``
* ``button1.pack``

   *#ustawienie przycisków: kolor, rozmiar, nazwa, położenie*

* ``submenu = Menu(filemenu, tearoff=0)``
* ``filemenu.add_cascade(label='Otwórz...', menu=submenu)``
* ``submenu.add_command(label="Szyfrowanie", command=open_file_encrypt)``
* ``submenu.add_command(label="Dezzyfrowanie", command=open_file_decrypt)``

   *#filemenu.add_command(label="Otwórz...", command=open_file), funkcja otwórz plik*

* ``submenu2 = Menu(filemenu, tearoff=0)``
* ``filemenu.add_cascade(label='Zapisz...', menu=submenu2)``
* ``submenu2.add_command(label="Szyfrowanie", command=file_save_encrypt)``
* ``submenu2.add_command(label="Dezzyfrowanie", command=file_save_decrypt)``

   *#filemenu.add_command(label="Zapisz ...", command=file_save), funkcja zapisz plik*

* ``filemenu.add_separator()``
* ``filemenu.add_command(label="Zamknij", command=root.quit)``
* ``menubar.add_cascade(label="Plik", menu=filemenu)``

   *#funkcja zamknij plik*

* ``def selectCaesar():``
* ``def selectVernam():``
* ``def selectVigenere():``

   *#wybranie wybranego szyfu*

* ``def encryptCaesar():``
* ``def decryptCaesar():``
* ``def encryptVerman():``
* ``def decryptVerman():``
* ``def encryptVigenere():``
* ``def decryptVigenere():``

   *#zdefiniowanie funkcji szyfrujących i deszyfrujących*

* ``root.configure(bg="black")``
* ``root.geometry("1280x720")``
* ``root.resizable(False, False)``

* ``p1 = PhotoImage(file='C:\\Users\\Matusz\\PycharmProjects\\mXCrypter\\Images\\logo.png')``
* ``#p1 = PhotoImage(file='logo.png')``
* ``# Setting icon of master window``
* ``root.iconphoto(False, p1)``

   *#ustawienie tła i loga*


