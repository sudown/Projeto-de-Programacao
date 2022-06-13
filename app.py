from tkinter import *
import tkinter
from turtle import color
import customtkinter
from PIL import ImageTk, Image
import random

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1280x720")
app.configure(bg="#fff")
app.title("APP")

################### IMAGENS ###############
img = ImageTk.PhotoImage(Image.open("./img/flor.jpg"))

################### FONTES ############### se for trocar ou adicionar uma cor ou fonte faça por aqui
fontPrimary = "Arial, 24"

################### CORES ###############
azul = "#0091ca"
verde = "#01bc53"
rosa = "#d7508a"
branco = "#e2dcd2"
laranja = "#f07d54"
pave = "#ffc1ce"

listaCores = [azul, verde, rosa, branco, laranja, pave]

bgColorPrimary = "#7C4CAF" 
bgColorSecundary = "#7C4CAF"
frameHome = Frame(app, bg=bgColorPrimary, height=720, width=1280)
frameHome.pack()

def destroiFrame(frame):
    for item in frame.winfo_children(): #pega itens, um a um do frame e destroi limpando a tela
        item.destroy()

def home(telaAtual):
    destroiFrame(telaAtual)
    buttonDitado = customtkinter.CTkButton(master=frameHome, text="Ditado", text_font=(fontPrimary))
    buttonPortugues = customtkinter.CTkButton(master=frameHome, text="Português", text_font=(fontPrimary), command=temasPortugues)
    buttonEnglish = customtkinter.CTkButton(master=frameHome, text="English", text_font=(fontPrimary), command=temasEnglish)

    buttonDitado.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    buttonPortugues.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
    buttonEnglish.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

def geraMenuTemas(lingua):
    frameTelaTemas = Frame(frameHome, bg=bgColorSecundary, height=720, width=1280).pack() #faria mais sentido trocar frameHome por app, mas isso não funcionou
    
    listaTemas = []
    if (lingua == "pt-br"): #se for pt-br ira pegar o arquivo em portugues se nao pega o ingles
        config = open("language/config_pt.txt", "r", encoding="utf-8")
        titulo = customtkinter.CTkButton(master=frameHome, text="Ditado", bg_color=bgColorSecundary, text_font=(fontPrimary))
        titulo.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    else:
        config = open("language/config_en.txt", "r", encoding="utf-8")
        titulo = customtkinter.CTkButton(master=frameHome, text="Saying", bg_color=bgColorSecundary, text_font=(fontPrimary))
        titulo.place(relx=0.5, rely=0.1, anchor=tkinter.N)

    texto = config.readlines()
    for linha in texto:
        if linha[0] == "t": #verifica se é um tema
            inicio, fim = 3, len(linha)-2
            tema = linha[inicio:fim]
            listaTemas.append(tema) #adiciona todos os temas a um lista
    config.close()

    

    frameMenuTemas = Frame(frameTelaTemas, bg=bgColorSecundary, height=500, width=800)
    frameMenuTemas.place(relx=0.437, rely=0.2, anchor=tkinter.N)

    rlx = c = 0.00
    rly = 0.04
    for i in range(0, len(listaTemas)):
        rlx += 0.3
        c += 1
        if c == 4:
            rly += 0.3
            rlx = 0.3
            c = 1
        buttonTema = customtkinter.CTkButton(frameMenuTemas, text=listaTemas[i], text_font=fontPrimary, command="",fg_color=listaCores[random.randint(0,5)], hover_color=listaCores[random.randint(0,5)])
        buttonTema.place(relx=rlx, rely=rly, anchor=tkinter.N)

def temasPortugues():
    destroiFrame(frameHome)
    geraMenuTemas("pt-br")

def temasEnglish():
    destroiFrame(frameHome)
    geraMenuTemas("en-us")

    '''buttonFase = customtkinter.CTkButton(master=frameHome, text="Fase", bg_color="#028f40")
    buttonFase.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    fase1 = Label(frameHome, image=img)
    fase1.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)''' #tela de fase

home(frameHome)

app.mainloop()