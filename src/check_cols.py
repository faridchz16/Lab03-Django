import sqlite3
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

tables = ['quiz_exam', 'quiz_question', 'quiz_choice']
for table in tables:
    print(f"\nColumns in {table}:")
    cursor.execute(f"PRAGMA table_info({table})")
    columns = cursor.fetchall()
    for col in columns:
        print(f"  {col}")

conn.close()