import json

import customtkinter as ctk
from PIL import Image

from utils.caminhos import caminho_projeto


class OnePieceExplorer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("One Piece Explorer V2")
        self.geometry("1100x680")
        self.minsize(900, 600)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.personagens = self.carregar_personagens()
        self.personagem_atual = None
        self.imagem_atual = None

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.criar_sidebar()
        self.criar_area_principal()

        if self.personagens:
            self.exibir_personagem(self.personagens[0])

    def carregar_personagens(self):
        caminho_json = caminho_projeto("data/personagens.json")

        with caminho_json.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)

    def criar_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=190, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        titulo = ctk.CTkLabel(
            self.sidebar,
            text="ONE PIECE\nEXPLORER",
            font=ctk.CTkFont(size=22, weight="bold"),
            justify="left"
        )
        titulo.pack(padx=20, pady=(28, 24), anchor="w")

        for personagem in self.personagens:
            botao = ctk.CTkButton(
                self.sidebar,
                text=personagem["nome"],
                height=42,
                anchor="w",
                command=lambda p=personagem: self.exibir_personagem(p)
            )
            botao.pack(fill="x", padx=15, pady=5)

    def criar_area_principal(self):
        self.area_principal = ctk.CTkFrame(self, corner_radius=0)
        self.area_principal.grid(row=0, column=1, sticky="nsew")

        self.area_principal.grid_columnconfigure(0, weight=1)
        self.area_principal.grid_columnconfigure(1, weight=1)
        self.area_principal.grid_rowconfigure(0, weight=1)

        self.frame_imagem = ctk.CTkFrame(self.area_principal)
        self.frame_imagem.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(24, 12),
            pady=24
        )

        self.label_imagem = ctk.CTkLabel(
            self.frame_imagem,
            text=""
        )
        self.label_imagem.pack(expand=True, fill="both", padx=12, pady=12)

        self.frame_info = ctk.CTkFrame(self.area_principal)
        self.frame_info.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(12, 24),
            pady=24
        )

        self.label_nome = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=30, weight="bold"),
            anchor="w",
            justify="left"
        )
        self.label_nome.pack(fill="x", padx=24, pady=(30, 4))

        self.label_epiteto = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=16),
            anchor="w",
            justify="left"
        )
        self.label_epiteto.pack(fill="x", padx=24, pady=(0, 18))

        self.label_cargo = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=15, weight="bold"),
            anchor="w",
            justify="left"
        )
        self.label_cargo.pack(fill="x", padx=24, pady=(0, 12))

        self.label_descricao = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=14),
            anchor="nw",
            justify="left",
            wraplength=380
        )
        self.label_descricao.pack(fill="x", padx=24, pady=(0, 20))

        self.label_status = ctk.CTkLabel(
            self.frame_info,
            text="Etapa 2: estrutura funcional",
            font=ctk.CTkFont(size=12),
            text_color="gray70"
        )
        self.label_status.pack(side="bottom", padx=24, pady=20, anchor="w")

    def exibir_personagem(self, personagem):
        self.personagem_atual = personagem

        self.label_nome.configure(text=personagem["nome"])
        self.label_epiteto.configure(text=f'“{personagem["epiteto"]}”')
        self.label_cargo.configure(text=personagem["cargo"])
        self.label_descricao.configure(text=personagem["descricao"])

        cor_principal = personagem["tema"]["principal"]
        self.label_nome.configure(text_color=cor_principal)

        caminho_imagem = caminho_projeto(personagem["imagem"])
        imagem_pil = Image.open(caminho_imagem)

        self.imagem_atual = ctk.CTkImage(
            light_image=imagem_pil,
            dark_image=imagem_pil,
            size=(420, 560)
        )

        self.label_imagem.configure(image=self.imagem_atual)
