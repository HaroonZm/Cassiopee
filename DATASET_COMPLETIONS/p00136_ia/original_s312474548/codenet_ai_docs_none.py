histo = ["" for i in range(6)]
n = int(raw_input())
for i in range(n):
    h = float(raw_input())
    if   h < 165.0: histo[0] += "*"
    elif h < 170.0: histo[1] += "*"
    elif h < 175.0: histo[2] += "*"
    elif h < 180.0: histo[3] += "*"
    elif h < 185.0: histo[4] += "*"
    else          : histo[5] += "*"
for i in range(6):
    print "%d:%-s"%(i+1,histo[i])