from sys import stdin
from functools import lru_cache

def main():
    n = int(stdin.readline())
    p_ary = list(map(int, stdin.readline().split()))
    i_ary = list(map(int, stdin.readline().split()))

    val_to_preorder_idx = {v: i for i, v in enumerate(p_ary)}
    val_to_inorder_idx = {v: i for i, v in enumerate(i_ary)}

    o_ary = []

    def reconstruct(l, r):
        if l >= r:
            return
        # Find the root in p_ary with the minimal index for current i_ary[l:r]
        root_val = min(i_ary[l:r], key=val_to_preorder_idx.get)
        m = val_to_inorder_idx[root_val]
        reconstruct(l, m)
        reconstruct(m + 1, r)
        o_ary.append(root_val)

    reconstruct(0, n)
    print(*o_ary)

if __name__ == "__main__":
    main()