class Note:
    open_string = 0
    fret = 0

    def __init__(self, name='A', octave=0):
        self.name = name
        self.octave = octave

    def __hash__(self):
        return hash((self.name))

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.name == other.name
        return False

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_octave(self):
        return self.octave

    def set_octave(self, new_octave):
        self.octave = new_octave

    def set_pos(self, s, f):
        self.open_string = s
        self.fret = f

    def get_fret(self):
        return self.fret
    
    def get_open_string(self):
        return self.open_string

    def __sub__(self, other):
        chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self_index = chromatic_scale.index(self.name)
        other_index = self_index
        res = 0
        while chromatic_scale[other_index] != other.name:
            res += 1
            other_index = (other_index + 1) % 12

        return res

    def __repr__(self):
        return f"{self.name}"

    def increment(self):
        chromatic_scale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        current_index = chromatic_scale.index(self.name)
        next_index = (current_index + 1) % len(chromatic_scale)
        self.name = chromatic_scale[next_index]
        
        if next_index == 0:
            self.octave += 1

    def print_note(self, flat_or_sharp=0):
        flats = {'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab', 'A#': 'Bb'}
        if flat_or_sharp == 1 and self.name in flats:
            print(f"{flats[self.name]}{self.octave}", end="")
        else:
            print(f"{self.name}{self.octave}", end="")
