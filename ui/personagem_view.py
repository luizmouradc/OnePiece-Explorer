import customtkinter as ctk
from PIL import Image

from utils.caminhos import caminho_projeto


class PersonagemView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            corner_radius=0,
            fg_color="#101218"
        )

        self.imagem_principal = None
        self.logo_atual = None

        self.grid_columnconfigure(0, weight=3)
        self.grid_columnconfigure(1, weight=2)
        self.grid_rowconfigure(0, weight=1)

        self.criar_area_imagem()
        self.criar_area_info()

    def criar_area_imagem(self):
        self.frame_imagem = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="#161A22",
            border_width=1,
            border_color="#242B36"
        )
        self.frame_imagem.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(26, 12),
            pady=26
        )

        self.label_imagem = ctk.CTkLabel(
            self.frame_imagem,
            text=""
        )
        self.label_imagem.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=10
        )

    def criar_area_info(self):
        self.frame_info = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="#14171E",
            border_width=1,
            border_color="#242B36"
        )
        self.frame_info.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(12, 26),
            pady=26
        )

        self.frame_info.grid_columnconfigure(0, weight=1)

        self.label_logo = ctk.CTkLabel(
            self.frame_info,
            text=""
        )
        self.label_logo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=26,
            pady=(30, 22)
        )

        self.barra_destaque = ctk.CTkFrame(
            self.frame_info,
            width=54,
            height=4,
            corner_radius=2,
            fg_color="#D62828"
        )
        self.barra_destaque.grid(
            row=1,
            column=0,
            sticky="w",
            padx=28,
            pady=(0, 18)
        )
        self.barra_destaque.grid_propagate(False)

        self.label_nome = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=34, weight="bold"),
            text_color="#FFFFFF",
            anchor="w",
            justify="left"
        )
        self.label_nome.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=26
        )

        self.label_epiteto = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=16),
            text_color="#9CA3AF",
            anchor="w",
            justify="left"
        )
        self.label_epiteto.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=27,
            pady=(3, 18)
        )

        self.badge_cargo = ctk.CTkLabel(
            self.frame_info,
            text="",
            height=34,
            corner_radius=9,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#FFFFFF",
            anchor="w"
        )
        self.badge_cargo.grid(
            row=4,
            column=0,
            sticky="w",
            padx=26,
            pady=(0, 22)
        )

        titulo_descricao = ctk.CTkLabel(
            self.frame_info,
            text="VISÃO GERAL",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color="#737B88",
            anchor="w"
        )
        titulo_descricao.grid(
            row=5,
            column=0,
            sticky="ew",
            padx=27,
            pady=(0, 8)
        )

        self.label_descricao = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#D6DAE1",
            anchor="nw",
            justify="left",
            wraplength=350
        )
        self.label_descricao.grid(
            row=6,
            column=0,
            sticky="new",
            padx=27,
            pady=(0, 24)
        )

        self.label_etapa = ctk.CTkLabel(
            self.frame_info,
            text="V2 • interface em desenvolvimento",
            font=ctk.CTkFont(size=11),
            text_color="#5F6672"
        )
        self.label_etapa.grid(
            row=7,
            column=0,
            sticky="sw",
            padx=27,
            pady=(20, 24)
        )

        self.frame_info.grid_rowconfigure(7, weight=1)

    @staticmethod
    def tamanho_logo(imagem, largura_maxima=315, altura_maxima=125):
        largura, altura = imagem.size

        escala = min(
            largura_maxima / largura,
            altura_maxima / altura
        )

        return (
            max(1, int(largura * escala)),
            max(1, int(altura * escala))
        )

    def atualizar(self, personagem):
        cor_principal = personagem["tema"]["principal"]
        cor_secundaria = personagem["tema"]["secundaria"]

        imagem = Image.open(
            caminho_projeto(personagem["imagem"])
        ).convert("RGB")

        self.imagem_principal = ctk.CTkImage(
            light_image=imagem,
            dark_image=imagem,
            size=(665, 416)
        )
        self.label_imagem.configure(image=self.imagem_principal)

        logo = Image.open(
            caminho_projeto(personagem["logo"])
        ).convert("RGBA")

        tamanho_logo = self.tamanho_logo(logo)

        self.logo_atual = ctk.CTkImage(
            light_image=logo,
            dark_image=logo,
            size=tamanho_logo
        )
        self.label_logo.configure(image=self.logo_atual)

        self.label_nome.configure(
            text=personagem["nome"],
            text_color=cor_principal
        )
        self.label_epiteto.configure(
            text=f'“{personagem["epiteto"]}”'
        )
        self.badge_cargo.configure(
            text=f'   {personagem["cargo"]}   ',
            fg_color=cor_principal
        )
        self.label_descricao.configure(
            text=personagem["descricao"]
        )

        self.barra_destaque.configure(
            fg_color=cor_secundaria
        )
