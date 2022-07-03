import tkinter
from tkinter import *
from tkinter import ttk
from Tools.demo.ss1 import center
from PIL import Image, ImageTk

def histoire_crash_bandicoot():
    window_histoire = tkinter.Tk()
    window_histoire.geometry("800x300")
    window_histoire.title("Histoire de Crash Bandicoot")
    window_histoire1 = ttk.Label(window_histoire, text="\n\n\n\nCrash Bandicoot est un jeu vidéo de plates-formes développé\npar Naughty Dog et édité par Sony Computer Entertainment\nen 1996 sur PlayStation. Il constitue le premier épisode\nde la série Crash Bandicoot\n\n\n\n\n\n\n\n\n\n")
    window_histoire1.config(justify=CENTER, foreground='yellow', background='purple', width=1000, font=('Courier', 15, 'bold'))
    window_histoire1.pack()

def regle():
    window_regle=tkinter.Tk()
    window_regle.geometry("1000x300")
    window_regle.title("La règle du jeu Crash Bandicoot")
    window_regle1=ttk.Label(window_regle, text = "\n\n\n\n\n\tCrash Bandicoot doit sauver sa petite amie, Tawna. \nParmis les ennemis il y a le crabe, le personnage Slim et la moufette.\nCrash doit les affronter tous et les vaincre pour pouvoir sauver sa bien-aimée!\n\n\n\n\n\n\n\n\n\n\n")
    window_regle1.config(justify=CENTER, foreground='yellow', width=1000, background='purple', font=('Courier',15,'bold'))
    window_regle1.pack()
    #window.mainloop()

def membres():
    window_membre = tkinter.Tk()
    window_membre.geometry("1200x450")
    window_membre.title("Liste des membres de l'equipe de travail 1PROJ")
    window_membre1=ttk.Label(window_membre, text = " PRENOM    | NOM \t      |  ROLE")
    window_membre=ttk.Label(window_membre, text = " Nana Jacelie\tBAKALAFOUA M'BOUSSI \t Marketing et Communication\n\n Nihad Rachel \tOULKHIARI \t\t Développeuse et Manager de projet\n\n Waï Berty \tLEKONE ANTA \t\t Développeuse\n\n Koundian \tSISSOKO \t\t Designer\n\n Seng Davy \tSIENG \t\t\t Cheffe designer\n\n Soronik \tSIENG \t\t\t Développeur\n\n Nazih \t\tKAF \t\t\t Marketing")
    window_membre.config(justify=LEFT, foreground='yellow', width=100, background='purple', relief= RIDGE, font=('Courier', 20,'bold'))
    window_membre1.config(justify=LEFT, foreground='yellow', width=70,background='purple', relief=GROOVE, borderwidth=10, font=('Courier', 25,'bold'))
    window_membre1.pack()
    window_membre.pack()
    window_membre.mainloop()

def membre():
    membre= Tk()
    membre.title('Photo des membres')
    membre.geometry('800x500')
    membre.iconbitmap('logocrash.png')
    membre.config(background='purple')
    my_pic=ImageTk.PhotoImage(file="team.png")
    label=Label(master=membre, image=my_pic)
    label.pack(pady=20)

def menu():

    wind = tkinter.Tk()
    wind.geometry("1000x500")
    wind.title("Crash Bandicoot")
    menu1 = tkinter.Menu(wind)
    col1 = tkinter.Menu(menu1, tearoff=0)
    #Background
    bgImage = PhotoImage(file="Menu.png")
    tkinter.Label(wind, image=bgImage).place(relwidth = 1, relheight= 1 )

    menu1.add_cascade(label="Menu", menu=col1)
    menu1.add_cascade(label="Options")
    col1.add_command(label="Regle du jeu", command=regle)
    col1.add_command(label="Histoire de Crash Bandicoot", command=histoire_crash_bandicoot)
    col1.add_command(label="Membres de l'equipe", command=membres)
    col1.add_command(label="Quitter", command=wind.quit)
    wind.config(menu=menu1, background='purple')
    frame=tkinter.Frame(wind,width=100, height=100, background="white")
    button=Button(wind, text="Lancer le Jeu", bg='orange', fg='darkgreen', font=('Lucida', 15, 'bold'), relief=RIDGE, width=10, borderwidth=5, command=wind.quit)
    frame.pack()
    button.pack()
    wind.mainloop()

menu()