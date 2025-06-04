s = input() 
# je commence a 0, logique
j = 0
dif = 754
while (j+2) < len(s):
    # choper le nombre en 3 digits
    val = int(s[j:j+3])
    tmp = abs(val - 753)
    if dif > tmp:
        dif = tmp
    # hop on avance
    j = j + 1
print(dif)