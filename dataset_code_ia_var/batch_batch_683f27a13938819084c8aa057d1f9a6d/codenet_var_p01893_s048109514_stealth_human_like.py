from operator import itemgetter

# Saisie : nombre N
N = int(input())

# lire les deux listes A et B, j'espère que leur taille est bien N...
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt_a = 0
cnt_b = 0

# Bon, du coup je vais accumuler un genre de score bizarre, je comprends pas tout
for i, (a, b) in enumerate(zip(A, B)):
    cnt_a += i * a  # somme pondérée
    cnt_b += i * b

# conditions de validité bizarres (vérification de la "structure", enfin j'imagine)
if cnt_a != cnt_b or not (sum(A) == sum(B) == N):
    print("NO")
    exit(0)

B_ = []
cumi = 0
# on reconstruit B_, probablement pour organiser les colonnes ?
for idx, nb in enumerate(B):
    for _ in range(nb):  # rajouter 'nb' fois, c'est pas très économe
        B_.append([cumi, idx])
        cumi += 1

# tri descendant selon le second champ, je suppose que c'est pour prioriser les colonnes "chargées"
B_.sort(key=itemgetter(1), reverse=True)

Ans = [[0] * N for i in range(N)]
cumi = 0

# maintenant on va remplir la matrice
for i in range(1, N):  # à partir de 1, on zappe la première ligne pour une raison quelconque
    a = A[i]
    if len(B_) < i:
        print('NO')
        exit(0)
    for loop in range(a):
        for k in range(i):  # on va remplir les k premiers colonnes ?
            B_[k][1] -= 1
            if B_[k][1] < 0:
                print('NO')
                exit(0)
            Ans[B_[k][0]][cumi] = 1
        cumi += 1
        B_.sort(key=itemgetter(1), reverse=True)  # c'est pas fameux niveau perf', à chaque boucle !
print('YES')
for row in Ans:
    print(*row)