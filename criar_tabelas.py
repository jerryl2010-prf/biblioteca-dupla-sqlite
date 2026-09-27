import sqlite3

def create_usuarios():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def create_autores():  
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def create_editoras():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS editoras (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def create_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor_id INTEGER NOT NULL REFERENCES autores(id),
        editora_id INTEGER NOT NULL REFERENCES editoras(id),
        ano_publicacao INTEGER NOT NULL,
        edicao INTEGER,
        disponivel BOOLEAN NOT NULL DEFAULT 1 CHECK (disponivel IN(0,1))
    )
    """)

    conn.commit()
    conn.close()

def create_emprestimos():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER REFERENCES usuario(id),
        data DATE DEFAULT CURRENT DATE
    )
    """)

    conn.commit()
    conn.close()

def create_emprestimos_livros():
    conn = sqlite3.connect("biblioteca.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos_livros (
        emprestimo_id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER REFERENCES livro(id),
        data_devolucao DATE,
        PRIMARY KEY (emprestimo_id, livro_id)
    )
    """)

    conn.commit()
    conn.close()