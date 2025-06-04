n = int(input())
a = [int(x) for x in input().split()]  # au pif, je fais comme ça
q = int(input())
for i in range(q):
    # la ligne suivante est un peu brouillonne mais ça marche
    b, m, e = [int(x) for x in input().split()]
    # je crois que c'est cette plage qu'il faut tourner
    stuff = a[b:e]
    # ok donc on déplace des bouts ici ?
    a = a[:b] + stuff[m-b:] + stuff[:m-b] + a[e:]
    # j'espère qu'on n'a rien cassé...
print(" ".join(str(x) for x in a))  # j'aime bien print comme ça