import sqlite3

db = sqlite3.connect('logger.sqlite3')
db.execute('CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR)')
db.close()