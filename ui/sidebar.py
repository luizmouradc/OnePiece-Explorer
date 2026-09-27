import customtkinter as ctk
from PIL import Image

from utils.caminhos import caminho_projeto


class Sidebar(ctk.CTkFrame):
    def __init__(
        self,
        master,
        personagens,
        ao_selecionar,
        ao_sortear
    ):
        super().__init__(
            master,
            width=190,
            corner_radius=0,
            fg_color="#0B0D12"
        )

        self.personagens = personagens
        self.ao_selecionar = ao_selecionar
        self.ao_sortear = ao_sortear

        self.botoes = {}
        self.icones = {}

        self.grid_propagate(False)

        self.criar_cabecalho()
        self.criar_botoes()
        self.criar_rodape()

    def criar_cabecalho(self):
        titulo = ctk.CTkLabel(
            self,
            text="ONE PIECE\nEXPLORER",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color="#F5F5F5",
            justify="left"
        )
        titulo.pack(
            padx=18,
            pady=(28, 6),
            anchor="w"
        )

        subtitulo = ctk.CTkLabel(
            self,
            text="Escolha um personagem",
            font=ctk.CTkFont(size=11),
            text_color="#7D8590"
        )
        subtitulo.pack(
            padx=18,
            pady=(0, 22),
            anchor="w"
        )

    def criar_botoes(self):
        self.frame_personagens = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.frame_personagens.pack(
            fill="x"
        )

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
                self.frame_personagens,
                text=nome_curto,
                image=icone,
                compound="left",
                height=58,
                corner_radius=12,
                anchor="w",
                font=ctk.CTkFont(
                    size=13,
                    weight="bold"
                ),
                fg_color="transparent",
                hover_color="#181C24",
                border_width=1,
                border_color="#1C222D",
                command=lambda p=personagem: self.ao_selecionar(p)
            )
            botao.pack(
                fill="x",
                padx=14,
                pady=5
            )

            self.botoes[personagem["id"]] = botao

    def criar_rodape(self):
        separador = ctk.CTkFrame(
            self,
            height=1,
            fg_color="#202631"
        )
        separador.pack(
            side="bottom",
            fill="x",
            padx=16,
            pady=(0, 14)
        )

        botao_aleatorio = ctk.CTkButton(
            self,
            text="🎲  Surpreenda-me",
            height=42,
            corner_radius=11,
            font=ctk.CTkFont(
                size=12,
                weight="bold"
            ),
            fg_color="#171B23",
            hover_color="#242B36",
            border_width=1,
            border_color="#2A313D",
            command=self.ao_sortear
        )
        botao_aleatorio.pack(
            side="bottom",
            fill="x",
            padx=14,
            pady=(0, 12)
        )

        texto = ctk.CTkLabel(
            self,
            text="One Piece Explorer V2",
            font=ctk.CTkFont(size=10),
            text_color="#555D69"
        )
        texto.pack(
            side="bottom",
            pady=(8, 8)
        )

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
