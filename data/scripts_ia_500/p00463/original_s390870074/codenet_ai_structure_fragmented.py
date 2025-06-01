def lire_entiers():
    return map(int, input().split())

def lire_pt():
    return int(input())

def lire_bar():
    return list(map(int, input().split()))

def initialiser_nos(n):
    return [i for i in range(n)]

def trier_bars(bars):
    bars.sort(key=lambda x: x[1])

def creer_barspt_et_permuter(nos, bars):
    barspt = []
    for bar in bars:
        b = bar[0] - 1
        barspt.append([nos[b], nos[b+1], 0, 0])
        nos[b], nos[b+1] = nos[b+1], nos[b]
    return barspt

def mise_a_jour_barspt_pts(nos, bars, barspt, pts):
    for barid in range(len(bars) - 1, -1, -1):
        b0 = bars[barid][0] - 1
        b1 = bars[barid][0]
        barspt[barid][2] = pts[nos[b0]]
        barspt[barid][3] = pts[nos[b1]]
        pts[nos[b0]], pts[nos[b1]] = pts[nos[b1]], pts[nos[b0]]

def calculer_minsc(pts, k):
    return sum(pts[0:k])

def calculer_hosei(atari, k, barspt):
    hosei = 0
    for bar in barspt:
        if atari <= bar[0] - 1 < atari + k and (bar[1] - 1 < atari or atari + k <= bar[1] - 1):
            sc = bar[2] - bar[3]
            if sc < hosei:
                hosei = sc
        if atari <= bar[1] - 1 < atari + k and (bar[0] - 1 < atari or atari + k <= bar[0] - 1):
            sc = bar[3] - bar[2]
            if sc < hosei:
                hosei = sc
    return hosei

def main():
    while True:
        n,m,h,k = lire_entiers()
        if n == 0:
            break
        pts = [lire_pt() for _ in range(n)]
        bars = [lire_bar() for _ in range(m)]
        trier_bars(bars)
        nos = initialiser_nos(n)
        barspt = creer_barspt_et_permuter(nos, bars)
        nos = initialiser_nos(n)
        mise_a_jour_barspt_pts(nos, bars, barspt, pts)
        atari = -1
        minsc = calculer_minsc(pts, k)
        hosei = calculer_hosei(atari, k, barspt)
        print(minsc + hosei)

main()