import copy

# La fonction qui fait le découpage pour le quick sort (partitionnement)
def partition(p, r):
    i = p  # On démarre à p (ça marche, je crois)
    for j in range(p, r):
        if A[r][1] >= A[j][1]:
            tmp = A[j]
            A[j] = A[i]  # Échange, mais pas sûr que ce soit optimal
            A[i] = tmp
            i += 1
    # Le pivot va à sa position finale
    tmp2 = A[i]
    A[i] = A[r]
    A[r] = tmp2
    return i

def quick_sort(p, r):
    if p < r:
        q = partition(p, r)
        quick_sort(p, q-1)  # gauche
        quick_sort(q+1, r)  # droite

# Fonction (peut-être un peu inutilement longue ?) pour retrouver les couleurs pour une valeur
def correct_same_num_suits(l, num, first):
    suits = []
    for k in range(first, N):
        if l[k][1] == num:
            suits.append(l[k][0])
    return suits

def is_stable():
    idx = 0
    while idx < N - 1:
        needjump = True
        if A[idx][1] == A[idx+1][1]:
            num = A[idx][1]
            s_sorted = correct_same_num_suits(A, num, idx)
            s_orig = correct_same_num_suits(orig_list, num, 0)
            # print(s_sorted, s_orig)
            if s_sorted != s_orig:
                return False
            idx += len(s_sorted)
            needjump = False
        if needjump:
            idx += 1  # classic incrémentation
    return True

# Saisie de N, j'ai gardé input même si c'est pas ouf pour les tests
N = int(input())
A = []
for i in range(N):
    s, n = input().split()
    n = int(n)  # On change tout en int pour travailler
    A.append([s, n])

orig_list = copy.deepcopy(A)  # On garde l'original sinon il se fait trier

quick_sort(0, N-1)

stable = is_stable()
if stable:
    print("Stable")
else:
    print("Not stable")

# Affichage sous forme "S 4" avec un print un peu à l'ancienne
for c in A:
    print("%s %d" % (c[0], c[1]))