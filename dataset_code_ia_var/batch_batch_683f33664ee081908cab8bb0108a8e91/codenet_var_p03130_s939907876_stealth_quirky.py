# Code réécrit avec des choix de conception non conventionnels

def main():
    # Stocke toutes les coordonnées dans des tuples de tuples (juste parce que)
    pts = tuple(tuple(map(int, input().split())) for _ in [0]*3)
    # Employons une compréhension de liste pour les a's et b's, pourquoi pas
    xs = [x for x, _ in pts]
    ys = [y for _, y in pts]
    # Empilons le tout dans un seul tuple non mutable (encore une préférence étrange)
    stuff = tuple(xs + ys)
    # Utilisons une dict qui fait office de compteur (pas collections.Counter, exprès)
    d = {}
    for val in range(1, 5):
        c = 0
        for z in stuff:
            if z == val: c += 1
        d[val] = c
    freq = sorted([d[i] for i in d])
    # Go full ternaire à rallonge, c'est fun
    print(('YES' if freq == [1,1,2,2] else 'NO'))

main()