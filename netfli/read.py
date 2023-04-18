from conectar import conexao
from prettytable import PrettyTable

cursor = conexao.cursor()
cursor.execute('select database();')
linha = cursor.fetchone()
print(f'Banco => {linha[0]}')


def listar_usuarios():
    sql = 'SELECT * from usuarios'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    return linhas

def listar_filmes():
    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    # tabela = PrettyTable()
    # tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]
    #
    # for linha in linhas:
    #     tabela.add_row(linha)
    # print(tabela)
    return linhas

def procurar_usuario(id):
    sql = f"SELECT * from usuarios WHERE idUsuario = '{id}'"
    cursor.execute(sql)
    return cursor.fetchall()