# One Piece Explorer

## 1. Sobre o projeto
Aplicação desenvolvida para exibir informações dos personagens de One Piece, permitindo ao usuário alternar entre diferentes personagens e visualizar detalhes como nome, cargo,
habilidades e objetivo. Utiliza uma interface gráfica em Python com tkinter, e a biblioteca PIL para carregar imagens dos personagens e seus símbolos.

## 2. Funcionalidades da aplicação
As funcionalidades disponibilizadas ao usuário na aplicação de exibição de personagens de One Piece incluem:

* Exibição de informações detalhadas: Ao selecionar um personagem, o usuário visualiza seu nome, cargo, habilidades (ou Akuma no Mi, se aplicável), e objetivo.
  Cada detalhe é mostrado em uma interface intuitiva com texto claro e organizado.
* Alternância entre personagens: O usuário pode alternar entre diferentes personagens (como Luffy, Zoro, Nami, Sanji e Chopper) ao clicar nos respectivos botões,
  cada um identificado por uma pequena imagem do símbolo do personagem (uma caveira estilizada).
* Atualização de imagem e logo: Ao selecionar um personagem, a imagem e o logo do personagem são atualizados automaticamente,
  oferecendo uma experiência visual personalizada para cada um deles.
* Design responsivo e intuitivo: Embora seja uma aplicação de janela fixa, o layout dos elementos foi projetado para garantir
  clareza e fácil navegação. A interface inclui uma separação visual com barras e alinhamento adequado para exibir as informações de forma organizada.

Cada funcionalidade foi desenvolvida com critérios de completude e verificação, como:
* Garantir que as imagens carreguem corretamente e com qualidade adequada para cada personagem.
* Assegurar que o texto descritivo de cada personagem seja exibido de forma legível e sem cortes, aplicando wraplength para adequação ao espaço.

## 3.Uso
Para visualizar e utilizar essa aplicação de exibição de personagens de One Piece, siga as instruções abaixo:

**1. Instalação do Ambiente:**
* A aplicação requer o interpretador Python 3.x instalado no seu sistema, assim como as bibliotecas tkinter e PIL (do pacote Pillow).
  Caso necessário, instale a biblioteca Pillow usando:
  ```
  pip install pillow
  ```
**2. Estrutura dos Dados:**
* Crie um arquivo chamado dados.py para armazenar as informações dos personagens, como nomes, imagens, cargos, habilidades e objetivos.
  Esse arquivo deve seguir o formato dos exemplos usados no código para garantir compatibilidade.

**3. Organização das Imagens:**
* As imagens dos personagens e seus símbolos (caveiras) devem estar armazenadas em uma pasta chamada OnePiece Explorer/imagens. Cada imagem precisa ter o nome específico do personagem
  (por exemplo, caveira do luffy.jpg para o botão de Luffy) para ser associada corretamente durante a exibição.

**4. Execução da Aplicação:**
* Para iniciar a aplicação, execute o arquivo principal em que está implementado o código (por exemplo, python main.py).
* A interface será aberta em uma janela do sistema, onde você poderá clicar nos botões para alternar entre os personagens e visualizar suas informações.

## 4. Visualização
Aqui você pode visualizar como o projeto funciona.

![OnePiece explorer](https://github.com/user-attachments/assets/115e7dd4-00d8-4c80-8c6a-c8783e4fc6d3)


## 5. Ferramentas utilizadas
Para desenvolver essa aplicação de exibição de personagens de One Piece, foram utilizadas as seguintes ferramentas:
* Python
* Tkinter
* Pillow (PIL)
* Git
* GitHub
