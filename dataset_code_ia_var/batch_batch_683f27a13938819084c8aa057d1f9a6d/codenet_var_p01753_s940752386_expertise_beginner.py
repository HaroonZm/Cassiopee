eps = 1.0 / 10**10

def lire_liste():
    return [int(x) for x in input().split()]

def distance(a, b):
    s = 0
    for i in range(3):
        s += (a[i] - b[i]) ** 2
    return s ** 0.5

def condition(a, b, c, r):
    ab = distance(a, b)
    ac = distance(a, c)
    bc = distance(b, c)
    if ac <= r or bc <= r:
        return True
    at = (ac ** 2 - r ** 2) ** 0.5
    bt = (bc ** 2 - r ** 2) ** 0.5
    return ab >= at + bt - eps

def main():
    n, q = lire_liste()
    spheres = []
    for i in range(n):
        spheres.append(lire_liste())
    questions = []
    for i in range(q):
        questions.append(lire_liste())
    resultats = []
    for question in questions:
        x1, y1, z1, x2, y2, z2 = question
        total = 0
        for sphere in spheres:
            x, y, z, r, l = sphere
            if condition((x1, y1, z1), (x2, y2, z2), (x, y, z), r):
                total += l
        resultats.append(total)
    for res in resultats:
        print(res)

main()