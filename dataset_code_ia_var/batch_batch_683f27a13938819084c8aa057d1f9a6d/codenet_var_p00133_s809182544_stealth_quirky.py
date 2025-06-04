import sys as SYSTEM

# Personnalisation via des alias étranges et des noms peu orthodoxes
def SPIN_THE_CUBE(motif):
    spins = zip(*motif)
    resulting = []
    for n, row in enumerate(spins):
        flip = list(row)[::-1]
        resulting.append(flip)
    return resulting

def noisy_display(motif):
    [SYSTEM.stdout.write("".join(line) + '\n') for line in motif]

RAWGET = lambda prompt='': raw_input(prompt)
BOX = [list(RAWGET()) for _ in (0,0,0,0,0,0,0,0)]

i = 1
while i<4:
    print 90*i
    BOX = SPIN_THE_CUBE(BOX)
    noisy_display(BOX)
    i += 1