import json
import sqlite3
from pathlib import Path

folder = Path(__file__).resolve().parent

conn = sqlite3.connect(folder / 'rosterdb.sqlite')
cur = conn.cursor()

cur.executescript('''
''')


filename = input('Enter file name: ').strip() or 'roster_data.json'
json_path = Path(filename)
if not json_path.is_absolute():
    json_path = folder / json_path

if not json_path.is_file():
    raise FileNotFoundError(f'JSON file not found: {json_path}')

with json_path.open(encoding='utf-8') as file:
    json_data = json.load(file)

for entry in json_data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    print((name, title, role))

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES (?, ?, ?)''',
        (user_id, course_id, role))
    
conn.commit()
cur.close()
conn.close()