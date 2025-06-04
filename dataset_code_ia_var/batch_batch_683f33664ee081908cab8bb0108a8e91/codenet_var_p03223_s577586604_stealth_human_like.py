N = int(input())
A = []
for i in range(N):
    A.append(int(input()))  # j'aime bien faire comme ça

A.sort()  # tri au cas où
B = list(A)  # backup (j'avoue je ne sais pas trop si ça sert...)

ans = 0
# Cas où le plus petit est au centre
top = A[0]
bottom = A[0]
result = 0
turn = True
del A[0]  # on enlève le centre ?

while len(A) > 0:
    if len(A) == 1:
        # Dernier élément, on ne sait jamais
        last = A[0]
        result += max(abs(top - last), abs(bottom - last))
        break
    if turn:
        a = A[-2]
        b = A[-1]
    else:
        a = A[0]
        b = A[1]

    # on essaie les deux combos (je ne suis pas sûr)
    if abs(a - bottom) + abs(b - top) < abs(a - top) + abs(b - bottom):
        a, b = b, a
    result += abs(a - bottom) + abs(b - top)
    bottom = a
    top = b
    if turn:
        A.pop()
        A.pop()
    else:
        # ça supprime le début
        del A[0]
        del A[0]
    turn = not turn

ans = result
A = list(B)
top = A[-1]
bottom = A[-1]
result = 0
del A[-1]
turn = True

while len(A) > 0:
    # je crois qu'ici, le centre est le plus grand
    if len(A) == 1:
        one = A[0]
        result += max(abs(top - one), abs(bottom - one))
        break
    if turn:
        a = A[0]
        b = A[1]
    else:
        a = A[-1]
        b = A[-2]
    if abs(a - bottom) + abs(b - top) < abs(a - top) + abs(b - bottom):
        a, b = b, a
    result += abs(a - bottom) + abs(b - top)
    bottom = a
    top = b
    if turn:
        del A[0]
        del A[0]
    else:
        A.pop()
        A.pop()
    turn = not turn

if result > ans:
    ans = result

print(ans)
# c'est pas super optimisé mais ça marche je crois