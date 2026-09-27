import sqlite3

def insert_emprestimo_livro (emprestimo_id, livro_id, data_devolucao):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    insert_sql = "INSERT INTO emprestimos_livros (emprestimo_id, livro_id, data_devolucao) VALUES (?, ?, ?)"

    cursor.execute(insert_sql, (emprestimo_id, livro_id, data_devolucao))

    conn.commit()
    conn.close()