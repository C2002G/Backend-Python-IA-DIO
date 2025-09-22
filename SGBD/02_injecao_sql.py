import sqlite3

# colocar na pasta
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")

# criar um conector
cur = conexao.cursor()

#row para printar como dicionario no dict
cur.row_factory = sqlite3.Row

id_cliente = input("informe o id: ")
cur.execute(f"SELECT * FROM cliente WHERE id=?", (id_cliente) )
cliente = cur.fetchone()
print(dict(cliente))