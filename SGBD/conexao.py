import sqlite3

# colocar na pasta
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

# criar um conector
cur = conexao.cursor()


def criar_tabela(cur, conexao):
    cur.execute(
        "CREATE TABLE cliente(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(55), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registo(conexao, cur, nome, email):
    novo = ("Lu", "lu@gmail.com")
    cur.execute("INSERT INTO cliente(nome, email) VALUES (?,?);", novo)
    conexao.commit()


def atualizar_registro(conexao, cur, nome, email, id):
    novo = (nome, email, id)
    cur.execute("UPDATE cliente SET nome=?, email=? WHERE id=?;", novo)
    conexao.commit()


def deletar_registro(conexao, cur, id):
    data = (id,)
    cur.execute("DELETE FROM cliente WHERE id=?;", data)
    conexao.commit()


# atualizar_registro(conexao, cur, 'Claudio Gabriel','Cg@gmail.com', 1 )

deletar_registro(conexao, cur, 2)
