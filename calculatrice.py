import tkinter as tk
from tkinter.messagebox import *

window = tk.Tk()
window.title("Ma calculatrice")

window.geometry("350x500")
window.resizable(0,0)


operationAffichee = ""
operateur = ""
operateurUtilise = True


def btn_1():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "1"
    data.set(operationAffichee)

def btn_2():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "2"
    data.set(operationAffichee)

def btn_3():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "3"
    data.set(operationAffichee)

def btn_4():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "4"
    data.set(operationAffichee)

def btn_5():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "5"
    data.set(operationAffichee)

def btn_6():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "6"
    data.set(operationAffichee)

def btn_7():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "7"
    data.set(operationAffichee)

def btn_8():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "8"
    data.set(operationAffichee)

def btn_9():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "9"
    data.set(operationAffichee)

def btn_0():
    global operationAffichee, operateurUtilise
    operateurUtilise = False
    operationAffichee = operationAffichee + "0"
    data.set(operationAffichee)


def btn_plus():
    global operationAffichee, operateurUtilise
    if operateurUtilise == False:
        operateurUtilise = True
        operationAffichee = operationAffichee + "+"
        data.set(operationAffichee)
    else:
        showinfo('Info','2 opérateurs enchainés ou vous avez commencé votre opération avec un opérateur')

def btn_sous():
    global operationAffichee, operateurUtilise
    if operateurUtilise == False:
        operateurUtilise = True
        operationAffichee = operationAffichee + "-"
        data.set(operationAffichee)
    else:
        showinfo('Info','2 opérateurs enchainés ou vous avez commencé votre opération avec un opérateur')

def btn_mult():
    global operationAffichee, operateurUtilise
    if operateurUtilise == False:
        operateurUtilise = True
        operationAffichee = operationAffichee + "*"
        data.set(operationAffichee)
    else:
        showinfo('Info','2 opérateurs enchainés ou vous avez commencé votre opération avec un opérateur')

def btn_div():
    global operateur,operationAffichee, operateurUtilise
    if operateurUtilise == False:
        operateurUtilise = True
        operateur = "/"
        operationAffichee = operationAffichee + "/"
        data.set(operationAffichee)
    else:
        showinfo('Info','2 opérateurs enchainés ou vous avez commencé votre opération avec un opérateur')

def btn_c():
    global operateur,operationAffichee
    operationAffichee = ""
    operateur = ""
    data.set(operationAffichee)


def egal():
    global operateur,operationAffichee, operateurUtilise

    if operateurUtilise == True:
        showinfo("Info", "Ne terminez pas votre opération par un opérateur")
    else:
        if operateur == "/":
            deuxiemeNombre = operationAffichee.split("/")
            if "0" in deuxiemeNombre:
                showinfo("Info", "Division par 0 non autorisé")
            else:
                resultat = eval(operationAffichee)
                operationAffichee = str(resultat)
                data.set(operationAffichee)
        else:
            resultat = eval(operationAffichee)
            operationAffichee = str(resultat)
            data.set(operationAffichee)


data = tk.StringVar()
lbl = tk.Label(master=window, textvariable = data, background = "#ffffff")
lbl.pack(expand = True, fill = tk.BOTH)


btnrow1 = tk.Frame(master=window)
btnrow1.pack(expand = True, fill = tk.BOTH)

btnrow2 = tk.Frame(master=window)
btnrow2.pack(expand = True, fill = tk.BOTH)

btnrow3 = tk.Frame(master=window)
btnrow3.pack(expand = True, fill = tk.BOTH)

btnrow4 = tk.Frame(master=window)
btnrow4.pack(expand = True, fill = tk.BOTH)



btn7 = tk.Button(master=btnrow1, text = "7", command = btn_7, relief=tk.GROOVE)
btn7.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn8 = tk.Button(master=btnrow1, text = "8", command = btn_8, relief=tk.GROOVE)
btn8.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn9 = tk.Button(master=btnrow1, text = "9", command = btn_9, relief=tk.GROOVE)
btn9.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btnplus = tk.Button(master=btnrow1,text = "+",command = btn_plus, relief=tk.GROOVE)
btnplus.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)



btn4 = tk.Button(master=btnrow2, text = "4", command = btn_4, relief=tk.GROOVE)
btn4.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn5 = tk.Button(master=btnrow2, text = "5", command = btn_5, relief=tk.GROOVE)
btn5.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn6 = tk.Button(master=btnrow2, text = "6", command = btn_6, relief=tk.GROOVE)
btn6.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btnsous = tk.Button(master=btnrow2, text = "-", command = btn_sous, relief=tk.GROOVE)
btnsous.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)



btn1 = tk.Button(master=btnrow3, text = "1", command = btn_1, relief=tk.GROOVE)
btn1.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn2 = tk.Button(master=btnrow3, text = "2", command = btn_2, relief=tk.GROOVE)
btn2.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn3 = tk.Button(master=btnrow3, text = "3", command = btn_3, relief=tk.GROOVE)
btn3.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btnmult = tk.Button(master=btnrow3, text = "*", command = btn_mult, relief=tk.GROOVE)
btnmult.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)




btnc = tk.Button(master=btnrow4, text = "C", command = btn_c, relief=tk.GROOVE)
btnc.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btn0 = tk.Button(master=btnrow4, text = "0", command = btn_0, relief=tk.GROOVE)
btn0.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btnequal = tk.Button(master=btnrow4, text = "=", command = egal, relief=tk.GROOVE)
btnequal.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

btndiv = tk.Button(master=btnrow4, text = "/", command = btn_div, relief=tk.GROOVE)
btndiv.pack(side = tk.LEFT, expand = True, fill = tk.BOTH)

window.mainloop()
