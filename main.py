from fretboard import Fretboard
from chord_database import ChordDatabase
from chord import Chord
from itertools import permutations

def generate_chords(guitar, open_strings, stretch, chord_db):
    for i in range(12):
        for j in range(max(0, i - stretch), min(12, i + stretch)):
            for k in range(max(0, j - stretch), min(12, j + stretch)):
                for l in range(max(0, k - stretch), min(12, k + stretch)):
                    min_val = min(i, j, k, l)
                    max_val = max(i, j, k, l)
                    
                    if max_val - min_val <= stretch:
                        positions = [(i, open_strings[0]), 
                                        (j, open_strings[1]),
                                        (k, open_strings[2]),
                                        (l, open_strings[3])]
                        validate_and_store_chords(guitar, positions, chord_db)

def format_strings_input(guitar_strings):
    return [index for index, value in enumerate(guitar_strings) if value == 1]

def validate_and_store_chords(guitar, positions, chord_db):
    chord = Chord()
    for fret, string in positions:
        note = guitar.get_note_at(string, fret)
        note.set_pos(string, fret)
        chord.add_note(note, fret, string)

    ids = chord.calculate_ids()
    
    for i in ids:
        if chord_db.is_valid_id(i):
            chord.set_id(i)
            chord_db.insert_valid_chord(chord)
            break

def main():
    guitar = Fretboard()
    chord_db = ChordDatabase()
    four_note_open_strings = set(permutations([1, 1, 1, 1, 0, 0]))
    
    for open_strings in four_note_open_strings:
        generate_chords(guitar, format_strings_input(open_strings), 3, chord_db)

    chord_db.print_all()

if __name__ == "__main__":
    main()