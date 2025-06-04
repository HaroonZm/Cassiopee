plen = int(input())
while plen != 0:
    cnum = int(input())
    width = int(input())
    cspace = int(input())

    def formated_print(note):
        for i in range(plen):
            row = ""
            for j in range(cnum):
                if j > 0:
                    row += "." * cspace
                idx = j * plen + i
                row += note[idx].ljust(width, ".")
            print(row)
        print("#")

    note = []
    line = input()
    while line != "?":
        if len(note) >= plen * cnum:
            formated_print(note)
            note = []
        if len(line) > width:
            note.append(line[:width])
            line = line[width:]
        else:
            note.append(line)
            line = ""
        if line == "":
            line = input()
    if note:
        while len(note) < plen * cnum:
            note.append("")
        formated_print(note)
    print("?")
    plen = int(input())