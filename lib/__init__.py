import sqlite3

CONN = sqlite3.connect('my_students.db')
CURSOR = CONN.cursor()