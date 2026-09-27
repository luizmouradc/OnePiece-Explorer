import customtkinter as ctk


class InfoPanel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            fg_color="transparent",
            corner_radius=0
        )

        self.personagem = None
        self.aba_atual = "visao"
        self.cor_principal = "#D62828"

        self.botoes_abas = {}

        self.grid_columnconfigure(0, weight=1)

        self.criar_abas()
        self.criar_area_conteudo()

    def criar_abas(self):
        frame_abas = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        frame_abas.grid(
            row=0,
            column=0,
            sticky="ew",
            pady=(0, 18)
        )

        nomes = [
            ("visao", "Visão geral"),
            ("habilidades", "Habilidades"),
            ("objetivo", "Objetivo"),
            ("ficha", "Ficha")
        ]

        for indice, (chave, texto) in enumerate(nomes):
            botao = ctk.CTkButton(
                frame_abas,
                text=texto,
                height=34,
                corner_radius=9,
                font=ctk.CTkFont(size=12, weight="bold"),
                fg_color="transparent",
                hover_color="#222833",
                border_width=1,
                border_color="#2A313D",
                text_color="#B7BDC7",
                command=lambda aba=chave: self.mudar_aba(aba)
            )
            botao.grid(
                row=0,
                column=indice,
                padx=(0 if indice == 0 else 5, 5),
                sticky="ew"
            )
            frame_abas.grid_columnconfigure(indice, weight=1)

            self.botoes_abas[chave] = botao

    def criar_area_conteudo(self):
        self.area_conteudo = ctk.CTkFrame(
            self,
            fg_color="#10131A",
            corner_radius=14,
            border_width=1,
            border_color="#232A35"
        )
        self.area_conteudo.grid(
            row=1,
            column=0,
            sticky="nsew"
        )

        self.grid_rowconfigure(1, weight=1)

        self.label_titulo = ctk.CTkLabel(
            self.area_conteudo,
            text="",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#747D8A",
            anchor="w"
        )
        self.label_titulo.pack(
            fill="x",
            padx=20,
            pady=(18, 7)
        )

        self.label_texto = ctk.CTkLabel(
            self.area_conteudo,
            text="",
            font=ctk.CTkFont(size=14),
            text_color="#D7DBE2",
            justify="left",
            anchor="nw",
            wraplength=350
        )
        self.label_texto.pack(
            fill="x",
            padx=20,
            pady=(0, 18)
        )

        self.frame_ficha = ctk.CTkFrame(
            self.area_conteudo,
            fg_color="transparent"
        )

    def atualizar_personagem(self, personagem):
        self.personagem = personagem
        self.cor_principal = personagem["tema"]["principal"]

        self.mudar_aba(self.aba_atual)

    def mudar_aba(self, aba):
        self.aba_atual = aba
        self.atualizar_estado_abas()

        if not self.personagem:
            return

        if aba == "ficha":
            self.mostrar_ficha()
            return

        self.frame_ficha.pack_forget()
        self.label_titulo.pack(
            fill="x",
            padx=20,
            pady=(18, 7)
        )
        self.label_texto.pack(
            fill="x",
            padx=20,
            pady=(0, 18)
        )

        if aba == "visao":
            titulo = "VISÃO GERAL"
            texto = self.personagem["descricao"]

        elif aba == "habilidades":
            titulo = "HABILIDADES"
            texto = self.personagem["habilidades"]

        else:
            titulo = "OBJETIVO"
            texto = self.personagem["objetivo"]

        self.label_titulo.configure(text=titulo)
        self.label_texto.configure(text=texto)

    def atualizar_estado_abas(self):
        for chave, botao in self.botoes_abas.items():
            if chave == self.aba_atual:
                botao.configure(
                    fg_color=self.cor_principal,
                    border_color=self.cor_principal,
                    text_color="#FFFFFF"
                )
            else:
                botao.configure(
                    fg_color="transparent",
                    border_color="#2A313D",
                    text_color="#B7BDC7"
                )

    def limpar_ficha(self):
        for widget in self.frame_ficha.winfo_children():
            widget.destroy()

    def criar_card(self, master, titulo, valor, linha, coluna):
        card = ctk.CTkFrame(
            master,
            fg_color="#171B23",
            corner_radius=12,
            border_width=1,
            border_color="#272E39"
        )
        card.grid(
            row=linha,
            column=coluna,
            sticky="nsew",
            padx=5,
            pady=5
        )

        master.grid_columnconfigure(coluna, weight=1)

        label_titulo = ctk.CTkLabel(
            card,
            text=titulo.upper(),
            font=ctk.CTkFont(size=10, weight="bold"),
            text_color="#777F8C",
            anchor="w"
        )
        label_titulo.pack(
            fill="x",
            padx=14,
            pady=(12, 4)
        )

        label_valor = ctk.CTkLabel(
            card,
            text=valor,
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color="#F1F3F5",
            anchor="w",
            justify="left",
            wraplength=155
        )
        label_valor.pack(
            fill="x",
            padx=14,
            pady=(0, 12)
        )

    def mostrar_ficha(self):
        self.label_titulo.pack_forget()
        self.label_texto.pack_forget()

        self.limpar_ficha()

        self.frame_ficha.pack(
            fill="both",
            expand=True,
            padx=14,
            pady=14
        )

        recompensa = self.personagem["recompensa"]["exibicao"]
        origem = self.personagem["origem"]
        aniversario = self.personagem["aniversario"]

        akuma = self.personagem["akuma_no_mi"]
        if akuma:
            fruta = f'{akuma["nome"]}\n{akuma["tipo"]}'
        else:
            fruta = "Nenhuma"

        tipos_haki = self.personagem["haki"]["tipos"]
        haki = ", ".join(tipos_haki) if tipos_haki else "Não confirmado"

        self.criar_card(
            self.frame_ficha,
            "Recompensa",
            recompensa,
            0,
            0
        )
        self.criar_card(
            self.frame_ficha,
            "Origem",
            origem,
            0,
            1
        )
        self.criar_card(
            self.frame_ficha,
            "Aniversário",
            aniversario,
            1,
            0
        )
        self.criar_card(
            self.frame_ficha,
            "Akuma no Mi",
            fruta,
            1,
            1
        )
        self.criar_card(
            self.frame_ficha,
            "Haki",
            haki,
            2,
            0
        )
