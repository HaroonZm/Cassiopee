def lire_nombre():
    return int(input())

def lire_liste():
    return [int(x) for x in input().split()]

elements = ["KIH", "B", "R", ""]
possibilites = []

for i in range(32):  # 1 << 5 = 32
    mot = ""
    for j in range(4):
        if ((i >> j) & 1) == 1:
            mot += "A"
        mot += elements[j]
    possibilites.append(mot)

mot_utilisateur = input()
if mot_utilisateur in possibilites:
    print("YES")
else:
    print("NO")