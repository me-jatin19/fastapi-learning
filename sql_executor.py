import sqlite3

def execute_query(query):

    conn = sqlite3.connect("company.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]