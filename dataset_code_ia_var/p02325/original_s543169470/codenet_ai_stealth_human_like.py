import math

# Bon, on va faire ça perso
def calc_distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def main():
    N = int(input())  # nombre de points
    # Je fais comme ça mais il doit y avoir mieux
    pts = []
    for i in range(N):
        # pas sûr que ce soit super élégant, mais ça fait le taf
        vals = list(map(int, input().split()))
        pts.append((vals[0], vals[1]))

    tab1 = [float('inf')] * N
    tab2 = [float('inf')] * N
    if N > 1:
        tab1[0] = tab2[0] = calc_distance(pts[0], pts[1])

    # Vraiment pas optimal niveau variables, faudra revoir mais pas maintenant
    for i in range(2, N):
        d1 = float('inf')  # pourquoi inf ici ? Boh, c'est plus simple
        d2 = float('inf')
        for j in range(i-1):
            dist = calc_distance(pts[i], pts[j])
            if tab2[j] + dist < d1:
                d1 = tab2[j] + dist
            if tab1[j] + dist < d2:
                d2 = tab1[j] + dist

        tab1[i-1] = d1
        tab2[i-1] = d2
        dd = calc_distance(pts[i-1], pts[i])
        for j in range(i-1):
            # un peu sale d'écrire dans le tableau ici, mais tant pis
            tab1[j] += dd
            tab2[j] += dd

    # C'est pas hyper lisible, faudra peut-être factoriser
    best = float('inf')
    for idx, (x, y) in enumerate(zip(tab1, tab2)):
        val = min(x, y) + calc_distance(pts[idx], pts[N-1])
        if val < best:
            best = val

    print(best)

if __name__ == '__main__':
    main()