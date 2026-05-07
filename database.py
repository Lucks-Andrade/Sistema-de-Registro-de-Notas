import sqlite3

def conectar():
    return sqlite3.connect("alunos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        matricula TEXT PRIMARY KEY,
        nome TEXT NOT NULL,
        data_nascimento TEXT,
        nota REAL
    )
    """)

    conn.commit()
    conn.close()


def inserir_aluno(matricula, nome, data_nascimento, nota):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO alunos (matricula, nome, data_nascimento, nota)
        VALUES (?, ?, ?, ?)
        """, (matricula, nome, data_nascimento, nota))

        conn.commit()

    except sqlite3.IntegrityError:
        print("Matrícula já cadastrada!")

    conn.close()


def deletar_aluno(matricula):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM alunos WHERE matricula = ?
    """, (matricula,))

    conn.commit()
    conn.close()


def buscar_matricula(matricula):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM alunos WHERE matricula = ?
    """, (matricula,))

    aluno = cursor.fetchone()

    conn.close()
    return aluno


def buscar_nome(nome):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM alunos WHERE nome LIKE ?
    """, ('%' + nome + '%',))

    resultado = cursor.fetchall()

    conn.close()
    return resultado


def listar_alunos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")

    alunos = cursor.fetchall()

    conn.close()
    return alunos


def atualizar_aluno(matricula, nome, data_nascimento, nota):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE alunos
    SET nome = ?, data_nascimento = ?, nota = ?
    WHERE matricula = ?
    """, (nome, data_nascimento, nota, matricula))

    conn.commit()
    conn.close()


criar_tabela()