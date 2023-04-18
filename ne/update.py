from conectar import conexao
from prettytable import PrettyTable

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()


def up_usuario():
    try:
        sql = 'SELECT * from usuarios'
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

        for linha in linhas:
            tabela.add_row(linha)
        print(tabela)

        id = input('Entre com o ID do usuário: ')

        sql = f"""SELECT * FROM usuarios WHERE idUsuario = '{id}';"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

        for linha in linhas:
            tabela.add_row(linha)
        print(tabela)

        usuario = input("Nome: ")
        email = input("Email: ")
        plano = input("Plano: ")
        tipo = input("Tipo: ")
        idade = input("Idade: ")

        sql = f"""UPDATE usuarios SET usuario='{usuario}', email = '{email}', plano = '{plano}', 
        tipo = '{tipo}', idade = '{idade}' WHERE idUsuario = '{id}';"""
        cursor.execute(sql)
        conexao.commit()
    except:
        print("Erro ao inserir os dados...")

def up_filme():
    try:
        sql = 'SELECT * from filmes'
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

        for linha in linhas:
            tabela.add_row(linha)
        print(tabela)

        id = input('Entre com o ID do filme: ')

        sql = f"""SELECT * FROM filmes WHERE idFilme = '{id}';"""
        cursor.execute(sql)
        linhas = cursor.fetchall()
        tabela = PrettyTable()
        tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

        for linha in linhas:
            tabela.add_row(linha)
        print(tabela)

        filme = input("Filme: ")
        plano = input("Plano: ")
        descricao = input("Descrição: ")
        classs = input("Classificação: ")

        sql = f"""UPDATE filmes SET filme='{filme}', plano = '{plano}', descricao = '{descricao}', 
        class = '{classs}' WHERE idFilme = '{id}';"""
        cursor.execute(sql)
        conexao.commit()
    except:
        print("Erro ao inserir os dados do filme...")