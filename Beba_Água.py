from PIL import Image
import time as t
import tkinter as tk
from tkinter import messagebox

def popup(Titulo, Mensagem):
    tk.Tk().withdraw()
    messagebox.showinfo(
    title=Titulo,message = Mensagem)

while True:
    popup("Favor Beber Água", "Fazem 20 minutos desde que voce bebeu Água\nAperte ok quando beber")
    im = Image.open('imagem.jfif') 
    im.show()
    t.sleep(1200)
    continue

