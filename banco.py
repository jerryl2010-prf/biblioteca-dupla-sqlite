import sqlite3

def conectar_banco():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()
    return cursor