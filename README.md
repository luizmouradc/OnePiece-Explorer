# ☠️ One Piece Explorer V2

O **One Piece Explorer V2** é uma reconstrução do meu primeiro projeto
desenvolvido em Python. A ideia original foi mantida: explorar personagens
dos Piratas do Chapéu de Palha por meio de uma aplicação desktop.

A V2 refaz o projeto com uma interface mais moderna, código modular,
dados externos em JSON e componentes reutilizáveis.

## Sobre a evolução

A versão original foi criada com **Tkinter + Pillow** e concentrava boa
parte da interface em um único arquivo, com posições fixas e botões
criados manualmente.

Na V2, o projeto passou a utilizar:

- **CustomTkinter** para a interface;
- dados dos personagens em **JSON**;
- componentes separados para sidebar, personagem e informações;
- geração dinâmica dos personagens;
- temas de cores individuais;
- tratamento centralizado dos caminhos dos arquivos;
- transições e redimensionamento das imagens.

A versão original continua preservada na pasta `original/`.

## Funcionalidades

- seleção entre Luffy, Zoro, Nami, Sanji e Chopper;
- sidebar com os Jolly Rogers dos personagens;
- hero cinematográfico com a arte do personagem ocupando toda a área principal;
- overlay em gradiente integrado à imagem para manter os textos legíveis sem criar um painel separado;
- imagem, logo e identidade visual próprios para cada personagem;
- abas de **Visão geral**, **Habilidades**, **Objetivo** e **Ficha**;
- ficha com recompensa, origem, aniversário, Akuma no Mi e Haki;
- botão **Surpreenda-me** para escolher outro personagem aleatoriamente;
- transição suave em fade entre os heroes dos personagens;
- enquadramento individual de cada arte por meio de parâmetros de foco no JSON;
- abas editoriais sobrepostas à composição principal;
- redimensionamento da arte principal de acordo com a janela;
- atalhos de teclado para navegação.

## Atalhos

| Atalho | Ação |
| --- | --- |
| `1` a `5` | Selecionar personagem |
| `←` / `→` | Navegar entre os personagens |
| `R` | Escolher um personagem aleatório |

## Tecnologias

- Python
- CustomTkinter
- Pillow
- JSON

## Estrutura

```text
OnePiece-Explorer-V2/
├── main.py
├── requirements.txt
├── data/
│   └── personagens.json
├── ui/
│   ├── app.py
│   ├── sidebar.py
│   ├── personagem_view.py
│   └── info_panel.py
├── utils/
│   └── caminhos.py
├── assets/
│   ├── personagens/
│   ├── logos/
│   └── icones/
└── original/
    ├── main.py
    └── dados.py
```

## Como executar

Clone o repositório e entre na pasta do projeto.

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute:

```bash
python main.py
```

## Como adicionar um novo personagem

A interface é gerada a partir de `data/personagens.json`.

Para adicionar outro personagem:

1. adicione sua imagem em `assets/personagens/`;
2. adicione o logo em `assets/logos/`;
3. adicione o ícone em `assets/icones/`;
4. cadastre os dados no `personagens.json`.

Não é necessário criar manualmente um novo botão na interface.

## Versão

**V2.0**

Esta versão representa a reconstrução completa do projeto original, com uma interface cinematográfica pensada para valorizar as artes dos personagens.

## Observação

Projeto desenvolvido para fins educacionais e de portfólio.
One Piece e seus personagens pertencem aos respectivos detentores de direitos.
