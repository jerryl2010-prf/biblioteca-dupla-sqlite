import sqlite3

def insert_livro (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    insert_sql = "INSERT INTO livros (titulo, autor_id, editora_id, ano_publicacao, edicao,disponivel) VALUES (?, ?, ?, ?, ?, ?)"

    cursor.execute(insert_sql, (titulo, autor_id, editora_id, ano_publicacao, edicao, disponivel))

    conn.commit()
    conn.close()