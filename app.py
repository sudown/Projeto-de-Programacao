from tkinter import *
import tkinter
from playsound import playsound
import customtkinter
from PIL import ImageTk
import random
from functools import partial #como não é possivel passar uma função com parametros no campo command de um button, essa biblioteca
import json                                #permite criar uma varivel que recebe a função e o seu parametro. Leiam a linha 118 e 125 preguiçosos
from unidecode import unidecode

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("1280x720")
app.configure(bg="#fff")
app.title("APP")
app.configure(bg="#7C4CAF")

################### IMAGENS ###############
#img = ImageTk.PhotoImage(Image.open("./img/flor.jpg"))

################### FONTES ############### se for trocar ou adicionar uma cor ou fonte faça por aqui
fontPrimary = "Arial, 24"
fontEntry = "Helvetica, 30"
fontAcerto = "Arial, 48"

################### CORES ###############
azul = "#0091ca"
verde = "#01bc53"
rosa = "#d7508a"
branco = "#e2dcd2"
laranja = "#f07d54"
pave = "#ffc1ce"

listaCores = [azul, verde, rosa, branco, laranja, pave]

bgColorPrimary = "#7C4CAF"
bgColorSecundary = "#673f91"
#frameHome = Frame(app, bg=bgColorPrimary, height=720, width=1280)
#frameHome.pack()

def bubble(array):
    trocou = True
    fim = len(array) - 1
    final = len(array) - 1
    while fim > 0 and trocou:
        for i in range(final):
            for i in range(fim):
                if array[i] > array[i + 1]:
                    temp = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = temp
                else:
                    trocou = False
            fim = fim - 1
        final = final - 1

def destroiFrame(frame):
    for item in frame.winfo_children(): #pega itens, um a um do frame e destroi limpando a tela
        item.destroy()

def home():
    frameInicio = Frame(app, bg=bgColorPrimary, height=720, width=1280)
    frameInicio.place(relx=0.5, rely=0.0, anchor=tkinter.N)
    buttonDitado = customtkinter.CTkButton(master=frameInicio, text="Ditado", text_font=(fontPrimary))
    buttonPortugues = customtkinter.CTkButton(master=frameInicio, text="Português", text_font=(fontPrimary), command=temasPortugues)
    buttonEnglish = customtkinter.CTkButton(master=frameInicio, text="English", text_font=(fontPrimary), command=temasEnglish)

    buttonDitado.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    buttonPortugues.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
    buttonEnglish.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

def geraMenuTemas(lingua):
    frameTelaTemas = Frame(app, bg=bgColorPrimary, height=720, width=1280) #faria mais sentido trocar app por app, mas isso não funcionou
    frameTelaTemas.place(relx=0.5, rely=0.0, anchor=tkinter.N)
    listaTemas = []

    if (lingua == "pt-br"): #se for pt-br ira pegar o arquivo em portugues se nao pega o ingles
        config = open("language/json_pt.txt", "r", encoding="utf-8")
        titulo = customtkinter.CTkButton(master=app, text="Ditado", command=home, bg_color=bgColorPrimary, text_font=(fontPrimary))
        titulo.place(relx=0.5, rely=0.1, anchor=tkinter.N)

    else:
        config = open("language/json_en.txt", "r", encoding="utf-8")
        titulo = customtkinter.CTkButton(master=app, text="Saying", command=home, bg_color=bgColorPrimary, text_font=(fontPrimary))
        titulo.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    
    texto = config.readlines()
    listaTemas = []

    for linha in texto:
        js = json.loads(linha)
        #print(js["tema"])
        listaTemas.append(js["tema"]) #adiciona todos os temas a um lista
        config.close()

    frameMenuTemas = Frame(frameTelaTemas, bg=bgColorPrimary, height=500, width=800)
    frameMenuTemas.place(relx=0.437, rely=0.2, anchor=tkinter.N)

    bubble(listaTemas)

    rlx = c = 0.00
    rly = 0.04
    for i in range(0, len(listaTemas)):
        f_geraMenuNiveis = partial(geraMenuNiveis, listaTemas[i], lingua)
        rlx += 0.3
        c += 1
        if c == 4:
            rly += 0.3
            rlx = 0.3
            c = 1
        buttonTema = customtkinter.CTkButton(frameMenuTemas, text=listaTemas[i], text_font=fontPrimary, command=f_geraMenuNiveis, fg_color=listaCores[random.randint(0,5)], hover_color=listaCores[random.randint(0,5)])
        buttonTema.place(relx=rlx, rely=rly, anchor=tkinter.N)

    buttonVoltar = customtkinter.CTkButton(frameMenuTemas, text="← Voltar", text_font=fontPrimary, command=home, fg_color=listaCores[random.randint(0,5)], hover_color=listaCores[random.randint(0,5)])
    buttonVoltar.place(relx=1, rely=1, anchor=tkinter.SE)

