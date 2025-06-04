import sys

def main():
    data = sys.stdin.read().split()
    N = int(data[0])
    A = list(map(int, data[1:]))

    # Vérification du nombre de 90 et 270
    n90 = 0
    for x in A:
        if x == 90:
            n90 += 1
    if n90 - (N - n90) != 4:
        print(-1)
        return

    # Trouve le meilleur endroit pour "décaler" le tableau
    temp = []
    total = 0
    for x in A:
        if x == 90:
            total += 1
        else:
            total -= 1
        temp.append(total)
    min_temp = min(temp)
    slide = 0
    for i in range(len(temp)):
        if temp[i] == min_temp:
            slide = i + 1
            break
    A = A[slide:] + A[:slide]

    # On prépare les listes left_node et right_node
    left_node = []
    right_node = []
    for i in range(N):
        left_node.append(i - 1)
        right_node.append(i + 1)
    right_node[N - 1] = 0

    # On construit le tas des indices pour les 270
    import heapq
    R = []
    for i in range(N):
        if A[i] == 270:
            R.append(i)
    heapq.heapify(R)

    # Fonction récursive principale
    def F(left_node, right_node, R, depth):
        step = 1 << depth
        if len(R) == 0:
            n = []
            for i in range(len(left_node)):
                if left_node[i] is not None:
                    n.append(i)
            X = [None] * N
            Y = [None] * N
            X[n[0]] = step
            Y[n[0]] = 0
            X[n[1]] = step
            Y[n[1]] = step
            X[n[2]] = 0
            Y[n[2]] = step
            X[n[3]] = 0
            Y[n[3]] = 0
            return X, Y
        r = heapq.heappop(R)
        l = left_node[r]
        ll = left_node[l]
        rr = right_node[r]
        left_node[rr] = ll
        right_node[ll] = rr
        left_node[l] = None
        left_node[r] = None
        right_node[l] = None
        right_node[r] = None
        X, Y = F(left_node, right_node, R, depth + 1)

        dx = X[rr] - X[ll]
        dy = Y[rr] - Y[ll]
        if dx > 0:
            Y[rr] += step
            X[l] = X[rr] - step
            Y[l] = Y[ll]
            X[r] = X[l]
            Y[r] = Y[rr]
        elif dx < 0:
            Y[rr] -= step
            X[l] = X[rr] + step
            Y[l] = Y[ll]
            X[r] = X[l]
            Y[r] = Y[rr]
        elif dy > 0:
            X[rr] -= step
            X[l] = X[ll]
            Y[l] = Y[rr] - step
            X[r] = X[rr]
            Y[r] = Y[l]
        elif dy < 0:
            X[rr] += step
            X[l] = X[ll]
            Y[l] = Y[rr] + step
            X[r] = X[rr]
            Y[r] = Y[l]
        return X, Y

    X, Y = F(list(left_node), list(right_node), R, 0)

    # Remet dans l'ordre initial
    X = X[N-slide:] + X[:N-slide]
    Y = Y[N-slide:] + Y[:N-slide]

    # Attribution des indices pour compresser les coordonnées
    pos_x = {}
    pos_y = {}
    for x in sorted(set(X)):
        if x not in pos_x:
            pos_x[x] = len(pos_x)
    for y in sorted(set(Y)):
        if y not in pos_y:
            pos_y[y] = len(pos_y)
    X = [pos_x[x] for x in X]
    Y = [pos_y[y] for y in Y]

    for i in range(N):
        print(X[i], Y[i])

if __name__ == "__main__":
    main()