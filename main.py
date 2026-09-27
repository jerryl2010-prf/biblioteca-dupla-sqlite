import sqlite3 as sqlite
from criar_tabelas import create_autores
from dados_autores import insert_autor

nome = "Luiz"

create_autores()

insert_autor (nome)
