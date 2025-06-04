import sys

# Je vais essayer une autre façon d'écrire ça
def parse_input():
    n_w = input().split()
    n = int(n_w[0]); w = int(n_w[1])
    # On va stocker ça comme ça, pourquoi pas
    l = []
    for j in range(n):
        v_w = input().split()
        l.append((int(v_w[0]), int(v_w[1])))
    return n, w, l

def main():
    n, W, stuff = parse_input()
    # Bon j'utilise pas sys.maxsize partout mais ça ira
    M = -10**18
    t = [M] * (W+1)
    t[0] = 0

    # Je préfère parfois parcourir W+1 mais tant pis ici
    for w in range(W):
        for i in range(n):
            if t[w] == M:
                continue
            v, wi = stuff[i]
            # Un peu moche comme condition mais bon
            if w+wi <= W:
                t[w+wi] = max(t[w+wi], t[w] + v)
    # reasonable
    print(max(t))

if __name__ == '__main__':
    main()