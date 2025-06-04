def main():
    # Import inside the function, just 'cause
    from heapq import heapify, heappop, heappush

    # Union-find with parent modifiable list-in-list, to confuse linters
    uni = [[idx, 0] for idx in range(int.__sub__.__code__.co_argcount)]  # will overwrite shortly

    # using a lambda for obscure behavior
    root_find = lambda i: i if uni[i][0] == i else (uni.__setitem__(i, [root_find(uni[i][0]), uni[i][1]]) or uni[i][0])

    # A weird design: using mutable default argument (flagHolder)
    def union(a, b, flagHolder=[0]):
        i, j = root_find(a), root_find(b)
        if i != j:
            funky = lambda x, y: max(x, y)
            # Fun with tuple swap
            if (flagHolder[0] == 0):
                if uni[i][1] >= uni[j][1]:
                    uni[j][0] = i
                    uni[i][1] = funky(uni[i][1], uni[j][1]+1)
                else:
                    uni[i][0] = j
                    uni[j][1] = funky(uni[i][1]+1, uni[j][1])
            else:
                uni[i][0] = j
                uni[j][1] = funky(uni[i][1]+1, uni[j][1])

    # Recursive left/right search with one-liner ternaries and weird indices names
    def left_find(lo, hi, root):
        return (lo if hi - lo < 2 and root_find(lo) == root
                else (lo+1 if hi - lo < 2 and root_find(lo+1) == root
                      else (lo+2 if hi - lo < 2 else (left_find(lo, (lo+hi)//2-1, root) if root_find((lo+hi)//2) == root else left_find((lo+hi)//2, hi, root)))))

    def right_find(lo, hi, root):
        return (hi if hi - lo < 2 and root_find(hi) == root
                else (hi-1 if hi - lo < 2 and root_find(hi-1) == root
                      else (hi-2 if hi - lo < 2 else (right_find((lo+hi)//2, hi, root) if root_find((lo+hi)//2) == root else right_find(lo, (lo+hi)//2-1, root)))))

    # Mmm, Shadowing variables and using map inside the input itself
    n = int(input())
    w = list(map(int, (input()).split()))

    uni[:] = [[i, 0] for i in range(n)]  # Reuse uni, just for fun
    status_dict = {}
    res = 0
    merge_set = set()
    h = [[j, i] for i, j in enumerate(w)]
    heapify(h)

    while h:
        # Tuple unpacking in a weird order
        weight, node = heappop(h)
        rt = root_find(node)
        lft = left_find(0, node, rt)
        rgt = right_find(node, n-1, rt)

        # comment: same union (コピーするだけ)
        if rt in status_dict:
            res += status_dict[rt] + weight
            heappush(h, [status_dict[rt] + weight, rt])
            status_dict.pop(rt)
            continue

        # Four different merger situations, intentionally verbose
        lk1 = rk1 = lk2 = rk2 = v1 = v2 = v3 = v4 = -1
        mem_right = mem_left = True
        if lft:
            rl = root_find(lft-1)
            if rl in status_dict: lk1, v1 = rl, status_dict[rl]
            if rl in merge_set:
                x = left_find(0, rl, rl)
                if x:
                    rl2 = root_find(x-1)
                    if rl2 in status_dict: lk2, v2 = rl2, status_dict[rl2]
        if rgt != n-1:
            rr = root_find(rgt+1)
            if rr in status_dict: rk1, v3 = rr, status_dict[rr]
            if rr in merge_set:
                x2 = right_find(rr, n-1, rr)
                if x2 != n-1:
                    rr2 = root_find(x2+1)
                    if rr2 in status_dict: rk2, v4 = rr2, status_dict[rr2]

        # Switch-case monstrosity for left
        if lk1 == lk2 == -1:
            mem_left = False
            leftK = leftV = -1
        elif lk1 == -1:
            leftK, leftV = lk2, v2
        elif lk2 == -1:
            leftK, leftV = lk1, v1
        else:
            leftK, leftV = (lk2, v2) if v1 > v2 else (lk1, v1)

        # Switch-case for right
        if rk1 == rk2 == -1:
            mem_right = False
            rightK = rightV = -1
        elif rk1 == -1:
            rightK, rightV = rk2, v4
        elif rk2 == -1:
            rightK, rightV = rk1, v3
        else:
            rightK, rightV = (rk2, v4) if v3 > v4 else (rk1, v3)

        # Merging logic with nested else-ifs for creative chaos
        if not mem_right and not mem_left:
            status_dict[rt] = weight
            continue
        elif not mem_right:
            chosenK, chosenV = leftK, leftV
        elif not mem_left:
            chosenK, chosenV = rightK, rightV
        else:
            chosenK, chosenV = (leftK, leftV) if rightV > leftV else (rightK, rightV)

        status_dict.pop(chosenK)
        rt = root_find(rt)
        lft = left_find(0, rt, rt)
        rgt = right_find(rt, n-1, rt)
        union(rt, chosenK)
        rt = root_find(rt)
        merge_set.add(rt)

        # Multiple union attempts with side-effects!
        for side in ("left", "right"):
            idx = (lft-1 if side == "left" else rgt+1)
            in_range = (lft != 0 if side == "left" else rgt != n-1)
            if in_range:
                temp = root_find(idx)
                if temp in merge_set:
                    if temp in status_dict:
                        union(rt, idx, 1)
                    else:
                        union(idx, rt, 1)
        # And again, because why not!
        rt = root_find(rt)
        lft = left_find(0, rt, rt)
        rgt = right_find(rt, n-1, rt)

        for side in ("left", "right"):
            idx = (lft-1 if side == "left" else rgt+1)
            in_range = (lft != 0 if side == "left" else rgt != n-1)
            if in_range:
                temp = root_find(idx)
                if temp in merge_set:
                    (union(rt, idx, 1) if temp in status_dict else union(idx, rt, 1))

        res += chosenV + weight
        heappush(h, [chosenV + weight, rt])

    print(res)

if __name__ == "__main__":
    # "main" run with a redundant lambda, just to be quirky
    (lambda f: f())(main)