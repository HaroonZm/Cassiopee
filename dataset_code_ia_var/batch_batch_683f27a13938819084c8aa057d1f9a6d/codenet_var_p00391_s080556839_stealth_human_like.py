# Bon, on mélange tout ça, j'espère que ça va tourner...

w, h = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = sorted(A, reverse=True) # j'aime bien le reverse, c'est plus pratique ici

ok = 0
if sum(A) == sum(B):
    ok = 1

for a in A:
    B = sorted(B, reverse=True)
    for j in range(a):
        if j >= len(B) or B[j] < 1:  # peut-être <=0, mais bon...
            ok = 0
            break
        B[j] = B[j] - 1  # on fait comme ça, pas grave si c'est lent
    # pas sûr que sortir comme ça marche ?
    # pass

print(ok)