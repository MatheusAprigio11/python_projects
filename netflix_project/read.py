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
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]

    for linha in linhas:
        tabela.add_row(linha)
    print(tabela)

def listar_filmes():
    sql = 'SELECT * from filmes'
    cursor.execute(sql)
    linhas = cursor.fetchall()
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Filme", "Plano", "Descrição", "Classificação"]

    for linha in linhas:
        tabela.add_row(linha)
    print(tabela)


def procurar_usuario(user, email):
    sql = f"SELECT * from usuarios WHERE usuario = '{user}' AND email ='{email}'"
    cursor.execute(sql)
    linhas = cursor.fetchall()
    tabela = PrettyTable()
    tabela.field_names = ["ID", "Usuário", "Email", "Plano", "Tipo", "Idade"]
    if len(linhas) != 0:
        print('Usuário cadastrado...')
        for linha in linhas:
            tabela.add_row(linha)
        return linhas[0][4]
    else:
        print("Usuário não encontrado...")