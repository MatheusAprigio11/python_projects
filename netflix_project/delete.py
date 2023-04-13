from conectar import conexao
from prettytable import PrettyTable

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()


def dt_usuario():
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

        resp = input(f'Deseja realmente apagar? [S/N]').strip().upper()
        if resp == 'S':
            sql = f"""DELETE FROM usuarios WHERE idUsuario = '{id}';"""
            cursor.execute(sql)
            conexao.commit()
    except:
        print("Erro ao apagar os dados...")

def dt_filme():
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

        resp = input(f'Deseja realmente apagar? [S/N]').strip().upper()
        if resp == 'S':
            sql = f"""DELETE FROM filmes WHERE idFilme = '{id}';"""
            cursor.execute(sql)
            conexao.commit()
    except:
        print("Erro ao apagar os dados...")