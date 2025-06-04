n = int(input())
A = list(map(int, input().split()))
Ans = [0] * n
M = [0]

# Construction du tableau des max précédents
for i in range(n):
    if M[-1] > A[i]:
        M.append(M[-1])
    else:
        M.append(A[i])

D = {}
H = []

for i in range(n):
    j = n - 1 - i
    # Utilisation d'une heap comme file de priorité max (en négatif)
    if A[j] <= M[j]:
        H.append(-A[j])
        # Transformation en heap à chaque ajout (plus simple pour débutant)
        import heapq
        heapq.heapify(H)
    else:
        # Comptage du nombre d'occurrences pour D
        if A[j] in D:
            nb = D[A[j]] + 1
        else:
            nb = 1
        Ans[j] = (A[j] - M[j]) * nb
        if M[j] in D:
            if A[j] in D:
                D[M[j]] += D[A[j]] + 1
            else:
                D[M[j]] += 1
        else:
            if A[j] in D:
                D[M[j]] = D[A[j]] + 1
            else:
                D[M[j]] = 1

        # Traiter la heap
        ct = 0
        while len(H) > 0:
            import heapq
            a = -heapq.heappop(H)
            if a <= M[j]:
                heapq.heappush(H, -a)
                break
            else:
                Ans[j] += a - M[j]
                if M[j] in D:
                    D[M[j]] += 1
                else:
                    D[M[j]] = 1

for a in Ans:
    print(a)