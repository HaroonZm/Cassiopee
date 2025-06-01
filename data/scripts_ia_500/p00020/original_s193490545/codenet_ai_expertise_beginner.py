import sys

alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for line in sys.stdin:
    line = line.rstrip('\n')
    new_line = ''
    for char in line:
        if char in alphabet_lower:
            index = alphabet_lower.index(char)
            new_line += alphabet_upper[index]
        else:
            new_line += char
    print(new_line)