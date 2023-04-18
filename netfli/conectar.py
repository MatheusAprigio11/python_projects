
import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='netflix',
    user='root',
    password=''
)

if conexao.is_connected():
    print(f'conectou a {conexao.get_server_info()}')