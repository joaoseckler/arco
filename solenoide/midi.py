#!/usr/bin/env python3

# 'arquivo.mid'

# Lê esse arquivo e imprime os note_on e as notas

from mido import MidiFile, tick2second, MetaMessage, merge_tracks
from jinja2 import Template

def make_dict():
    mid = MidiFile('file.mid')
    acc = 0
    tempo = 500000
    ret = {'notas': '', 'note_on': '', 'n_notas': ''}
    k = 0

    ret['notas'] += 'const int notas[] = {'
    for msg in merge_tracks(mid.tracks):
        if msg.type == 'note_on' and msg.velocity > 0:
            k += 1
            ret['notas'] += str(msg.note) + ', '

    ret['notas'] += '}'

    ret['note_on'] += 'const int note_on[] = {'
    for msg in merge_tracks(mid.tracks):
        if isinstance(msg, MetaMessage) and msg.type == 'set_tempo':
            tempo = msg.tempo
        if hasattr(msg, 'time'):
            acc += msg.time
        if msg.type == 'note_on' and msg.velocity > 0:
            ret['note_on'] += str(int(tick2second(acc, mid.ticks_per_beat, tempo) * 1000))  + ', '
    ret['note_on'] += '}'
    ret['n_notas'] += str(k)

    return ret


with open('template.ino.jinja2', 'r') as f:
    template = Template(f.read())

with open('file.ino', 'w') as f:
    f.write(template.render(make_dict()))
