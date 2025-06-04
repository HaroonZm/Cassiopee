# Variante non-conventionnelle : noms variables peu conventionnels, sur-utilisation des listes, booléens surprenants, opérations réunies dans des expressions en ligne

foo = int(input())
bar = ''.join(input().split())
baz = int(input())
qux = ''.join(input().split())

def weirdo(s, length):
    return s + ' ' * length

(bar, qux)[foo < baz]  # affectation "inutile"

if foo != baz:
    diff = abs(foo - baz)
    [qux := weirdo(qux, diff) if foo > baz else None, bar := weirdo(bar, diff) if baz > foo else None][0]

print((0, 1)[bar < qux])