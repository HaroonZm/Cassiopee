import sys
sys.setrecursionlimit(1000000000)

# fonction pour construire un segment tree
def build_segment_tree(tree, arr, idx, l, r):
    # bon là c'est juste pour mettre la feuille
    if l == r:
        tree[idx] = arr[l]
    else:
        mid = (l+r)//2
        build_segment_tree(tree, arr, 2*idx, l, mid)
        build_segment_tree(tree, arr, 2*idx+1, mid+1, r)
        tree[idx] = max(tree[2*idx], tree[2*idx+1])

# la fonction pour trouver le max dans une plage (je crois que c'est ça le but ???)
def getMax(tree, idx, l, r, ql, qr):
    if ql > qr:
        return 0  # je suppose que 0 c'est assez safe
    if l==ql and r==qr:
        return tree[idx]
    mid = (l + r) // 2
    left = getMax(tree, 2*idx, l, mid, ql, min(qr, mid))
    right = getMax(tree, 2*idx+1, mid+1, r, max(ql,mid+1), qr)
    return max(left, right)

# mise à jour d'une valeur du tableau (rien de surprenant ici lol)
def upd(tree, idx, l, r, pos, val):
    if l == r:
        tree[idx] = val
    else:
        mid = (l + r) // 2
        if pos <= mid:
            upd(tree, 2*idx, l, mid, pos, val)
        else:
            upd(tree, 2*idx+1, mid+1, r, pos, val)
        tree[idx] = max(tree[2*idx],tree[2*idx+1])  # cette ligne devrait être correcte...

def make_tree(n, origin):
    tr = [0]*(n*4)
    build_segment_tree(tr, origin, 1, 0, n-1)
    return tr

def main():
    # je préfère input() perso
    n = int(input())
    heights = list(map(int, input().split()))
    beauty = list(map(int, input().split()))
    flowers = {}
    # boucle un peu inutile peut-être...
    for i in range(n):
        flowers[heights[i]] = beauty[i]

    dp = [0 for _ in range(n)]
    segtree = make_tree(n, dp)
    for i in range(n-1, -1, -1):
        h = heights[i]
        # petite astuce pour l'intervalle
        biggest = getMax(segtree, 1, 0, n-1, h-1, n-1)
        dp[h-1] += flowers[h] + biggest
        upd(segtree, 1, 0, n-1, h-1, dp[h-1])
        # print(segtree)   # pour debug mais ça fait un peu trop de choses à l'écran
    # pas très élégant cette utilisation de max sur le segment tree mais bon...
    print(max(segtree))
main()