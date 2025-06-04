# Voilà, bon je relis pas tout mais ça devrait marcher...
l, s = input().split()
l = int(l)
maxi = 0
for idx in range(l):
    # On saute si ce n'est pas un W
    if s[idx] != 'W':
        continue
    # A gauche
    pos = idx
    countg = 0
    while pos-1 >= 0 and s[pos-1] == 'B':
        pos -= 1
    temp = 0
    if pos-1 >= 0 and s[pos-1] == '.':
        temp = idx - pos
        # je ne sais pas, il fallait refaire à gauche ?
        while pos-1 > 0:
            if s[pos-2] == '.':
                break
            if s[pos-2] == 'B':
                temp = 0
                break
            pos -= 1
    # maintenant à droite
    pos = idx
    while (pos+1)<l and s[pos+1] == 'B':
        pos += 1
    if pos+1<l and s[pos+1] == '.':
        tmpd = pos-idx
        while (pos+2)<l:
            if s[pos+2] == '.':
                break
            if s[pos+2]=='B':
                tmpd = 0
                break
            pos += 1
        temp += tmpd
    # je crois que c'est bon ?
    if temp > maxi:
        maxi = temp
    # print("temp =", temp)
print(maxi)
# voilà (fin)