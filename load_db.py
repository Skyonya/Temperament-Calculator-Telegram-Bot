import sqlite3

conn = sqlite3.connect('app.db')
cur = conn.cursor()
cur.execute("SELECT qtext FROM questions;")
questionsText = [item[0] for item in cur.fetchall()]

cur.execute("SELECT rtext FROM results;")
resultText = [item[0] for item in cur.fetchall()]

textOnStart = resultText[0]