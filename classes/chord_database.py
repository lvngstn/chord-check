class ChordDatabase:
    def __init__(self):
        self.chord_list = {
            119: "maj", 3689: "maj7", 11067: "maj9",
            121737: "maj11", 1095633: "maj11",
            357: "add9", 8211: "6/9", 1309: "add11", 
            187: "sus4", 65: "dim", 1495: "dim7", 133: "aug", 
            5423: "7sus4", 4123: "maj7#5", 3451: "7", 
            10353: "9", 113883: "11", 2619309: "13", 
            85: "m", 2465: "m7", 7395: "m9", 
            81345: "m11", 1870935: "m13", 255: "madd9", 
            5865: "m6/9", 1885: "m7b5", 91: "-5", 
            2635: "mmaj7", 2821: "maj7b5", 230: "m6/9no5",
            1015: "7#9no5"
            #  2737: "6", 51: "sus2", 561: "sus2sus4",
        }
        self.chord_db = {}

    def is_valid_id(self, chord_id):
        return chord_id in self.chord_list

    def insert_valid_chord(self, chord_voicing):
        chord_id = chord_voicing.get_string_id()
        if self.is_valid_id(chord_voicing.get_id()):
            self.chord_db[chord_id] = chord_voicing

    def get_chord_type(self, chord_id):
        return self.chord_list.get(chord_id, "Unknown")

    def format_strings_output(self, chord):
        chord_tab = ['X']*6

        for c in chord.chord_notes:
            chord_tab[c.get_open_string()] = c.get_fret()
        return chord_tab
            
    def print_all(self):
        with open("chords.txt", "w") as f:
            chords = []
            for chord in self.chord_db.values():
                root_note = chord.get_root()
                chord_type = self.get_chord_type(chord.get_id())
                formatted_output = f"{root_note}{chord_type} {self.format_strings_output(chord)}"
                chords.append((chord_type, formatted_output))

            chords.sort(key=lambda x: x[0])

            for _, formatted_output in chords:
                f.write(formatted_output + "\n")