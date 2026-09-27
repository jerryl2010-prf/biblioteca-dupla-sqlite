import sqlite3 as sqlite
from criar_tabelas import create_autores, create_editoras, create_emprestimos, create_emprestimos_livros, create_livros, create_usuarios
from dados_autores import insert_autor
from dados_editoras import insert_editora
from dados_emprestimos import insert_emprestimo
from dados_usuarios import insert_usuario
from dados_livros import insert_livro
from dados_emprestimos_livro import insert_emprestimo_livro
from listar_dados import listar_autores, listar_editoras, listar_emprestimos, listar_emprestimos_livros, listar_livros, listar_usuarios
from time import sleep

create_autores()
create_editoras()
create_livros()
create_usuarios()
create_emprestimos()
create_emprestimos_livros()

while True:

    sleep(0.7)
    print("--- Biblioteca ---")
    sleep(0.7)
    print("""
1) Cadastrar usuário
2) Cadastrar autor
3) Cadastrar editora
4) Cadastrar livro
5) Cadastrar empréstimo
6) Cadastrar livro do empréstimo
7) Listar usuários
8) Listar autores
9) Listar editoras
10) Listar livros
11) Listar empréstimos
12) Listar livros dos empréstimos
13) Sair
""")

    opcao = int(input("Escolha uma opção: "))
    sleep(0.7)

    if opcao == 1:
        nome = input("Nome do usuário: ")
        insert_usuario(nome)
        print("Usuário cadastrado com sucesso!")

    elif opcao == 2:
        nome = input("Nome do autor: ")
        insert_autor(nome)
        print("Autor cadastrado com sucesso!")

    elif opcao == 3:
        nome = input("Nome da editora: ")
        insert_editora(nome)
        print("Editora cadastrada com sucesso!")

    elif opcao == 4:
        titulo = input("Título do livro: ")
        autor_id = int(input("ID do autor: "))
        editora_id = int(input("ID da editora: "))
        ano_publicacao = int(input("Ano de publicação: "))
        edicao = input("Edição (Se não tiver, deixe vazio): ")
        if edicao == "":
            edicao = None
        else:
            edicao = int(edicao)
        disponivel = int(input("Disponível? (1 - Sim | 0 - Não): "))

        insert_livro(titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel)
        print("Livro cadastrado com sucesso!")

    elif opcao == 5:
        usuario_id = int(input("ID do usuário: "))
        data = input("Data do empréstimo (Ano-Mês-Dia): ")
        insert_emprestimo(usuario_id, data)

        print("Empréstimo cadastrado com sucesso!")

    elif opcao == 6:

        emprestimo_id = int(input("ID do empréstimo: "))
        livro_id = int(input("ID do livro: "))
        data_devolucao = input("Data de devolução (Ano-Mês-Dia): ")

        insert_emprestimo_livro(emprestimo_id, livro_id, data_devolucao)
        print("Livro do empréstimo cadastrado com sucesso!")

    elif opcao == 7:
        listar_usuarios()

    elif opcao == 8:
        listar_autores()

    elif opcao == 9:
        listar_editoras()

    elif opcao == 10:
        listar_livros()

    elif opcao == 11:
        listar_emprestimos()

    elif opcao == 12:
        listar_emprestimos_livros()

    elif opcao == 13:
        print("Saindo...")
        sleep(0.8)
        break

    else:
        print("Opção inválida!")