# One Piece Explorer V2

Reconstrução do primeiro projeto em Python/Tkinter, agora usando CustomTkinter,
organização modular e dados externos em JSON.

## Etapa atual

A Etapa 2 cria o esqueleto funcional da aplicação:

- leitura automática de `data/personagens.json`;
- sidebar gerada a partir dos personagens cadastrados;
- troca dinâmica de personagem;
- exibição da imagem principal;
- atualização de nome, epíteto, cargo, descrição e cor temática;
- caminhos de arquivos centralizados em `utils/caminhos.py`.

O visual ainda é propositalmente simples. A estilização completa será feita
nas próximas etapas.

## Como executar

```bash
pip install -r requirements.txt
python main.py
```
