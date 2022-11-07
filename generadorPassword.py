from tkinter import *
#tkinter abre la ventana emergente
import pyperclip
import random
#inicializamos la pantalla tkinter
pantalla= Tk()
pantalla.geometry("600x600")

#variables para almacenar la contraseña
passw= StringVar()
#tamaño de la contraseña
passwlen=IntVar()

#inicializo el tamaño de la contraseña
passwlen.set(0)

#funcion para generar la contraseña
def generador():
    passw1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                   'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                   'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                   '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
                   '*', '(',')']
    
    password=""
    #hacemos un for que recorrala longitud de la constraseña
    #definido poor el usuario
    for x in range(passwlen.get()):
        password=password+random.choice(passw1)
    #seteamos el password
    passw.set(password)

#funcion para copiar la contraseña generada en el clipboard

def clipboard():
    random_password=passw.get()
    pyperclip.copy(random_password)

#titulo de la ventana emergente
Label(pantalla, text="Aplicacion generadora de constaseña", font="calibri 20 bold").pack()

#ingrese el tamaño de la constraseña
Label(pantalla, text="Ingrese la longitud de la constraseña").pack(pady=3)

Entry(pantalla, textvariable=passwlen).pack(pady=3)

#boton para generar la funcion
Button(pantalla, text="Generar contraseña", command=generador).pack(padx=7)
#muestra la constraseña generada
Entry(pantalla, textvariable=passw).pack(pady=3)

#boton para llamar la funcion de clipboard
Button(pantalla, text="Copiar al portapales", command=clipboard).pack()

pantalla.mainloop()