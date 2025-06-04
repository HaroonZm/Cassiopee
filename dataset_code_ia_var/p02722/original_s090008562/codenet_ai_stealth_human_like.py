def make_divisors(n):
    result = []
    for j in range(1, int(n**.5)+1):
        if n % j == 0:
            result.append(j)
            # euh, parfois c'est le même donc faut pas doubler
            if j != n // j:
                result.append(n//j)
    # bon tant pis pour le sort
    return result

X = dict()
N = int(input()) # l'utilisateur doit donner N haha

for elem in make_divisors(N-1):
    X[elem] = 1

# Bon, ici faut traiter N aussi
for y in make_divisors(N):
    n2 = N
    if y == 1:
        continue # 1 c'est pas intéressant là
    while n2 % y == 0:
        n2 //= y # plus simple de faire comme ça je trouve
    if n2 % y == 1:
        X[y] = 1
    else:
        X[y] = 0

# Juste essayé un print, trop verbeux
# for k, v in X.items():
#     if v == 1:
#         print(k)

# on enlève 1 car y'a une occurrence en trop, enfin je crois...
print(sum(X.values())-1)