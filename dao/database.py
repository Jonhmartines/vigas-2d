import sqlite3
import os

# Caminho do banco dentro da pasta "data"
DB_PATH = os.path.join("data", "beam_data.db")


def get_connection():
    """Retorna conexão com o banco e cria a pasta 'data' caso não exista."""
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_PATH)


def init_db():
    """Cria as tabelas caso ainda não existam."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            position REAL,
            magnitude REAL,
            load_type TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            id INTEGER PRIMARY KEY,
            support_a REAL,
            support_b REAL
        )
    """)

    conn.commit()
    conn.close()


# ---------- FUNÇÕES PARA CARGAS APLICADAS ----------

def save_load(position, magnitude, load_type):
    """Salva uma carga aplicada na viga."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO loads (position, magnitude, load_type)
        VALUES (?, ?, ?)
    """, (position, magnitude, load_type))

    conn.commit()
    conn.close()


def load_all_loads():
    """Retorna todas as cargas salvas no banco."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT position, magnitude, load_type FROM loads")
    result = cursor.fetchall()

    conn.close()
    return result


def clear_loads():
    """Apaga TODAS as cargas salvas (útil ao resetar projeto)."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM loads")

    conn.commit()
    conn.close()


# ---------- FUNÇÕES PARA APOIOS ----------

def save_supports(a, b):
    """Salva valores dos apoios A e B."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM settings")  # mantém sempre apenas 1 linha

    cursor.execute("""
        INSERT INTO settings (id, support_a, support_b)
        VALUES (1, ?, ?)
    """, (a, b))

    conn.commit()
    conn.close()


def load_supports():
    """Carrega os apoios salvos. Caso não existam, retorna (0,0)."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT support_a, support_b FROM settings WHERE id = 1")
    row = cursor.fetchone()

    conn.close()

    return row if row else (0, 0)