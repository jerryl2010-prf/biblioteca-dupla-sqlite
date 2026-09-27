import sqlite3

def listar_usuarios():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM usuarios")
    resultados = cursor.fetchall()

    print("\n--- Usuários ---")

    for linha in resultados:
        print(f"ID: {linha['id']} | Nome: {linha['nome']}")

    conn.close()

def listar_autores():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM autores")
    resultados = cursor.fetchall()

    print("\n--- Autores ---")

    for linha in resultados:
        print(f"ID: {linha['id']} | Nome: {linha['nome']}")

    conn.close()

def listar_editoras():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM editoras")
    resultados = cursor.fetchall()

    print("\n--- Editoras ---")

    for linha in resultados:
        print(f"ID: {linha['id']} | Nome: {linha['nome']}")

    conn.close()


def listar_livros():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM livros")
    resultados = cursor.fetchall()

    print("\n--- Livros ---")

    for linha in resultados:
        if linha["disponivel"]:
            disponibilidade = "Disponível"
        else:
            disponibilidade = "Indisponível"

        print (
            f"ID: {linha['id']} | "
            f"Título: {linha['titulo']} | "
            f"Autor: {linha['autor_id']} | "
            f"Editora: {linha['editora_id']} | "
            f"Ano: {linha['ano_publicacao']} | "
            f"Edição: {linha['edicao']} | "
            f"{disponibilidade}"
        )

    conn.close()

def listar_emprestimos():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos")
    resultados = cursor.fetchall()

    print("\n--- Empréstimos ---")

    for linha in resultados:
        print (
            f"ID: {linha['id']} | "
            f"Usuário: {linha['usuario_id']} | "
            f"Data: {linha['data']}"
        )

    conn.close()


def listar_emprestimos_livros():
    conn = sqlite3.connect("biblioteca.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM emprestimos_livros")
    resultados = cursor.fetchall()

    print("\n--- Livros emprestados ---")

    for linha in resultados:
        print(
            f"Empréstimo: {linha['emprestimo_id']} | "
            f"Livro: {linha['livro_id']} | "
            f"Devolução: {linha['data_devolucao']}"
        )

    conn.close()