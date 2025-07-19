import sqlite3

conn = sqlite3.connect("quiz.db")
cursor = conn.cursor()

for level in ["easy", "medium", "hard"]:
    cursor.execute("SELECT COUNT(*) FROM questions WHERE difficulty = ?", (level,))
    count = cursor.fetchone()[0]
    print(f"{level.capitalize()} Questions: {count}")

conn.close()
