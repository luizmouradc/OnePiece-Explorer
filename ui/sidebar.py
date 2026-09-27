import customtkinter as ctk
from PIL import Image, ImageDraw, ImageEnhance, ImageOps

from utils.caminhos import caminho_projeto


class Sidebar(ctk.CTkFrame):
    """Índice lateral da Grand Line com acabamento editorial."""

    LARGURA = 236
    COR_BASE = "#080A0E"

    def __init__(
        self,
        master,
        personagens,
        ao_selecionar,
        ao_sortear,
    ):
        super().__init__(
            master,
            width=self.LARGURA,
            corner_radius=0,
            fg_color=self.COR_BASE,
        )

        self.personagens = personagens
        self.ao_selecionar = ao_selecionar
        self.ao_sortear = ao_sortear
        self.selecionado = None

        self.linhas = {}
        self.barras = {}
        self.icones = {}
        self.rotulos_numero = {}
        self.rotulos_nome = {}
        self.rotulos_icone = {}

        self.grid_propagate(False)

        self.criar_cabecalho()
        self.criar_botoes()
        self.criar_rodape()

    @staticmethod
    def _rgb(cor):
        cor = cor.lstrip("#")
        return tuple(int(cor[i:i + 2], 16) for i in (0, 2, 4))

    @classmethod
    def _misturar(cls, base, destaque, proporcao):
        base_rgb = cls._rgb(base)
        destaque_rgb = cls._rgb(destaque)
        mistura = tuple(
            int(a + (b - a) * proporcao)
            for a, b in zip(base_rgb, destaque_rgb)
        )
        return "#" + "".join(f"{canal:02X}" for canal in mistura)

    def criar_cabecalho(self):
        etiqueta = ctk.CTkLabel(
            self,
            text="GRAND LINE  /  DATABASE",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color="#626A75",
        )
        etiqueta.pack(
            padx=20,
            pady=(24, 5),
            anchor="w",
        )

        titulo = ctk.CTkLabel(
            self,
            text="ONE PIECE\nEXPLORER",
            font=ctk.CTkFont(size=21, weight="bold"),
            text_color="#F4F5F7",
            justify="left",
        )
        titulo.pack(
            padx=20,
            pady=(0, 8),
            anchor="w",
        )

        meta = ctk.CTkFrame(self, fg_color="transparent")
        meta.pack(fill="x", padx=20, pady=(0, 20))

        ctk.CTkLabel(
            meta,
            text="CHARACTER ARCHIVE",
            font=ctk.CTkFont(size=8),
            text_color="#69717C",
        ).pack(side="left")

        ctk.CTkLabel(
            meta,
            text="V2.0",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color="#8A919B",
        ).pack(side="right")

        self.separador_topo = ctk.CTkFrame(
            self,
            height=1,
            fg_color="#1B1E24",
        )
        self.separador_topo.pack(
            fill="x",
            padx=18,
            pady=(0, 14),
        )

        secao = ctk.CTkFrame(self, fg_color="transparent")
        secao.pack(fill="x", padx=20, pady=(0, 6))

        ctk.CTkLabel(
            secao,
            text="CREW INDEX",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color="#626A75",
        ).pack(side="left")

        ctk.CTkLabel(
            secao,
            text=f"{len(self.personagens):02d} FILES",
            font=ctk.CTkFont(size=8, weight="bold"),
            text_color="#4D5560",
        ).pack(side="right")

    def _criar_medalhao(self, personagem):
        tamanho = 44
        borda = 2
        interno = 36

        imagem = Image.open(
            caminho_projeto(personagem["icone"])
        ).convert("RGB")
        imagem = ImageOps.fit(
            imagem,
            (interno, interno),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        imagem = ImageEnhance.Brightness(imagem).enhance(1.04)
        imagem = ImageEnhance.Contrast(imagem).enhance(1.06)

        saida = Image.new("RGBA", (tamanho, tamanho), (0, 0, 0, 0))
        draw = ImageDraw.Draw(saida)

        cor = self._rgb(personagem["tema"]["principal"])
        cor_anel = (*cor, 210)
        draw.ellipse(
            (1, 1, tamanho - 2, tamanho - 2),
            fill=(9, 11, 15, 245),
            outline=cor_anel,
            width=borda,
        )

        mascara = Image.new("L", (interno, interno), 0)
        ImageDraw.Draw(mascara).ellipse(
            (0, 0, interno - 1, interno - 1),
            fill=255,
        )

        pos = ((tamanho - interno) // 2, (tamanho - interno) // 2)
        saida.paste(imagem, pos, mascara)

        # Aro interno escuro para integrar logos que originalmente têm fundo preto.
        draw.ellipse(
            (
                pos[0] - 1,
                pos[1] - 1,
                pos[0] + interno,
                pos[1] + interno,
            ),
            outline=(255, 255, 255, 24),
            width=1,
        )

        return ctk.CTkImage(
            light_image=saida,
            dark_image=saida,
            size=(40, 40),
        )

    def _registrar_eventos(self, widgets, personagem):
        identificador = personagem["id"]

        def selecionar(evento=None):
            self.ao_selecionar(personagem)

        def entrar(evento=None):
            if identificador != self.selecionado:
                self.linhas[identificador].configure(fg_color="#11151B")

        def sair(evento=None):
            if identificador != self.selecionado:
                self.linhas[identificador].configure(fg_color="transparent")

        for widget in widgets:
            widget.bind("<Button-1>", selecionar)
            widget.bind("<Enter>", entrar)
            widget.bind("<Leave>", sair)

    def criar_botoes(self):
        self.frame_personagens = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        self.frame_personagens.pack(fill="x")

        for indice, personagem in enumerate(self.personagens, start=1):
            linha = ctk.CTkFrame(
                self.frame_personagens,
                height=54,
                corner_radius=11,
                fg_color="transparent",
            )
            linha.pack(
                fill="x",
                padx=11,
                pady=2,
            )
            linha.pack_propagate(False)

            barra = ctk.CTkFrame(
                linha,
                width=2,
                height=34,
                corner_radius=2,
                fg_color="transparent",
            )
            barra.pack(
                side="left",
                padx=(5, 7),
                pady=10,
            )
            barra.pack_propagate(False)

            icone = self._criar_medalhao(personagem)
            self.icones[personagem["id"]] = icone

            rotulo_icone = ctk.CTkLabel(
                linha,
                text="",
                image=icone,
                width=42,
                height=42,
            )
            rotulo_icone.pack(side="left", padx=(0, 7), pady=6)

            numero = ctk.CTkLabel(
                linha,
                text=f"{indice:02d}",
                width=25,
                anchor="w",
                font=ctk.CTkFont(size=10, weight="bold"),
                text_color="#69717B",
            )
            numero.pack(side="left", padx=(0, 4))

            nome = ctk.CTkLabel(
                linha,
                text=personagem["id"].capitalize(),
                anchor="w",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color="#C9CDD3",
            )
            nome.pack(side="left", fill="x", expand=True, padx=(0, 8))

            self.linhas[personagem["id"]] = linha
            self.barras[personagem["id"]] = barra
            self.rotulos_icone[personagem["id"]] = rotulo_icone
            self.rotulos_numero[personagem["id"]] = numero
            self.rotulos_nome[personagem["id"]] = nome

            self._registrar_eventos(
                [linha, barra, rotulo_icone, numero, nome],
                personagem,
            )

    def criar_rodape(self):
        self.botao_aleatorio = ctk.CTkButton(
            self,
            text="✦  SURPREENDA-ME   ·   R",
            height=41,
            corner_radius=9,
            font=ctk.CTkFont(size=10, weight="bold"),
            fg_color="#101318",
            hover_color="#171B21",
            border_width=1,
            border_color="#2A3038",
            text_color="#ECEEF1",
            command=self.ao_sortear,
        )
        self.botao_aleatorio.pack(
            side="bottom",
            fill="x",
            padx=16,
            pady=(0, 16),
        )

        atalhos = ctk.CTkLabel(
            self,
            text="← → navegar   ·   1–5 selecionar\nR aleatório",
            font=ctk.CTkFont(size=8),
            text_color="#545C67",
            justify="left",
        )
        atalhos.pack(
            side="bottom",
            padx=20,
            pady=(0, 12),
            anchor="w",
        )

        self.separador_rodape = ctk.CTkFrame(
            self,
            height=1,
            fg_color="#1B1E24",
        )
        self.separador_rodape.pack(
            side="bottom",
            fill="x",
            padx=18,
            pady=(0, 12),
        )

    def destacar(self, personagem):
        self.selecionado = personagem["id"]
        cor = personagem["tema"]["principal"]

        # Um leve banho da cor do personagem integra sidebar e hero sem virar neon.
        ambiente = self._misturar(self.COR_BASE, cor, 0.055)
        linha_sutil = self._misturar("#1B1E24", cor, 0.12)
        borda_botao = self._misturar("#2A3038", cor, 0.28)

        self.configure(fg_color=ambiente)
        self.separador_topo.configure(fg_color=linha_sutil)
        self.separador_rodape.configure(fg_color=linha_sutil)
        self.botao_aleatorio.configure(border_color=borda_botao)

        for identificador in self.linhas:
            self.linhas[identificador].configure(fg_color="transparent")
            self.barras[identificador].configure(fg_color="transparent")
            self.rotulos_numero[identificador].configure(text_color="#69717B")
            self.rotulos_nome[identificador].configure(text_color="#C9CDD3")

        self.linhas[self.selecionado].configure(fg_color="#11151A")
        self.barras[self.selecionado].configure(fg_color=cor)
        self.rotulos_numero[self.selecionado].configure(text_color=cor)
        self.rotulos_nome[self.selecionado].configure(text_color="#FFFFFF")
