ref = ["= ****","=* ***","=** **","=*** *","=**** "]
try:
    n = raw_input()
    while True:
        n = "0" * (5 - len(n)) + n
        abacus = ["", "", "", "", ""]
        i = 4
        while i >= 0:
            if int(n[i]) < 5:
                abacus[i] += "* "
            else:
                abacus[i] += " *"
            abacus[i] += ref[int(n[i]) % 5]
            i -= 1
        i = 0
        while i < 8:
            a = ""
            j = 0
            while j < 5:
                a += abacus[j][i]
                j += 1
            print a
            i += 1
        n = raw_input()
        print
except:
    pass