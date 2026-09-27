import sqlite3

def insert_editora (nome):
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    insert_sql = "INSERT INTO editoras (nome) VALUES (?)"

    cursor.execute(insert_sql, (nome,))

    conn.commit()
    conn.close()