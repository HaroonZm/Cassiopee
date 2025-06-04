liste = []
for i in range(101):
    liste.append(0)

while True:
    valeurs = input()
    p_s = valeurs.split(",")
    p = int(p_s[0])
    s = int(p_s[1])
    if p == 0 and s == 0:
        break
    liste[p] = s

val_uniques = []
for val in liste:
    if val not in val_uniques:
        val_uniques.append(val)
val_uniques.sort(reverse=True)

while True:
    try:
        q_str = input()
        q = int(q_str)
    except EOFError:
        break
    print(val_uniques.index(liste[q]) + 1)