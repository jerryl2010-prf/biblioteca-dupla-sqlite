import sqlite3

def insert_usuario (nome):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    insert_sql = "INSERT INTO usuarios (nome) VALUES (?)"

    cursor.execute(insert_sql, (nome,))

    conn.commit()
    conn.close()