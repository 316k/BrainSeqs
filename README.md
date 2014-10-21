BrainSeqs
================

BrainSeqs (pronounced *BrainSex*) is a brainfuck-based musical sequencer.

## Installation

BrainSeqs requires python2.* and the audio library
[Pyo](http://ajaxsoundstudio.com/software/pyo/).

## Usage

Run `python2 brainseqs.py my/brainfuck/sequence` to listen to a file

## Examples

See the files in [the `examples` folder](/examples)

Protip: you can run the examples directly with `brainseqs.py`

## Syntax

To write your melodies, you have access to all of the eight brainfuck commands :

* **+** : Increments the current pointer's value
* **-** : Decrements the current pointer's value
* **>** : Switch to the next pointer
* **<** : Switch to the previous pointer
* **[** : Begin loop (if the current pointer's value is not 0)
* **]** : End loop if the current pointer's value is 0, else go to the beginning
of the current loop
* **.** : Add a note to the stack with the current pointer's value as the midi
note with the last updated duration (default : 0)
* **,** : Sets the note duration to 2^(current pointer's value)

## Attribution

* The brainfuck interpreter code is loosely based on this
[Python-Brainfuck](https://github.com/pocmo/Python-Brainfuck) interpreter
* The sequencer class is a modified version of Adelrune's class