def geraMenuNiveis(nomeDoTema, lingua):
    print(nomeDoTema)
    frameTelaNiveis = Frame(app, bg=bgColorPrimary, height=720,width=1280).pack() #

    listaFases = []
    if lingua == "pt-br":
        listaNiveis = ["Fácil", "Médio", "Difícil"]
        titulo = customtkinter.CTkButton(master=app, text="Ditado", command=home, bg_color=bgColorPrimary, text_font=(fontPrimary))
    elif lingua == "en-us":
        listaNiveis = ["Easy", "Medium", "Hard"]
        titulo = customtkinter.CTkButton(master=app, text="Saying", command=home, bg_color=bgColorPrimary, text_font=(fontPrimary))
    else:
        1 == 1

    titulo.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    frameMenuNiveis = Frame(frameTelaNiveis, bg=bgColorPrimary, height=500, width=800)
    frameMenuNiveis.place(relx=0.437, rely=0.2, anchor=tkinter.N)

    rlx = c = 0.00
    rly = 0.04
    for i in range(0, len(listaNiveis)):
        f_geraFases = partial(geraMenuFases, nomeDoTema, listaNiveis[i], lingua)
        rlx += 0.3
        c += 1
        if c == 4:
            rly += 0.3
            rlx = 0.3
            c = 1
        buttonNivel = customtkinter.CTkButton(frameMenuNiveis, text=listaNiveis[i], text_font=fontPrimary, command=f_geraFases, fg_color=listaCores[random.randint(0, 5)], hover_color=listaCores[random.randint(0, 5)])
        buttonNivel.place(relx=rlx, rely=rly, anchor=tkinter.N)

    f_geraMenuTemas = partial(geraMenuTemas, lingua)
    buttonVoltar = customtkinter.CTkButton(frameMenuNiveis, text="← Voltar", text_font=fontPrimary, command=f_geraMenuTemas, fg_color=listaCores[random.randint(0,5)], hover_color=listaCores[random.randint(0,5)])
    buttonVoltar.place(relx=1, rely=1, anchor=tkinter.SE)

