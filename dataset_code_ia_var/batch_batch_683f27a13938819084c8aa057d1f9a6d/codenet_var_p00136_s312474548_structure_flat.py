histo = ["", "", "", "", "", ""]
n = int(raw_input())
i = 0
while i < n:
    h = float(raw_input())
    if h < 165.0:
        histo[0] += "*"
    else:
        if h < 170.0:
            histo[1] += "*"
        else:
            if h < 175.0:
                histo[2] += "*"
            else:
                if h < 180.0:
                    histo[3] += "*"
                else:
                    if h < 185.0:
                        histo[4] += "*"
                    else:
                        histo[5] += "*"
    i = i + 1

i = 0
while i < 6:
    print "%d:%-s" % (i+1, histo[i])
    i = i + 1