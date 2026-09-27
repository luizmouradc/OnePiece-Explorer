import json

import customtkinter as ctk

from ui.personagem_view import PersonagemView
from ui.sidebar import Sidebar
from utils.caminhos import caminho_projeto


class OnePieceExplorer(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("One Piece Explorer V2")
        self.geometry("1240x760")
        self.minsize(1120, 680)
        self.configure(fg_color="#101218")

        self.personagens = self.carregar_personagens()
        self.personagem_atual = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(
            self,
            self.personagens,
            self.exibir_personagem
        )
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.personagem_view = PersonagemView(self)
        self.personagem_view.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        if self.personagens:
            self.exibir_personagem(self.personagens[0])

    def carregar_personagens(self):
        caminho_json = caminho_projeto("data/personagens.json")

        with caminho_json.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    def exibir_personagem(self, personagem):
        self.personagem_atual = personagem
        self.sidebar.destacar(personagem)
        self.personagem_view.atualizar(personagem)
