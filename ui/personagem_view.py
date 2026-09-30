import tkinter as tk
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageOps, ImageTk
import customtkinter as ctk

from ui.info_panel import InfoPanel
from utils.caminhos import caminho_projeto


class PersonagemView(ctk.CTkFrame):
    """Hero cinematográfico do personagem."""

    TAMANHO_FALLBACK = (1050, 760)

    def __init__(self, master, total_personagens=5):
        super().__init__(master, corner_radius=0, fg_color="#07090D")

        self.total_personagens = total_personagens
        self.personagem_atual = None
        self.indice_atual = 0

        self.imagem_original = None
        self.logo_original = None
        self.imagem_pil_atual = None

        self.background_photo = None
        self.logo_photo = None
        self.background_item = None

        self.animacao_id = 0
        self.resize_job = None
        self.entrada_job = None

        self.canvas = tk.Canvas(
            self,
            bg="#07090D",
            bd=0,
            highlightthickness=0,
            relief="flat",
        )
        self.canvas.pack(fill="both", expand=True)

        self.info_panel = InfoPanel(
            self.canvas,
            ao_mudar=self.redesenhar_conteudo,
        )

        self.canvas.bind("<Configure>", self.ao_redimensionar)

    @staticmethod
    def _hex_para_rgb(cor):
        cor = cor.lstrip("#")
        return tuple(int(cor[i:i + 2], 16) for i in (0, 2, 4))

    def tamanho_canvas(self):
        largura = self.canvas.winfo_width()
        altura = self.canvas.winfo_height()

        if largura < 200 or altura < 200:
            return self.TAMANHO_FALLBACK

        return largura, altura

    def preparar_background(self, tamanho):
        largura, altura = tamanho

        visual = self.personagem_atual.get("visual", {})
        foco_x = float(visual.get("foco_x", 0.56))
        foco_y = float(visual.get("foco_y", 0.50))
        brilho = float(visual.get("brilho", 0.80))

        imagem = ImageOps.fit(
            self.imagem_original,
            (largura, altura),
            method=Image.Resampling.LANCZOS,
            centering=(foco_x, foco_y),
        )

        imagem = ImageEnhance.Brightness(imagem).enhance(brilho)
        imagem = ImageEnhance.Contrast(imagem).enhance(1.04)
        imagem = ImageEnhance.Color(imagem).enhance(0.96)
        imagem = imagem.convert("RGBA")

        # Escurecimento geral muito leve para unir arte e interface.
        geral = Image.new("RGBA", imagem.size, (3, 5, 8, 28))
        imagem = Image.alpha_composite(imagem, geral)

        # Glow temático suave atrás da arte.
        cor_tema = self._hex_para_rgb(
            self.personagem_atual["tema"]["principal"]
        )
        glow_mask = Image.new("L", imagem.size, 0)
        glow_draw = ImageDraw.Draw(glow_mask)
        raio_x = int(largura * 0.28)
        raio_y = int(altura * 0.43)
        centro_x = int(largura * 0.78)
        centro_y = int(altura * 0.42)
        glow_draw.ellipse(
            (
                centro_x - raio_x,
                centro_y - raio_y,
                centro_x + raio_x,
                centro_y + raio_y,
            ),
            fill=58,
        )
        glow_mask = glow_mask.filter(
            ImageFilter.GaussianBlur(max(80, int(largura * 0.08)))
        )
        glow = Image.new("RGBA", imagem.size, (*cor_tema, 0))
        glow.putalpha(glow_mask)
        imagem = Image.alpha_composite(imagem, glow)

        # Gradiente lateral: informações entram na própria arte, sem painel.
        mascara_lateral = Image.new("L", (largura, 1))
        pixels = []
        fim_forte = 0.18
        fim_gradiente = 0.72

        for px in range(largura):
            pos = px / max(1, largura - 1)
            if pos <= fim_forte:
                alpha = 238
            elif pos >= fim_gradiente:
                alpha = 0
            else:
                progresso = (pos - fim_forte) / (fim_gradiente - fim_forte)
                alpha = int(238 * ((1 - progresso) ** 1.65))
            pixels.append(alpha)

        mascara_lateral.putdata(pixels)
        mascara_lateral = mascara_lateral.resize((largura, altura))
        lateral = Image.new("RGBA", imagem.size, (5, 7, 10, 0))
        lateral.putalpha(mascara_lateral)
        imagem = Image.alpha_composite(imagem, lateral)

        # Vinheta superior/inferior para acabamento cinematográfico.
        vinheta = Image.new("L", (1, altura))
        pixels_v = []
        for py in range(altura):
            pos = py / max(1, altura - 1)
            topo = max(0.0, 1.0 - pos / 0.17)
            base = max(0.0, (pos - 0.72) / 0.28)
            alpha = int(min(150, topo * 72 + base * 150))
            pixels_v.append(alpha)

        vinheta.putdata(pixels_v)
        vinheta = vinheta.resize((largura, altura))
        camada_v = Image.new("RGBA", imagem.size, (3, 4, 6, 0))
        camada_v.putalpha(vinheta)
        imagem = Image.alpha_composite(imagem, camada_v)

        return imagem.convert("RGB")

    def aplicar_background(self, imagem):
        self.background_photo = ImageTk.PhotoImage(imagem)

        if self.background_item is None:
            self.background_item = self.canvas.create_image(
                0,
                0,
                image=self.background_photo,
                anchor="nw",
                tags="background",
            )
            self.canvas.tag_lower("background")
        else:
            self.canvas.itemconfigure(
                self.background_item,
                image=self.background_photo,
            )
            self.canvas.coords(self.background_item, 0, 0)

    def animar_troca_background(self, imagem_nova):
        self.animacao_id += 1
        animacao_atual = self.animacao_id

        if (
            self.imagem_pil_atual is None
            or self.imagem_pil_atual.size != imagem_nova.size
        ):
            self.aplicar_background(imagem_nova)
            self.imagem_pil_atual = imagem_nova
            return

        anterior = self.imagem_pil_atual.copy()
        frames = 9
        intervalo = 24

        def mostrar(indice):
            if animacao_atual != self.animacao_id:
                return

            fator = indice / frames
            frame = Image.blend(anterior, imagem_nova, fator)
            self.aplicar_background(frame)

            if indice < frames:
                self.after(intervalo, lambda: mostrar(indice + 1))
            else:
                self.imagem_pil_atual = imagem_nova

        mostrar(1)

    @staticmethod
    def tamanho_logo(imagem, largura_maxima, altura_maxima):
        largura, altura = imagem.size
        escala = min(largura_maxima / largura, altura_maxima / altura)
        return (
            max(1, int(largura * escala)),
            max(1, int(altura * escala)),
        )

    def criar_logo_photo(self, largura_canvas):
        largura_max = max(175, min(240, int(largura_canvas * 0.22)))
        tamanho = self.tamanho_logo(
            self.logo_original,
            largura_max,
            74,
        )

        logo = self.logo_original.resize(
            tamanho,
            Image.Resampling.LANCZOS,
        )
        self.logo_photo = ImageTk.PhotoImage(logo)

    def desenhar_conteudo(self, deslocamento_x=0):
        self.canvas.delete("content")
        self.canvas.delete("info")

        if not self.personagem_atual:
            return

        largura, altura = self.tamanho_canvas()
        escala = max(0.86, min(1.02, altura / 760))

        esquerda = max(46, int(largura * 0.052)) + deslocamento_x
        topo = max(24, int(altura * 0.032))
        largura_texto = min(455, int(largura * 0.47))

        cor_principal = self.personagem_atual["tema"]["principal"]
        cor_secundaria = self.personagem_atual["tema"]["secundaria"]

        self.criar_logo_photo(largura)
        self.canvas.create_image(
            esquerda,
            topo,
            image=self.logo_photo,
            anchor="nw",
            tags="content",
        )

        # Índice editorial do personagem.
        numero = self.indice_atual + 1
        self.canvas.create_text(
            esquerda,
            topo + 88,
            text=f"CHARACTER FILE   {numero:02d} / {self.total_personagens:02d}",
            anchor="nw",
            fill="#777D86",
            font=("Arial", max(7, int(8 * escala)), "bold"),
            tags="content",
        )
        self.canvas.create_rectangle(
            esquerda,
            topo + 108,
            esquerda + 34,
            topo + 110,
            fill=cor_secundaria,
            outline="",
            tags="content",
        )

        tamanho_nome = max(31, min(45, int(42 * escala)))
        nome_y = topo + 124

        # Sombra mínima para manter legibilidade sobre artes mais claras.
        self.canvas.create_text(
            esquerda + 2,
            nome_y + 2,
            text=self.personagem_atual["nome"].upper(),
            anchor="nw",
            fill="#050608",
            font=("Arial", tamanho_nome, "bold"),
            width=largura_texto,
            justify="left",
            tags="content",
        )
        nome_item = self.canvas.create_text(
            esquerda,
            nome_y,
            text=self.personagem_atual["nome"].upper(),
            anchor="nw",
            fill=cor_principal,
            font=("Arial", tamanho_nome, "bold"),
            width=largura_texto,
            justify="left",
            tags="content",
        )

        bbox_nome = self.canvas.bbox(nome_item)
        fim_nome = bbox_nome[3] if bbox_nome else nome_y + tamanho_nome

        self.canvas.create_text(
            esquerda,
            fim_nome + 5,
            text=f'“{self.personagem_atual["epiteto"]}”',
            anchor="nw",
            fill="#D5D8DD",
            font=("Arial", max(10, int(11 * escala)), "italic"),
            tags="content",
        )

        cargo_y = fim_nome + 34
        cargo = self.personagem_atual["cargo"].upper()
        cargo_item = self.canvas.create_text(
            esquerda + 14,
            cargo_y + 6,
            text=cargo,
            anchor="nw",
            fill="#F7F7F8",
            font=("Arial", max(7, int(8 * escala)), "bold"),
            tags="content",
        )
        bbox_cargo = self.canvas.bbox(cargo_item)
        cargo_largura = (bbox_cargo[2] - bbox_cargo[0]) + 28
        self.canvas.create_rectangle(
            esquerda,
            cargo_y,
            esquerda + cargo_largura,
            cargo_y + 27,
            fill="#11151B",
            outline=cor_principal,
            width=1,
            tags="content",
        )
        self.canvas.tag_raise(cargo_item)

        info_y = cargo_y + 52
        self.info_panel.desenhar(
            esquerda,
            info_y,
            largura_texto,
            altura - info_y - 30,
        )

        # Marca discreta no canto inferior direito.
        self.canvas.create_text(
            largura - 28,
            altura - 25,
            text="ONE PIECE EXPLORER",
            anchor="se",
            fill="#666B73",
            font=("Arial", 8, "bold"),
            tags="content",
        )

        # Linha de leitura vertical, dá acabamento editorial.
        self.canvas.create_rectangle(
            esquerda - 18,
            nome_y + 4,
            esquerda - 15,
            max(nome_y + 42, fim_nome - 2),
            fill=cor_principal,
            outline="",
            tags="content",
        )

    def redesenhar_conteudo(self):
        self.desenhar_conteudo(0)

    def animar_entrada_conteudo(self):
        if self.entrada_job is not None:
            try:
                self.after_cancel(self.entrada_job)
            except tk.TclError:
                pass

        passos = [18, 13, 9, 5, 2, 0]

        def mostrar(indice):
            self.desenhar_conteudo(passos[indice])
            if indice < len(passos) - 1:
                self.entrada_job = self.after(
                    24,
                    lambda: mostrar(indice + 1),
                )
            else:
                self.entrada_job = None

        mostrar(0)

    def ao_redimensionar(self, evento=None):
        if not self.personagem_atual:
            return

        if self.resize_job is not None:
            try:
                self.after_cancel(self.resize_job)
            except tk.TclError:
                pass

        self.resize_job = self.after(120, self.atualizar_layout)

    def atualizar_layout(self):
        self.resize_job = None

        if not self.personagem_atual or self.imagem_original is None:
            return

        self.animacao_id += 1
        imagem = self.preparar_background(self.tamanho_canvas())
        self.aplicar_background(imagem)
        self.imagem_pil_atual = imagem
        self.redesenhar_conteudo()

    def atualizar(self, personagem, indice=0, animar=True):
        self.personagem_atual = personagem
        self.indice_atual = indice

        self.imagem_original = Image.open(
            caminho_projeto(personagem["imagem"])
        ).convert("RGB")

        self.logo_original = Image.open(
            caminho_projeto(personagem["logo"])
        ).convert("RGBA")

        self.info_panel.atualizar_personagem(personagem)

        imagem_nova = self.preparar_background(self.tamanho_canvas())

        if animar:
            self.animar_troca_background(imagem_nova)
            self.animar_entrada_conteudo()
        else:
            self.animacao_id += 1
            self.aplicar_background(imagem_nova)
            self.imagem_pil_atual = imagem_nova
            self.redesenhar_conteudo()
