# One Piece Explorer V2

Reconstrução do primeiro projeto em Python/Tkinter, agora usando CustomTkinter,
organização modular e dados externos em JSON.

## Etapa atual — Interface base

A Etapa 3 começa a identidade visual da V2:

- sidebar própria com as caveiras dos personagens;
- destaque do personagem selecionado usando sua cor temática;
- layout escuro e mais moderno;
- imagem principal em uma área de destaque;
- logo individual de cada personagem;
- nome, epíteto, cargo e visão geral;
- cores que mudam de acordo com o personagem;
- componentes separados em `sidebar.py` e `personagem_view.py`;
- `.gitignore` para evitar arquivos de cache no repositório.

As abas `Visão geral`, `Habilidades`, `Objetivo` e `Ficha`,
além do personagem aleatório, entram nas próximas etapas.

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
│   └── personagem_view.py
├── utils/
│   └── caminhos.py
└── assets/
    ├── personagens/
    ├── logos/
    └── icones/
```
