class InfoPanel:
    """Informações editoriais desenhadas diretamente sobre o Canvas do hero."""

    ABAS = [
        ("visao", "VISÃO GERAL"),
        ("habilidades", "HABILIDADES"),
        ("objetivo", "OBJETIVO"),
        ("ficha", "FICHA"),
    ]

    def __init__(self, canvas, ao_mudar=None):
        self.canvas = canvas
        self.ao_mudar = ao_mudar

        self.personagem = None
        self.aba_atual = "visao"
        self.cor_principal = "#D62828"
        self.cor_secundaria = "#F4C542"

    def atualizar_personagem(self, personagem):
        self.personagem = personagem
        self.cor_principal = personagem["tema"]["principal"]
        self.cor_secundaria = personagem["tema"]["secundaria"]

    def mudar_aba(self, aba):
        if aba == self.aba_atual:
            return

        self.aba_atual = aba
        if self.ao_mudar:
            self.ao_mudar()

    def desenhar(self, x, y, largura, altura):
        self.canvas.delete("info")

        if not self.personagem:
            return

        y_conteudo = self._desenhar_abas(x, y, largura)

        if self.aba_atual == "ficha":
            self._desenhar_ficha(
                x,
                y_conteudo + 20,
                largura,
                altura - (y_conteudo - y) - 20,
            )
        else:
            self._desenhar_texto(
                x,
                y_conteudo + 22,
                largura,
            )

    def _desenhar_abas(self, x, y, largura):
        espacamento = 22
        pos_x = x

        for chave, texto in self.ABAS:
            ativa = chave == self.aba_atual
            cor = self.cor_principal if ativa else "#9096A0"
            fonte = ("Arial", 9, "bold")

            item = self.canvas.create_text(
                pos_x,
                y,
                text=texto,
                anchor="nw",
                fill=cor,
                font=fonte,
                tags=("info", f"aba_{chave}"),
            )

            caixa = self.canvas.bbox(item)
            largura_texto = caixa[2] - caixa[0]

            if ativa:
                self.canvas.create_rectangle(
                    pos_x,
                    y + 20,
                    pos_x + largura_texto,
                    y + 22,
                    fill=self.cor_principal,
                    outline="",
                    tags="info",
                )

            self.canvas.tag_bind(
                f"aba_{chave}",
                "<Button-1>",
                lambda evento, aba=chave: self.mudar_aba(aba),
            )
            self.canvas.tag_bind(
                f"aba_{chave}",
                "<Enter>",
                lambda evento: self.canvas.configure(cursor="hand2"),
            )
            self.canvas.tag_bind(
                f"aba_{chave}",
                "<Leave>",
                lambda evento: self.canvas.configure(cursor=""),
            )

            pos_x += largura_texto + espacamento

        self.canvas.create_line(
            x,
            y + 30,
            x + min(largura, 445),
            y + 30,
            fill="#30343B",
            width=1,
            tags="info",
        )

        return y + 30

    def _desenhar_texto(self, x, y, largura):
        dados = {
            "visao": (
                "SOBRE O PERSONAGEM",
                self.personagem["descricao"],
            ),
            "habilidades": (
                "ESTILO DE COMBATE",
                self.personagem["habilidades"],
            ),
            "objetivo": (
                "SONHO / OBJETIVO",
                self.personagem["objetivo"],
            ),
        }

        titulo, texto = dados[self.aba_atual]

        self.canvas.create_text(
            x,
            y,
            text=titulo,
            anchor="nw",
            fill="#747A84",
            font=("Arial", 8, "bold"),
            tags="info",
        )

        self.canvas.create_text(
            x,
            y + 23,
            text=texto,
            anchor="nw",
            fill="#ECEEF1",
            font=("Arial", 13),
            width=min(largura, 450),
            justify="left",
            tags="info",
        )

    def _desenhar_ficha(self, x, y, largura, altura):
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

        itens = [
            ("RECOMPENSA", recompensa),
            ("ORIGEM", origem),
            ("ANIVERSÁRIO", aniversario),
            ("AKUMA NO MI", fruta),
        ]

        largura_total = min(largura, 450)
        gap = 24
        largura_coluna = (largura_total - gap) / 2
        altura_linha = 73

        for indice, (titulo, valor) in enumerate(itens):
            linha = indice // 2
            coluna = indice % 2
            px = x + coluna * (largura_coluna + gap)
            py = y + linha * altura_linha

            self._desenhar_campo(
                px,
                py,
                largura_coluna,
                titulo,
                valor,
            )

        y_haki = y + (2 * altura_linha)
        self._desenhar_campo(
            x,
            y_haki,
            largura_total,
            "HAKI",
            haki,
        )

    def _desenhar_campo(self, x, y, largura, titulo, valor):
        self.canvas.create_text(
            x,
            y,
            text=titulo,
            anchor="nw",
            fill="#747A84",
            font=("Arial", 8, "bold"),
            tags="info",
        )

        self.canvas.create_text(
            x,
            y + 17,
            text=valor,
            anchor="nw",
            fill="#F4F5F7",
            font=("Arial", 11, "bold"),
            width=largura,
            justify="left",
            tags="info",
        )

        self.canvas.create_line(
            x,
            y + 56,
            x + largura,
            y + 56,
            fill="#30343B",
            width=1,
            tags="info",
        )
