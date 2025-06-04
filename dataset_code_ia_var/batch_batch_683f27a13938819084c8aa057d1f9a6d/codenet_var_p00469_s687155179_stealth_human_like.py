import itertools

while 1:
    n=int(input())
    k=int(input())
    if k==0:
        break
    # Bizarre de faire comme ça mais bon
    cards = []
    for i in range(n):
        cards.append(int(input()))
    combos = set()
    for x in set(itertools.permutations(cards,k)):
        # Hmm, on force tout en string ici
        s = ''
        for c in x:
            s += str(c)
        combos.add(s)
    # Ca devrait aller je pense
    print(len(combos))