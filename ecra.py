from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

# importando o TkScrolledframe
from tkscrolledframe import ScrolledFrame


# importando bibliotecas necessarias
import requests
import json


# cores ---------------------

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde
co10 ="#6e8faf"  # 
co11 = "#f2f4f2"


# Criando janela -----------------------------------------------------

janela = Tk()
janela.title ("")
janela.geometry('350x415')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)


# Frames -----------------------------------------------------

frameCima = Frame(janela, width=350, height=50, bg=co1,  relief="flat",)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=350, height=90, bg=co1,  relief="solid",)
frameMeio.grid(row=1, column=0)

frameBaixo = Frame(janela,width=350, height=290,bg=co1, relief="raised")
frameBaixo.grid(row=2, column=0)

# Create a ScrolledFrame widget
sf = ScrolledFrame(frameBaixo, width=310, height=250,bg=co1)
sf.grid(row=0, column=0, sticky=NW, padx=0, pady=20)

# passando tudo para dentro da frame
framecanva = sf.display_widget(Frame, bg=co1)



# Logo -----------------------------------------------------

# abrindo imagem
app_img  = Image.open('logo.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=900,compound=LEFT, padx=5, relief=FLAT, anchor=NW,bg=co1, fg=co4)
app_logo.place(x=5, y=0)

app_ = Label(frameCima,text="Dicionário",compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 20'),bg=co1, fg=co4 )
app_.place(x=50, y=0)

l_linha = Label(frameCima, width=395, height=1,anchor=NW, font=('Verdana 1 '), bg=co3, fg=co1)
l_linha.place(x=0, y=47)


# funcao procurar e acessar a API
def procurar():

    # Obtendo a palavra
    palavra = e_palavra.get()

    l_palavra['text'] = palavra

    # link contendo a api
    api_link = "https://dicio-api-ten.vercel.app/v2/{}".format(palavra)

    # requests 
    r = requests.get(api_link)

    # convertendo os dados do request em dicionario
    dados = r.json()


    # dicionario para salvar o nome das variaveis dos frames
    frames = {}

    # contador de linhas para frame
    num_row = 0


    for i in range(len(dados)):
        # criando un novo frame e posicionar dentro do framecanva
        frames["F{}".format(i)] = i
        frames["F{}".format(i)] = Frame(framecanva, width=310, height=100, bg=co1)
        frames["F{}".format(i)].grid(row=num_row,column=0, sticky=NSEW, pady=2)

        # Significado 
        l_significado = Label(frames["F{}".format(num_row)], height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co0)
        l_significado.place(x=10, y=5)

        # Exemplos
        l_exemplo = Label(frames["F{}".format(num_row)], text="", wraplength=305,justify=LEFT, height=4,anchor=NW, font=('Ivy 9'), bg=co1, fg=co0)
        l_exemplo.place(x=10, y=30)

        # Passando o significado no label
        l_significado['text'] = (dados[i]['partOfSpeech'])

        # Passando Exemplos para o Label exemplos
        for j in dados[i]['meanings']:
            l_exemplo['text'] = (j)

        # incrementando o valor da linha
        num_row+= 1 



# Frame Meio --------------------------------------------------

l_palavra = Label(frameMeio, text="Digite a palavra", height=1,anchor=NW, font=('Ivy 10 '), bg=co1, fg=co4)
l_palavra.place(x=7, y=15)
e_palavra = Entry(frameMeio, width=18, font=('Ivy 14 '), justify='center',relief="solid")
e_palavra.place(x=10, y=41)

# botao procurar
img_procurar = Image.open('procurar.png')
img_procurar = img_procurar.resize((18, 18))
img_procurar = ImageTk.PhotoImage(img_procurar)
b_procurar = Button(frameMeio,command=procurar, image=img_procurar, compound=LEFT,width=100, text='  Procurar' ,bg=co1, fg=co0,font=('Ivy 11'), overrelief=RIDGE)
b_procurar.place(x=230, y=40)


# Label no frame baixo -------------------------------------------------------

l_palavra = Label(frameBaixo, text="",padx=10, width=37, height=1,anchor=NW, font=('Verdana 12 '), bg=co3, fg=co1)
l_palavra.place(x=0, y=0)


janela.mainloop()