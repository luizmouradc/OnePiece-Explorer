# One Piece Explorer V2

Reconstrução do primeiro projeto em Python/Tkinter, agora usando CustomTkinter,
organização modular e dados externos em JSON.

## Etapa atual — Abas e ficha

A Etapa 4 adiciona a navegação de informações de cada personagem:

- aba `Visão geral`;
- aba `Habilidades`;
- aba `Objetivo`;
- aba `Ficha`;
- cards com recompensa, origem, aniversário, Akuma no Mi e Haki;
- destaque das abas usando a cor temática do personagem;
- novo componente `ui/info_panel.py`.

A troca de personagem continua atualizando imagem, logo, cores e todos os dados
do painel automaticamente.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```

## Estrutura principal

```text
OnePiece-Explorer-V2/
├── main.py
├── data/
│   └── personagens.json
├── ui/
│   ├── app.py
│   ├── sidebar.py
│   ├── personagem_view.py
│   └── info_panel.py
├── utils/
│   └── caminhos.py
└── assets/
    ├── personagens/
    ├── logos/
    └── icones/
```
