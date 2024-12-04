import sqlite3

conn = sqlite3.connect('chords.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS Chord (
    root_note VARCHAR(2) NOT NULL,
    chord_type VARCHAR(10) NOT NULL,
    string_id INT PRIMARY KEY,
    chord_tab CHAR(6) NOT NULL,
    number_of_notes INT NOT NULL,
    bass_note VARCHAR(2) NOT NULL,
    chord_shape BOOL NOT NULL,
    open_chord BOOL NOT NULL
)
''')

conn.commit()
conn.close()
