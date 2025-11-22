import sqlite3

# creating of a table
connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

cursor.execute('''
INSERT INTO users (id, name, email) VALUES(2, 'Joan', 'joan@example.com')
''')

connection.commit()
connection.close()
