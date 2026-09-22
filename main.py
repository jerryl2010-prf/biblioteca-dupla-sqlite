import sqlite3
from banco import conectar_banco
from dados_autores import del_autores, criar_autores, commit_autores, inserir_autores

autor = "Machadao"

del_autores()
criar_autores()
inserir_autores(autor)
commit_autores()