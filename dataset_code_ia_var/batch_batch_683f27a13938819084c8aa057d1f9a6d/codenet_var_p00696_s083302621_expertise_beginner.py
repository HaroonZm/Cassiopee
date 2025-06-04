# Version débutant, avec des noms de variables explicites et une structure simple

while True:
    plen = int(input())
    if plen == 0:
        break
    cnum = int(input())
    width = int(input())
    cspace = int(input())

    def afficher_format(note):
        for i in range(plen):
            ligne = ""
            for j in range(cnum):
                index = j * plen + i
                morceau = note[index].ljust(width, ".")
                if j != 0:
                    ligne += "." * cspace
                ligne += morceau
            print(ligne)
        print("#")

    notes = []
    ligne = input()
    while ligne != "?":
        while len(notes) < plen * cnum and ligne != "":
            if len(ligne) > width:
                notes.append(ligne[:width])
                ligne = ligne[width:]
            else:
                notes.append(ligne)
                ligne = ""
        if len(notes) == plen * cnum:
            afficher_format(notes)
            notes = []
        if ligne == "":
            ligne = input()

    if notes and not all(s == "" for s in notes):
        while len(notes) < plen * cnum:
            notes.append("")
        afficher_format(notes)
    print("?")