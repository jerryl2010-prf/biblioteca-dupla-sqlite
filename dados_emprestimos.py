import sqlite3

def insert_emprestimo (usuario_id, data):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    insert_sql = "INSERT INTO emprestimos (usuario_id, data) VALUES (?,?)"

    cursor.execute(insert_sql, (usuario_id, data))

    conn.commit()
    conn.close()