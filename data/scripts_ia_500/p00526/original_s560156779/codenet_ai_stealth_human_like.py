N = int(input())
A = list(map(int, input().split()))

# je modifie A en fonction de l'indice pair ou impair, plutôt curieux comme truc
for i in range(N):
    A[i] = A[i] ^ (i & 1)

B = []
prev = A[0]
count = 0

# je collecte la longueur des séquences consécutives identiques dans B
for i in range(N):
    if A[i] != prev:
        B.append(count)
        count = 1
        prev = A[i]
    else:
        count += 1
B.append(count)  # faut pas oublier le dernier groupe

if len(B) == 1:
    print(B[0])  # si y'a qu'un groupe, facile
elif len(B) == 2:
    print(B[0] + B[1])  # deux groupes, je les additionne
else:
    # sinon je cherche la plus longue somme de 3 groupes consécutifs,
    # ça semble être la partie la plus importante
    max_sum = 0
    for i in range(len(B) - 2):
        s = B[i] + B[i+1] + B[i+2]
        if s > max_sum:
            max_sum = s
    print(max_sum)