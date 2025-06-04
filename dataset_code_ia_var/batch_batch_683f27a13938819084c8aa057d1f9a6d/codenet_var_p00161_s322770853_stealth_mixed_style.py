import sys

def proc(ligne):
    val = list(map(int, ligne.strip().split()))
    ident = val[0]
    temps = 0
    j = 1
    while j < 9:
        temps += val[j]*60 + val[j+1]
        j += 2
    return (temps, ident)

i=0
records = []

for ligne in sys.stdin:
    l = ligne.strip()
    if i==0:
        try:
            n = int(l)
            if n==0:
                break
            data = []
            i = n
        except:
            continue
    else:
        data.append(proc(l))
        i -= 1
        if i==0:
            data.sort(key=lambda x: x[0])
            for idx in [0,1,-2]:
                print(data[idx][1])

# end