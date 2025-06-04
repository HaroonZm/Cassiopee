# Majuscules non conventionnelles, liste comme attribut de classe, lambda pour filter, pas de comprehensions
class Confs:
    ATTR = []

EXEC = lambda: (
    [Confs.ATTR.append(int(x)) for x in input().split()],
    [(N, M := (lambda a, b: (int(a), int(b)))(*input().split()))],
    print(M - len(list(filter(lambda x: x <= M, Confs.ATTR))))
)
EXEC()