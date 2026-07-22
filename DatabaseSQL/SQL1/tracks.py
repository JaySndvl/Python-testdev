import csv
import sqlite3
from pathlib import Path

folder = Path(__file__).resolve().parent
database = folder / 'trackdb.sqlite'

conn = sqlite3.connect(database)
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;

CREATE TABLE Artist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Genre (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Album (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id INTEGER,
    title TEXT UNIQUE
);

CREATE TABLE Track (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE,
    album_id INTEGER,
    genre_id INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

filename = input('Enter iTunes CSV file name: ').strip() or 'tracks.csv'
csv_path = Path(filename)
if not csv_path.is_absolute():
    csv_path = folder / csv_path

if not csv_path.is_file():
    raise FileNotFoundError(f'CSV file not found: {csv_path}')

with csv_path.open(encoding='utf-8-sig', newline='') as file:
    reader = csv.reader(file)
    imported = 0
    for row in reader:
        if len(row) != 7:
            continue

        title, artist, album, play_count, rating, length, genre = (
            value.strip() for value in row
        )

        if not all((title, artist, album, genre)):
            continue

        try:
            play_count = int(play_count)
            rating = int(rating)
            length = int(length)
        except ValueError:
            continue