def geraMenuFases(nomeDoTema, NivelDoTema, lingua):
    #print(nomeDoTema, NivelDoTema)

    frameTelaFases = Frame(app, bg=bgColorPrimary, height=720, width=1280).pack()
    palavraEscolhida = ""
    listaFases = []
    if lingua == "pt-br":
        config = open("language/json_pt.txt", "r", encoding="utf-8")
        titulo = customtkinter.CTkButton(master=app, text="Ditado", command=home, bg_color=bgColorPrimary, text_font=(fontPrimary))
    elif lingua == "en-us":
        config = open("language/json_en.txt", "r", encoding="utf-8")
        titulo = customtkinter.CTkButton(master=app, text="Saying", command=home, bg_color=bgColorPrimary, text_font=(fontPrimary))
    titulo.place(relx=0.5, rely=0.1, anchor=tkinter.N)
    texto = config.readlines()

    listaFases = []
    for linha in texto:
        js = json.loads(linha)
        if js["tema"] == nomeDoTema:
            config.close()
            break

    for i in range(1, 16):
        listaFases.append(js[str(i)])

    frameMenuFases = Frame(frameTelaFases, bg=bgColorPrimary, height=500, width=800)
    frameMenuFases.place(relx=0.437, rely=0.2, anchor=tkinter.N)

    if lingua == "pt-br":
        if NivelDoTema == "Fácil":
            NumeroDasFases = [0, 1, 2, 3, 4]  # nivel 1 pega as cinco primeiras fases
        elif NivelDoTema == "Médio":
            NumeroDasFases = [5, 6, 7, 8, 9]  # nivel 2 pega as fases do meio
        else:
            NumeroDasFases = [10, 11, 12, 13, 14]  # nivel 2 pega as cinco ultimas fases
    elif lingua == "en-us":
        if NivelDoTema == "Easy":
            NumeroDasFases = [0, 1, 2, 3, 4]  # nivel 1 pega as cinco primeiras fases
        elif NivelDoTema == "Medium":
            NumeroDasFases = [5, 6, 7, 8, 9]  # nivel 2 pega as fases do meio
        else:
            NumeroDasFases = [10, 11, 12, 13, 14]  # nivel 2 pega as cinco ultimas fases

    rlx = c = 0.00
    rly = 0.04
    for i in NumeroDasFases:
        palavraEscolhida = listaFases[i]
        tocaAudio = partial(playsound, (f'./sounds/{unidecode(nomeDoTema)}/{unidecode(listaFases[i])}.mp3'))  # fica pra natureza ficara assim ./sounds/Natureza/Flor.mp3
        f_geraFase = partial(geraFase, nomeDoTema, i, lingua, frameMenuFases, frameTelaFases, i+1, palavraEscolhida, tocaAudio)
        rlx += 0.3
        c += 1
        if c == 4:
            rly += 0.3
            rlx = 0.3
            c = 1
        buttonTema = customtkinter.CTkButton(frameMenuFases, text=i + 1, text_font=fontPrimary, command=f_geraFase, fg_color=listaCores[random.randint(0, 5)], hover_color=listaCores[random.randint(0, 5)])
        buttonTema.place(relx=rlx, rely=rly, anchor=tkinter.N)
        
    f_geraMenuNiveis = partial(geraMenuNiveis, nomeDoTema, lingua)
    buttonVoltar = customtkinter.CTkButton(frameMenuFases, text="← Voltar", text_font=fontPrimary, command=f_geraMenuNiveis, fg_color=listaCores[random.randint(0, 5)], hover_color=listaCores[random.randint(0, 5)])
    buttonVoltar.place(relx=1, rely=1, anchor=tkinter.SE)
    #print(nomeDoTema)

def geraFase(nomeDoTema, nivelDoTema, lingua, frameMenuFases, frameTelaFases, nivelEscolhido, palavraEscolhida, tocaAudio):
    print(nomeDoTema, nivelDoTema, lingua)
    destroiFrame(frameMenuFases)
    frameTelaFase = Frame(frameTelaFases, bg="#c9224f", height=10000, width=10000).pack()

    #img = Image.open(f'./img/{unidecode(nomeDoTema)}/{unidecode(palavraEscolhida)}.png')
    imagem = ImageTk.PhotoImage(file=f'./img/{unidecode(nomeDoTema)}/{unidecode(palavraEscolhida)}.png')
    imagemFase = Label(frameTelaFase, image=imagem)
    imagemFase.place(relx=0.5, rely=0.28, height=300, width=300, anchor=tkinter.N)

    altofalante = ImageTk.PhotoImage(file="./img/altofalante.png")
    buttomAudio = customtkinter.CTkButton(frameTelaFase, command=tocaAudio, text="🔈", text_font=(fontPrimary))
    buttomAudio.place(relx=0.64, rely=0.63, height=50, width=50, anchor=tkinter.N)

    entradaPalavra = Entry(frameTelaFase, background=branco, font=fontEntry)
    entradaPalavra.place(relx=0.5, rely=0.9, height=50, width=600, anchor=tkinter.S)
    
    f_verificaPalavra = partial(verificaPalavra, entradaPalavra, nivelEscolhido, lingua, nomeDoTema)
    buttomEnviar = customtkinter.CTkButton(frameTelaFase, text="Enviar", text_font=fontPrimary, command=f_verificaPalavra, fg_color=listaCores[random.randint(0, 5)], hover_color=listaCores[random.randint(0, 5)])
    buttomEnviar.place(relx=0.75, rely=0.9, anchor=tkinter.SW, height=50)
    
