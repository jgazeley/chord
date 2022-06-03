from sys import argv

seq = [1, 2, 2, 2, 1, 2, 2]
tones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

n = 0

def flat(note):
	index = tones.index(note)
	print(tones[(index -1) % 12])

def sharp(note):
	index = tones.index(note)
	print(tones[(index +1) % 12])

if argv[1] == 'C':
	i = 0
if argv[1] == 'C#':
	i = 1
if argv[1] == 'D':
	i = 2
if argv[1] == 'D#':
	i = 3
if argv[1] == 'E':
	i = 4
if argv[1] == 'F':
	i = 5
if argv[1] == 'F#':
	i = 6
if argv[1] == 'G':
	i = 7
if argv[1] == 'G#':
	i = 8
if argv[1] == 'A':
	i = 9
if argv[1] == 'A#':
	i = 10
if argv[1] == 'B':
	i = 11

scale = []

while n < 8:
	scale.append(tones[i % 12])
	if n < 7:
		i += seq.pop()
	n += 1

# print(scale)

# MAJOR
if argv[2] == 'M':
	print(scale[1 - 1])
	print(scale[3 - 1])
	print(scale[5 - 1])

if argv[2] == '6':
	print(scale[1 - 1])
	print(scale[3 - 1])
	print(scale[5 - 1])
	print(scale[6 - 1])

if argv[2] == '7':
	print(scale[1 - 1])
	print(scale[3 - 1])
	print(scale[5 - 1])
	flat(scale[7 - 1])

if argv[2] == 'M7':
	print(scale[1 - 1])
	print(scale[3 - 1])
	print(scale[5 - 1])
	print(scale[7 - 1])

if argv[2] == 'M9':
	print(scale[1 - 1])
	print(scale[3 - 1])
	print(scale[5 - 1])
	print(scale[7 - 1])
	print(scale[(9 - 1) % 7])

if argv[2] == 'M13':
	print(scale[1 - 1])
	print(scale[3 - 1])
	print(scale[5 - 1])
	print(scale[7 - 1])
	print(scale[(9 - 1) % 7])
	print(scale[(13 - 1) % 7])

# MINOR
if argv[2] == 'm':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])

if argv[2] == 'm+9':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	print(scale[(9 - 1) % 7])

if argv[2] == 'm6':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	print(scale[6 - 1])

if argv[2] == 'mb6':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	flat(scale[6 - 1])

if argv[2] == 'm7':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	flat(scale[7 - 1])

if argv[2] == 'm7b5':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	flat(scale[5 - 1])
	flat(scale[7 - 1])

if argv[2] == 'm9':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	flat(scale[7 - 1])
	print(scale[(9 - 1) % 7])

if argv[2] == 'm11':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	flat(scale[7 - 1])
	print(scale[(9 - 1) % 7])
	print(scale[(11 - 1) % 7])

if argv[2] == 'm13':
	print(scale[1 - 1])
	flat(scale[3 - 1])
	print(scale[5 - 1])
	flat(scale[7 - 1])
	print(scale[(9 - 1) % 7])
	print(scale[(11 - 1) % 7])
	print(scale[(13 - 1) % 7])

# SHARP / FLAT
if argv[2] == 'sharp':
	sharp(scale[(1 - 1) % 7])
	sharp(scale[(3 - 1) % 7])
	sharp(scale[(5 - 1) % 7])

if argv[2] == 'flat':
	flat(scale[(1 - 1) % 7])
	flat(scale[(3 - 1) % 7])
	flat(scale[(5 - 1) % 7])