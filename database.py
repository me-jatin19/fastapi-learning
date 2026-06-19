import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    department TEXT
)
""")

cursor.execute("DELETE FROM employees")

employees = [
    (1, "Cat 1", 800, "Engineering"),
    (2, "Cat2 ", 500000, "HR"),
    (3, "Cat3", 900, "Engineering"),
    (4, "Cat4", 600000, "Marketing"),
    (5, "Velli Cat", 88, "Berozgar")
]

cursor.executemany(
    "INSERT INTO employees VALUES (?, ?, ?, ?)",
    employees
)

conn.commit()

print("Database populated successfully!")

conn.close()