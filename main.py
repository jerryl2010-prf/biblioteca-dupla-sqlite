import sqlite3 as sqlite
from criar_tabelas import create_autores, create_editoras, create_emprestimos, create_emprestimos_livros, create_livros, create_usuarios
from dados_autores import insert_autor
from dados_editoras import insert_editora
from dados_emprestimos import insert_emprestimo
from dados_usuarios import insert_usuario
from dados_livros import insert_livro
from dados_emprestimos_livro import insert_emprestimo_livro
from time import sleep

create_autores()
create_editoras()
create_livros()
create_usuarios()
create_emprestimos()
create_emprestimos_livros()
