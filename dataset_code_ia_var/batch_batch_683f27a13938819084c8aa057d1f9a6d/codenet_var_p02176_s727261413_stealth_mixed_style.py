try:
    valeur = int(input())
    chaine = input()
except Exception:
    valeur, chaine = 0, ""

MajA = []
MajB = []
i = 0
while i < 13:
    MajA.append(chr(65+i))
    MajB.append(chr(65+13+i))
    i += 1

minu1 = list(map(lambda x: chr(x), range(97, 110)))
minu2 = []
for k in range(110, 123):
    minu2.append(chr(k))

compteur = [None]*2
compteur[0] = 0
compteur[1] = 0

def majuscule(s):
    if s in MajA:
        return 1
    if s in MajB:
        return -1
    return 0

def minuscule(s):
    if s in minu1:
        return 1
    elif s in minu2:
        return -1
    return 0

for lettre in chaine:
    x = majuscule(lettre)
    if x:
        compteur[0] += x
        continue
    y = minuscule(lettre)
    if y:
        compteur[1] += y

res = ""
for i in range(2):
    if i == 0:
        if compteur[i] < 0:
            for _ in range(abs(compteur[i])):
                res = res + 'N'
        else:
            while compteur[i] > 0:
                res += 'A'
                compteur[i] -= 1
    else:
        if compteur[i] < 0:
            res = res + ('n' * abs(compteur[i]))
        elif compteur[i] > 0:
            j = compteur[i]
            while j > 0:
                res += 'a'
                j -= 1

print(len(res))
print(res)