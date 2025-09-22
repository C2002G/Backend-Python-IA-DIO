import sqlite3

# colocar na pasta
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

# criar um conector
cur = conexao.cursor()

#row para printar como dicionario no dict
cur.row_factory = sqlite3.Row

try:
    cur.execute("INSERT INTO cliente (nome, email) VALUES (?,?)",  ("Teste 3" , "teste3@gmail.com"))
    cur.execute("INSERT INTO cliente (ID, nome, email) VALUES (?,?,?)",  ("2","Teste 4" , "teste4@gmail.com"))
    conexao.commit()
except Exception as exc:
    print("erro! {exc}")
    conexao.rollback()


# esse try serve para se um insert into ou delete for errado, ele n faz a implementações anteriores dentro do try

