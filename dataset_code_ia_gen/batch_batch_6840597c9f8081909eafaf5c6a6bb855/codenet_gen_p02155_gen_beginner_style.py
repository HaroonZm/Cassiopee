N, D = map(int, input().split())
a = list(map(int, input().split()))

# Comme la taille maximale à enlever est D et on ne peut pas enlever plus que D,
# on peut considérer chaque a_i modulo (D+1).
# Si la xor des valeurs a_i % (D+1) est zéro, alors le second joueur gagne, sinon le premier.

xor_sum = 0
for length in a:
    xor_sum ^= (length % (D + 1))

if xor_sum == 0:
    print("Second")
else:
    print("First")