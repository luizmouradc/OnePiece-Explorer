import json
import random

import customtkinter as ctk

from ui.personagem_view import PersonagemView
from ui.sidebar import Sidebar
from utils.caminhos import caminho_projeto


class OnePieceExplorer(ctk.CTk):
    LARGURA_JANELA = 1340
    ALTURA_JANELA = 820

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.title("One Piece Explorer V2")
        self.geometry(f"{self.LARGURA_JANELA}x{self.ALTURA_JANELA}")
        self.minsize(1120, 700)
        self.configure(fg_color="#07090D")

        self.personagens = self.carregar_personagens()
        self.personagem_atual = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(
            self,
            self.personagens,
            self.exibir_personagem,
            self.sortear_personagem,
        )
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.personagem_view = PersonagemView(
            self,
            total_personagens=len(self.personagens),
        )
        self.personagem_view.grid(
            row=0,
            column=1,
            sticky="nsew",
        )

        self.configurar_atalhos()
        self.after(10, self.centralizar_janela)

        if self.personagens:
            self.exibir_personagem(
                self.personagens[0],
                animar=False,
            )

    def carregar_personagens(self):
        caminho_json = caminho_projeto("data/personagens.json")

        try:
            with caminho_json.open("r", encoding="utf-8") as arquivo:
                personagens = json.load(arquivo)
        except (OSError, json.JSONDecodeError) as erro:
            raise RuntimeError(
                "Não foi possível carregar os dados dos personagens."
            ) from erro

        if not personagens:
            raise RuntimeError(
                "Nenhum personagem foi encontrado em personagens.json."
            )

        return personagens

    def centralizar_janela(self):
        self.update_idletasks()

        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()
        largura = self.winfo_width()
        altura = self.winfo_height()

        x = max(0, (largura_tela - largura) // 2)
        y = max(0, (altura_tela - altura) // 2)
        self.geometry(f"+{x}+{y}")

    def configurar_atalhos(self):
        for indice in range(min(9, len(self.personagens))):
            tecla = str(indice + 1)
            self.bind(
                tecla,
                lambda evento, i=indice: self.exibir_personagem(
                    self.personagens[i]
                ),
            )

        self.bind("<Left>", lambda evento: self.navegar_personagem(-1))
        self.bind("<Right>", lambda evento: self.navegar_personagem(1))
        self.bind("r", lambda evento: self.sortear_personagem())
        self.bind("R", lambda evento: self.sortear_personagem())

    def exibir_personagem(self, personagem, animar=True):
        if (
            self.personagem_atual
            and personagem["id"] == self.personagem_atual["id"]
        ):
            return

        self.personagem_atual = personagem
        indice = next(
            (
                i
                for i, item in enumerate(self.personagens)
                if item["id"] == personagem["id"]
            ),
            0,
        )

        self.sidebar.destacar(personagem)
        self.personagem_view.atualizar(
            personagem,
            indice=indice,
            animar=animar,
        )

    def navegar_personagem(self, direcao):
        if not self.personagem_atual:
            return

        indice_atual = next(
            (
                indice
                for indice, personagem in enumerate(self.personagens)
                if personagem["id"] == self.personagem_atual["id"]
            ),
            0,
        )

        proximo_indice = (indice_atual + direcao) % len(self.personagens)
        self.exibir_personagem(self.personagens[proximo_indice])

    def sortear_personagem(self):
        if len(self.personagens) <= 1:
            return

        opcoes = [
            personagem
            for personagem in self.personagens
            if not self.personagem_atual
            or personagem["id"] != self.personagem_atual["id"]
        ]

        self.exibir_personagem(random.choice(opcoes))
