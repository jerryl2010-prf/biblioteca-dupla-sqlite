import sqlite3
from banco import conectar_banco

def del_autores(cursor=conectar_banco()):
    cursor.execute("DROP TABLE IF EXISTS autores")

def criar_autores(cursor=conectar_banco()):
    cursor.execute("CREATE TABLE autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL)")

def inserir_autores (autor, cursor=conectar_banco()):
    cursor.executemany("INSERT INTO autores(nome) VALUES(?)", [(autor,)])

def commit_autores(cursor=conectar_banco()): 
    cursor.commit()