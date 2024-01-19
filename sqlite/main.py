import sqlite3

# criar a conexao
conexao = sqlite3.connect('usuario.db') # definir o nome do banco de dados

# Cria um objeto cursor para executar comandos SQL no banco de dados.
cursor = conexao.cursor()

# Criação da tabela 'usuario' no banco de dados.
# A tabela terá três colunas: 'id' (chave primária), 'nome' (texto) e 'idade' (inteiro).
cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                nome TEXT NOT NULL,
                idade INT NOT NULL);''')

# inserir dados na tabela -------
cursor.execute('''INSERT INTO usuario (nome, idade) VALUES('leticia', 18)''')
cursor.execute('''INSERT INTO usuario (nome, idade) VALUES('luiz', 19)''')

with sqlite3.connect('usuario.db') as conexao:

    # Cria um objeto cursor para executar comandos SQL no banco de dados.
    #cursor = conexao.cursor()

    # Consulta todos os dados da tabela 'usuario'
    cursor.execute('''SELECT * FROM usuario''')
    print("Dados selecionados da tabela 'usuario':")
    
    # para ver os dados
    #resultado1 = cursor.fetchone() vai mostrar so a primeira linha
    resultado = cursor.fetchall() # para mostar todas a linhas

    for linha in resultado:
        print(linha)

# Fecha a conexão com o banco de dados
#conexao.close()
