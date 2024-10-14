from note import Note

class Fretboard:
    def __init__(self):
        self.open_strings = [Note('E', 2), Note('A', 2), Note('D', 3), 
                             Note('G', 3), Note('B', 3), Note('E', 4)]
        
        self.the_fretboard = []
        for string in self.open_strings:
            current_string = []
            note = Note(string.get_name(), string.get_octave())
            for fret in range(12):
                current_string.append(note)
                note = Note(note.get_name(), note.get_octave())
                note.increment()
            self.the_fretboard.append(current_string)

    def __getitem__(self, index):
        return self.the_fretboard[index]

    def get_open_string(self, index):
        return self.open_strings[index]

    def get_note_at(self, string, fret):
        return self.the_fretboard[string][fret]

    def display(self):
        for string in self.the_fretboard:
            for note in string:
                note.print_note(2)
                print(", ", end="")
            print("\n")
