<div align="center">

# One Piece Explorer

Uma aplicação desktop para explorar os personagens dos Piratas do Chapéu de Palha, reconstruída a partir do meu primeiro projeto desenvolvido em Python.

<br>

</div>

---

## Sobre o projeto

O **One Piece Explorer** é uma reconstrução do meu primeiro projeto desenvolvido em Python.

A ideia original foi mantida: criar uma aplicação desktop para explorar personagens dos Piratas do Chapéu de Palha, apresentando informações, habilidades, objetivos e características de cada personagem.

A primeira versão foi desenvolvida utilizando **Tkinter + Pillow**, com grande parte da interface concentrada em poucos arquivos, posições fixas e elementos criados manualmente.

Nesta nova versão, o projeto foi reorganizado utilizando **CustomTkinter**, separação de componentes, dados armazenados em JSON e geração dinâmica da interface.

A versão original continua preservada na pasta `original/`, permitindo acompanhar a evolução do projeto.

---

## Funcionalidades

- Seleção entre Luffy, Zoro, Nami, Sanji e Chopper
- Sidebar com os Jolly Rogers dos personagens
- Arte principal ocupando toda a área de destaque
- Identidade visual personalizada para cada personagem
- Imagem, logo e cores individuais
- Abas de Visão geral, Habilidades, Objetivo e Ficha
- Informações sobre recompensa, origem, aniversário, Akuma no Mi e Haki
- Botão Surpreenda-me para escolher um personagem aleatoriamente
- Navegação entre personagens por teclado
- Transição suave entre os personagens
- Redimensionamento automático das imagens de acordo com a janela
- Enquadramento personalizado das artes utilizando parâmetros definidos no JSON
- Geração dinâmica dos personagens a partir dos dados cadastrados
- Organização dos dados dos personagens em arquivo JSON
- Tratamento centralizado dos caminhos dos arquivos
- Separação da interface em diferentes componentes

---

## Atalhos

| Atalho | Ação |
| --- | --- |
| `1` a `5` | Selecionar personagem |
| `←` / `→` | Navegar entre os personagens |
| `R` | Escolher um personagem aleatório |

---

## Tecnologias utilizadas

<div align="center">

<img src="https://skillicons.dev/icons?i=python,git,github,vscode&theme=dark"/>

</div>

<br>

Outras ferramentas e recursos utilizados no projeto:

- **CustomTkinter** para construção da interface
- **Pillow** para manipulação e redimensionamento das imagens
- **JSON** para armazenamento dos dados dos personagens
- **Tkinter** utilizado na versão original do projeto

---

## Estrutura do projeto

```text
OnePiece-Explorer-V2/
├── assets/
│   ├── personagens/
│   ├── logos/
│   └── icones/
│
├── data/
│   └── personagens.json
│
├── original/
│   ├── main.py
│   └── dados.py
│
├── ui/
│   ├── app.py
│   ├── sidebar.py
│   ├── personagem_view.py
│   └── info_panel.py
│
├── utils/
│   └── caminhos.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Demonstração

<div align="center">
<br>

### Luffy
<div align="center">

<img width="1366" height="728" alt="One Piece Explorer - Luffy" src="https://github.com/user-attachments/assets/d8d9203e-a58f-4a1d-80b0-0f50b44656b4" />

</div>
<br>

### Zoro
<div align="center">

<img width="1366" height="728" alt="One Piece Explorer - Zoro" src="https://github.com/user-attachments/assets/0753f335-744d-42fb-803b-a6f3dfd1b3ec" />

</div>
<br>

### Nami
<div align="center">

<img width="1366" height="728" alt="One Piece Explorer - Nami" src="https://github.com/user-attachments/assets/fa967d9e-0e6c-40fc-93e4-22684bf99671" />

</div>
<br>

### Sanji
<div align="center">

<img width="1366" height="728" alt="One Piece Explorer - Sanji" src="https://github.com/user-attachments/assets/c205d8a3-9594-4991-8330-f3e7dcbc0bb5" />

</div>
<br>

### Chopper
<div align="center">

<img width="1366" height="728" alt="One Piece Explorer - Chopper" src="https://github.com/user-attachments/assets/7c21fb50-9e8d-441b-bd05-f7d99a561acf" />

</div>
</div>

---

## Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd OnePiece-Explorer-V2
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Execute a aplicação:

```bash
python main.py
```

---

## Como adicionar um novo personagem

A interface é gerada a partir das informações presentes no arquivo `data/personagens.json`.

Para adicionar um novo personagem:

1. Adicione a imagem do personagem em `assets/personagens/`
2. Adicione o logo em `assets/logos/`
3. Adicione o ícone em `assets/icones/`
4. Cadastre as informações do personagem no arquivo `personagens.json`

Os elementos da interface são gerados dinamicamente, portanto não é necessário criar manualmente um novo botão para o personagem.

---

## Versão original

A primeira versão do **One Piece Explorer** foi desenvolvida utilizando **Tkinter + Pillow** e está preservada na pasta `original/`.

A versão atual representa uma reconstrução do projeto, com melhorias na organização do código, estrutura da interface, gerenciamento dos dados, responsividade dos elementos e experiência visual.

---

## Observação

Este projeto foi desenvolvido para fins educacionais e de portfólio.

**One Piece** e seus personagens pertencem aos seus respectivos detentores de direitos.

---

<div align="center">

Feito por <a href="https://github.com/luizmouradc">Luiz Inácio</a>

</div>
