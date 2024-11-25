from itertools import permutations
from classes.chord_database import ChordDatabase
class Chord:
    def __init__(self):
        self.chord_notes = []  
        self.chord_frets = []  
        self.root_note = None  
        self.chord_id = ""  
        self.prime_id = 1
        self.note_id = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

    def add_note(self, note, fret, string):
        self.chord_notes.append(note)
        self.chord_frets.append(fret)
        if self.root_note is None:
            self.root_note = note
        self.update_string_id(fret, string)

    def calculate_ids(self):
        chord_db = ChordDatabase()
        potential_ids = set()
        note_perms = permutations(self.chord_notes)

        for note_perm in note_perms:
            self.root_note = note_perm[0]
            potential_id = 1

            for note in note_perm:
                interval =  self.root_note - note
                potential_id *= self.note_id[interval]
            if chord_db.is_valid_id(potential_id):
                potential_ids.add(potential_id)
                break
        return list(potential_ids)

    def set_id(self, id):
        self.prime_id = id

    def get_id(self):
        return self.prime_id

    def update_string_id(self, fret, string):
        self.chord_id += f"{string}:{fret};"

    def get_string_id(self):
        return self.chord_id

    def get_root(self):
        return self.root_note

    def get_frets(self):
        return self.chord_frets

    def print(self, flat_or_sharp=0):
        for note in self.chord_notes:
            note.print(flat_or_sharp)
