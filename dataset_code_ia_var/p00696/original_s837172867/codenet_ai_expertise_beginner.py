# On suppose l'exécution sous Python 2 (car usage de raw_input, print sans parenthèses, xrange...)
# Version simple, structurée pour débutant

def formated_print(note, plen, cnum, width, space):
    i = 0
    while i < plen:
        line = []
        j = 0
        while j < cnum:
            idx = j * plen + i
            text = note[idx].ljust(width, ".")
            line.append(text)
            j += 1
        print space.join(line)
        i += 1
    print "#"

while True:
    plen = int(input())
    if plen == 0:
        break
    cnum = int(input())
    width = int(input())
    space_count = int(input())
    space = "." * space_count

    note = []
    line = raw_input()
    while line != "?":
        # Couper la ligne si trop longue
        while len(line) > 0:
            if len(note) >= plen * cnum:
                formated_print(note, plen, cnum, width, space)
                note = []
            if len(line) > width:
                note.append(line[:width])
                line = line[width:]
            else:
                note.append(line)
                line = ""
        line = raw_input()

    # Afficher la dernière note si elle existe
    if len(note) > 0:
        while len(note) < plen * cnum:
            note.append("")
        formated_print(note, plen, cnum, width, space)
    print "?"