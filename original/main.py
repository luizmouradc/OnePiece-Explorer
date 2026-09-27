from tkinter import *
from tkinter import ttk

# importando biblioteca para importar fotos
from PIL import Image, ImageTk

from dados import *

# cores 
co0 = "#0c0c12"  # Preta
co1 = "#feffff"  # branca

# criando janela
janela = Tk()
janela.title('')
janela.geometry('550x510')
janela.configure(bg=co0)

ttk.Separator(janela , orient=HORIZONTAL).grid(row=0, columnspan=1 , ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

# criando frame
frame_personagem = Frame(janela, width=550, height=290, relief='flat')
frame_personagem.grid(row=1, column=0)

def trocar_pokemon(i):

    global imagem_personagem, personagem_imagem , logo , logo_label

    # nome do personagem
    personagem_nome['text'] = i

    imagem_personagem = personagem[i]["imagem"]
    foto = imagem_personagem

    # imagem do personagem
    imagem_personagem = Image.open(foto)
    imagem_personagem = imagem_personagem.resize((570, 300))
    imagem_personagem = ImageTk.PhotoImage(imagem_personagem)
    
    personagem_imagem = Label(frame_personagem,image=imagem_personagem,relief='flat',bg=co0,fg=co1)
    personagem_imagem.place(x=0 , y=0)

    # definiçao
    personagem_cargo['text'] = personagem[i]['status'][0]
    personagem_HouA['text'] = personagem[i]['status'][1]
    personagem_objetivo['text'] = personagem[i]['status'][2]

    # colocando a logo do "one piece" ----------
    logo = personagem[i]["logo"]

    logo = Image.open(logo)
    logo = logo.resize((210,90))
    logo = ImageTk.PhotoImage(logo)
    
    logo_label = Label(janela, image=logo,relief='flat',bg=co0, fg=co0)
    logo_label.place(x=15,y=355)

#logo.lift()  pra logo ficar emcima da foto

# Nome
personagem_nome = Label(janela, text='Monkey D. Luffy', relief='flat', anchor='w', justify='left', font='verdana 20 bold', bg=co0, fg=co1)
personagem_nome.place(x=245, y=300)

# Cargo
personagem_cargo = Label(janela, text='Cargo: Capitão', relief='flat', anchor='w', justify='left', font='verdana 10', bg=co0, fg=co1)
personagem_cargo.place(x=245, y=340)  # Ajuste da posição vertical (y)

# Habilidades / Akuma no Mi
personagem_HouA = Label(janela, text='Akuma no Mi: Comeu a Gomu Gomu no Mi, tornando-se um Homem-Borracha com habilidades elásticas.', relief='flat', anchor='w', justify='left', font='verdana 10', bg=co0, fg=co1, wraplength=300)
personagem_HouA.place(x=245, y=360)

# Objetivo
personagem_objetivo = Label(janela, text='Objetivo : Tornar-se o Rei dos Piratas e encontrar o tesouro One Piece.', relief='flat', anchor='w', justify='left', font='verdana 10', bg=co0, fg=co1, wraplength=300)
personagem_objetivo.place(x=245, y=415)

# criando botao para os personagens --------------------------

# botao luffy
caveira_luffy = Image.open('OnePiece Explorer/imagens/caveira do luffy.jpg')
caveira_luffy = caveira_luffy.resize((45, 45))
caveira_luffy = ImageTk.PhotoImage(caveira_luffy)

butao_luffy = Button(janela,command=lambda:trocar_pokemon('Monkey D. Luffy') ,image=caveira_luffy ,relief='raised',padx=5, overrelief=RIDGE ,anchor=NW,bg=co0 , fg= co1)
butao_luffy.place(x=5 , y=10)

# botao zoro
caveira_zoro = Image.open('OnePiece Explorer/imagens/caveira do zoro.jpg')
caveira_zoro = caveira_zoro.resize((45, 45))
caveira_zoro = ImageTk.PhotoImage(caveira_zoro)

butao_zoro = Button(janela, command=lambda:trocar_pokemon('Roronoa Zoro') ,image=caveira_zoro ,relief='raised',padx=5, overrelief=RIDGE ,anchor=NW,bg=co0 , fg= co1)
butao_zoro.place(x=5 , y=65)

# botao nami
caveira_nami = Image.open('OnePiece Explorer/imagens/caveira da nami.jpg')
caveira_nami = caveira_nami.resize((45, 45))
caveira_nami = ImageTk.PhotoImage(caveira_nami)

butao_nami= Button(janela, command=lambda:trocar_pokemon('Nami') ,image=caveira_nami ,relief='raised',padx=5, overrelief=RIDGE ,anchor=NW,bg=co0 , fg= co1)
butao_nami.place(x=5 , y=120)

# botao sanji
caveira_sanji = Image.open('OnePiece Explorer/imagens/caveira do sanji.jpg')
caveira_sanji = caveira_sanji.resize((45, 45))
caveira_sanji = ImageTk.PhotoImage(caveira_sanji)

butao_sanji = Button(janela,command=lambda:trocar_pokemon('Sanji') , image=caveira_sanji ,relief='raised',padx=5, overrelief=RIDGE ,anchor=NW,bg=co0 , fg= co1)
butao_sanji.place(x=5 , y=175)

# botao chopper
caveira_chopper = Image.open('OnePiece Explorer/imagens/caveira do chopper.jpg')
caveira_chopper = caveira_chopper.resize((45, 45))
caveira_chopper = ImageTk.PhotoImage(caveira_chopper)

butao_chopper = Button(janela,command=lambda:trocar_pokemon('Tony Tony Chopper') , image=caveira_chopper ,relief='raised',padx=5, overrelief=RIDGE ,anchor=NW,bg=co0 , fg= co1)
butao_chopper.place(x=5 , y=230)

trocar_pokemon('Monkey D. Luffy')

# Impede a redimensionamento vertical e horizontal
janela.resizable(False, False)

janela.mainloop()