def temasPortugues():
    destroiFrame(app) #destroi o frame
    geraMenuTemas("pt-br")#chama uma função para construir o menu de temas

def verificaPalavra(entradaPalavra, nivelEscolhido, lingua, nomeDoTema):
    #print(entradaPalavra.get())
    palavraDigita = entradaPalavra.get()
    print(palavraDigita)
    palavraDigita = palavraDigita.capitalize()

    if lingua == "pt-br":
        config = open("language/json_pt.txt", "r", encoding="utf-8")
        
    elif lingua == "en-us":
        config = open("language/json_en.txt", "r", encoding="utf-8")
    texto = config.readlines()

    listaFases = []
    for linha in texto:
        js = json.loads(linha)
        if js["tema"] == nomeDoTema:
            config.close()
            break
    for i in range(1, 16):
        listaFases.append(js[str(i)])
    config.close()
    palavraCerta = listaFases[nivelEscolhido - 1]
    print(palavraCerta) 
    
    if palavraDigita == palavraCerta:
        acertouPalavra(lingua)
        print("Você Acertou!")

def acertouPalavra(lingua):
    frameAcertouPalavra = Frame(app, bg=bgColorPrimary, height=500, width=1200)#falta arrumar o height e o width
    frameAcertouPalavra.place(relx=0.5, rely=0.25, anchor=tkinter.N)

    #f_tema = partial(geraMenuTemas, lingua)
    #f_niveis = partial(geraMenuNiveis, nomeDoTema, lingua)
    #f_proxima = partial   ###Vou ver como coiso esse

    fraseAcerto = Label(frameAcertouPalavra, text='Parabens! Você acertou a palavra!', font=(fontAcerto), bg=bgColorSecundary, fg="#fff")
    fraseAcerto.place(relx=0.5, rely=0.3, anchor=tkinter.N)

    buttomTema = customtkinter.CTkButton(frameAcertouPalavra, text="Temas", text_font=fontPrimary,command='f_tema', fg_color=listaCores[random.randint(0, 5)],hover_color=listaCores[random.randint(0, 5)])
    buttomTema.place(relx=0.25, rely=0.8, anchor=tkinter.S, height=50)

    buttomNiveis = customtkinter.CTkButton(frameAcertouPalavra, text="Níveis", text_font=fontPrimary, command='f_niveis', fg_color=listaCores[random.randint(0, 5)], hover_color=listaCores[random.randint(0, 5)])
    buttomNiveis.place(relx=0.50, rely=0.8, anchor=tkinter.S, height=50)

    buttomProximo = customtkinter.CTkButton(frameAcertouPalavra, text="Fases", text_font=fontPrimary, command='f_proxima', fg_color=listaCores[random.randint(0, 5)],hover_color=listaCores[random.randint(0, 5)])
    buttomProximo.place(relx=0.75, rely=0.8, anchor=tkinter.S, height=50)
def temasEnglish():
    destroiFrame(app)
    geraMenuTemas("en-us")

home()

app.mainloop()