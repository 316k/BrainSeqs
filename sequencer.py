from pyo import Pattern, midiToHz, Sig, Trig

class Sequence:
    """Sequence of midi notes and rythms """

    def __init__(self, notes = [], tempo=120):
        self.signal = Sig(0)
        self.notes = notes
        self.tempo = float(tempo)
        self.index = 0
        self.trigger = Trig()

    def append(self, note):
            self.notes.append(note)

    def next(self):
        self.signal.setValue(self.notes[self.index].frequency())
        self._pattern.time = self.notes[self.index].time(self.tempo)

        self.index = (self.index + 1) % len(self.notes)
        self.trigger.play()

    def play(self):
        self._pattern = Pattern(self.next, self.notes[0].time(self.tempo))
        self._pattern.play()


class Note:
    def __init__(self, note, duration):
        self.note = note
        self.duration = duration

    def frequency(self):
        return midiToHz(self.note)

    def time(self, tempo):
        return (tempo * self.duration)/60.
