import customtkinter as ctk
from PIL import Image

from utils.caminhos import caminho_projeto


class Sidebar(ctk.CTkFrame):
    def __init__(self, master, personagens, ao_selecionar):
        super().__init__(
            master,
            width=185,
            corner_radius=0,
            fg_color="#0B0D12"
        )

        self.personagens = personagens
        self.ao_selecionar = ao_selecionar
        self.botoes = {}
        self.icones = {}

        self.grid_propagate(False)

        self.criar_cabecalho()
        self.criar_botoes()

    def criar_cabecalho(self):
        titulo = ctk.CTkLabel(
            self,
            text="ONE PIECE\nEXPLORER",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#F5F5F5",
            justify="left"
        )
        titulo.pack(padx=18, pady=(28, 6), anchor="w")

        subtitulo = ctk.CTkLabel(
            self,
            text="Escolha um personagem",
            font=ctk.CTkFont(size=11),
            text_color="#7D8590"
        )
        subtitulo.pack(padx=18, pady=(0, 24), anchor="w")

    def criar_botoes(self):
        for personagem in self.personagens:
            imagem = Image.open(
                caminho_projeto(personagem["icone"])
            ).convert("RGB")

            icone = ctk.CTkImage(
                light_image=imagem,
                dark_image=imagem,
                size=(45, 43)
            )
            self.icones[personagem["id"]] = icone

            nome_curto = personagem["id"].capitalize()

            botao = ctk.CTkButton(
                self,
                text=nome_curto,
                image=icone,
                compound="left",
                height=58,
                corner_radius=12,
                anchor="w",
                font=ctk.CTkFont(size=13, weight="bold"),
                fg_color="transparent",
                hover_color="#181C24",
                border_width=1,
                border_color="#1C222D",
                command=lambda p=personagem: self.ao_selecionar(p)
            )
            botao.pack(fill="x", padx=14, pady=5)

            self.botoes[personagem["id"]] = botao

    def destacar(self, personagem):
        for botao in self.botoes.values():
            botao.configure(
                fg_color="transparent",
                border_color="#1C222D",
                text_color="#D4D7DD"
            )

        botao_ativo = self.botoes[personagem["id"]]
        cor = personagem["tema"]["principal"]

        botao_ativo.configure(
            fg_color=cor,
            border_color=cor,
            text_color="#FFFFFF"
        )
