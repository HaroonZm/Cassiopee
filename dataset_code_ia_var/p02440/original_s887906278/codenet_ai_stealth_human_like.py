# Hum, bon, essayons de faire ça "à la main"
N=int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    temp = input().split()
    # ok on va bricoler, je sépare tout vite fait
    qtype = int(temp[0])
    b = int(temp[1])
    e = int(temp[2])

    if qtype==0:
        # alors là on veut clairement le minimum
        print(min(A[b:e])) # pfiu, j'espère que b<e etc
    else:
        # ça doit être 1 normalement... enfin bref
        if qtype==1:
            print(max(A[b:e])) # pareil mais pour le max
        # bon si c'est d'autres types on fait rien, osef