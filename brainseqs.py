#!/bin/python2

from pyo import *
from sequencer import *
from helpers import *
import sys
import time

pyo_server = Server().boot()

if len(sys.argv) == 2:
    code = read(sys.argv[1])
else:
    print("NOOOOOOOOOOOO")
    exit()

sequence = Sequence()
duration = 0

# Parse brainfuck code
code     = cleanup(list(code))
bracemap = buildbracemap(code)

cells, codeptr, cellptr = [0], 0, 0

while codeptr < len(code):
    command = code[codeptr]

    if command == ">":
        cellptr += 1
        if cellptr == len(cells): cells.append(0)

    if command == "<":
        cellptr = 0 if cellptr <= 0 else cellptr - 1

    if command == "+":
        cells[cellptr] = cells[cellptr] + 1 if cells[cellptr] < 127 else -127

    if command == "-":
        cells[cellptr] = cells[cellptr] - 1 if cells[cellptr] > -127 else 127

    if command == "[" and cells[cellptr] == 0: codeptr = bracemap[codeptr]
    if command == "]" and cells[cellptr] != 0: codeptr = bracemap[codeptr]
    if command == ".": sequence.append(Note(cells[cellptr], duration))
    if command == ",": duration = 2**cells[cellptr]

    codeptr += 1

for i in sequence.notes:
    print(i.note, i.duration)

# Start music !
sequence.play()
osc = LFO(freq=sequence.signal)
# In Stereo !
pan = Pan(osc).out()

pyo_server.start()
pyo_server.setAmp(0.3)

# Sleep for the duration of the melody
sleep = 0

for note in sequence.notes:
    sleep += note.time(sequence.tempo)

time.sleep(sleep)
