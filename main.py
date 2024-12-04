from classes.fretboard import Fretboard
from classes.chord_database import ChordDatabase
from classes.chord import Chord
from itertools import permutations
from itertools import product

def build_open_strings(n_strings):
    all_open_strings = set()

    open_strings = []
    for i in range(n_strings):
        open_strings.append(1)
    for i in range(6-n_strings):
        open_strings.append(0)
    
    all_n_open_strings = set(permutations(open_strings))
    for n in all_n_open_strings:
        all_open_strings.add(n)


    formatted_strings = []
    for n in all_open_strings:
        formatted_string = format_strings_input(n)
        formatted_strings.append(formatted_string)

    return formatted_strings

def format_strings_input(guitar_strings):
    return [index for index, value in enumerate(guitar_strings) if value == 1]

def generate_possible_chords_with_n_notes(n_strings, stretch, max_fret, shapes_only, open_chords):
    valid_combinations = []
    
    for pos in product(range(max_fret + 1), repeat=n_strings):
        non_zero_numbers = []
        if open_chords:
            non_zero_numbers = [num for num in pos if num != 0] 
        else:
            non_zero_numbers = pos

        if non_zero_numbers:
            max_pos, min_pos = max(non_zero_numbers), min(non_zero_numbers)
            if max_pos - min_pos > stretch:
                continue
            if shapes_only and 0 not in pos:
                continue
            if shapes_only and min_pos > stretch:
                continue
            if n_strings == 5 and 0 not in pos and pos.count(min_pos) < 2:
                continue
            if n_strings == 6 and 0 not in pos and pos.count(min_pos) < 3:
                continue
            if n_strings == 6 and pos.count(0) < 2:
                continue
            valid_combinations.append(pos) 

    return valid_combinations

def generate_chords(guitar, chord_db, chord_comb, formatted_strings):
    positions = []
    for i in range(len(formatted_strings)):
        positions.append((chord_comb[i], formatted_strings[i]))

    validate_and_store_chords(guitar, positions, chord_db)

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
    STRETCH = 3
    FRETS = 11
    SHAPES_ONLY = True
    OPEN_CHORDS = True
    
    for i in (6,):
        open_strings = build_open_strings(i)
        n_note_combs = generate_possible_chords_with_n_notes(i, STRETCH, FRETS, SHAPES_ONLY, OPEN_CHORDS)
        for j in open_strings:
            for k in n_note_combs:
                generate_chords(guitar, chord_db, k, j)

    chord_db.print_all()

if __name__ == "__main__":
    main()