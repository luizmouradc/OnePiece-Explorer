import customtkinter as ctk
from PIL import Image, ImageEnhance, ImageOps

from ui.info_panel import InfoPanel
from utils.caminhos import caminho_projeto


class PersonagemView(ctk.CTkFrame):
    TAMANHO_IMAGEM = (665, 416)

    def __init__(self, master):
        super().__init__(
            master,
            corner_radius=0,
            fg_color="#101218"
        )

        self.imagem_principal = None
        self.logo_atual = None
        self.imagem_pil_atual = None
        self.animacao_id = 0

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

        self.frame_info.grid_columnconfigure(
            0,
            weight=1
        )
        self.frame_info.grid_rowconfigure(
            6,
            weight=1
        )

        self.label_logo = ctk.CTkLabel(
            self.frame_info,
            text=""
        )
        self.label_logo.grid(
            row=0,
            column=0,
            sticky="w",
            padx=26,
            pady=(26, 16)
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
            pady=(0, 15)
        )
        self.barra_destaque.grid_propagate(False)

        self.label_nome = ctk.CTkLabel(
            self.frame_info,
            text="",
            font=ctk.CTkFont(
                size=32,
                weight="bold"
            ),
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
            font=ctk.CTkFont(size=15),
            text_color="#9CA3AF",
            anchor="w",
            justify="left"
        )
        self.label_epiteto.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=27,
            pady=(3, 14)
        )

        self.badge_cargo = ctk.CTkLabel(
            self.frame_info,
            text="",
            height=32,
            corner_radius=9,
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            text_color="#FFFFFF",
            anchor="w"
        )
        self.badge_cargo.grid(
            row=4,
            column=0,
            sticky="w",
            padx=26,
            pady=(0, 18)
        )

        self.info_panel = InfoPanel(
            self.frame_info
        )
        self.info_panel.grid(
            row=5,
            column=0,
            sticky="nsew",
            padx=22,
            pady=(0, 18)
        )

        self.label_etapa = ctk.CTkLabel(
            self.frame_info,
            text="V2 • interface em desenvolvimento",
            font=ctk.CTkFont(size=11),
            text_color="#5F6672"
        )
        self.label_etapa.grid(
            row=6,
            column=0,
            sticky="sw",
            padx=27,
            pady=(0, 20)
        )

    @staticmethod
    def tamanho_logo(
        imagem,
        largura_maxima=300,
        altura_maxima=110
    ):
        largura, altura = imagem.size

        escala = min(
            largura_maxima / largura,
            altura_maxima / altura
        )

        return (
            max(1, int(largura * escala)),
            max(1, int(altura * escala))
        )

    def preparar_imagem(self, personagem):
        imagem = Image.open(
            caminho_projeto(
                personagem["imagem"]
            )
        ).convert("RGB")

        imagem = ImageOps.fit(
            imagem,
            self.TAMANHO_IMAGEM,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5)
        )

        # Um leve escurecimento deixa o visual menos estourado
        # e combina melhor com o tema da interface.
        return ImageEnhance.Brightness(
            imagem
        ).enhance(0.94)

    def aplicar_imagem(self, imagem):
        self.imagem_principal = ctk.CTkImage(
            light_image=imagem,
            dark_image=imagem,
            size=self.TAMANHO_IMAGEM
        )
        self.label_imagem.configure(
            image=self.imagem_principal
        )

    def animar_troca_imagem(
        self,
        imagem_nova
    ):
        self.animacao_id += 1
        animacao_atual = self.animacao_id

        if self.imagem_pil_atual is None:
            self.aplicar_imagem(imagem_nova)
            self.imagem_pil_atual = imagem_nova
            return

        imagem_anterior = self.imagem_pil_atual

        frames = 7
        intervalo = 28

        def mostrar_frame(indice):
            if animacao_atual != self.animacao_id:
                return

            fator = indice / frames

            frame = Image.blend(
                imagem_anterior,
                imagem_nova,
                fator
            )
            self.aplicar_imagem(frame)

            if indice < frames:
                self.after(
                    intervalo,
                    lambda: mostrar_frame(
                        indice + 1
                    )
                )
            else:
                self.imagem_pil_atual = imagem_nova

        mostrar_frame(1)

    def atualizar(
        self,
        personagem,
        animar=True
    ):
        cor_principal = personagem[
            "tema"
        ]["principal"]

        cor_secundaria = personagem[
            "tema"
        ]["secundaria"]

        imagem_nova = self.preparar_imagem(
            personagem
        )

        if animar:
            self.animar_troca_imagem(
                imagem_nova
            )
        else:
            self.animacao_id += 1
            self.aplicar_imagem(imagem_nova)
            self.imagem_pil_atual = imagem_nova

        logo = Image.open(
            caminho_projeto(
                personagem["logo"]
            )
        ).convert("RGBA")

        tamanho_logo = self.tamanho_logo(
            logo
        )

        self.logo_atual = ctk.CTkImage(
            light_image=logo,
            dark_image=logo,
            size=tamanho_logo
        )
        self.label_logo.configure(
            image=self.logo_atual
        )

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
        self.barra_destaque.configure(
            fg_color=cor_secundaria
        )

        self.info_panel.atualizar_personagem(
            personagem
        )
