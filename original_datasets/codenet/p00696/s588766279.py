while True:
    plen = input()
    if plen == 0:
        break
    cnum = input()
    width = input()
    cspace = input()
    def formated_print(note):
        for i in xrange(plen):
            print ("."*cspace).join(note[j*plen+i].ljust(width, ".") for j in xrange(cnum))
        print "#"
    note = []
    line = raw_input()
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
            line = raw_input()
    if note:
        while len(note) < plen * cnum:
            note.append("")    
        formated_print(note)
    print "?"