from functools import reduce
from itertools import combinations, takewhile, count, islice
from operator import or_

def add_edge(node, adj_lst, adj_rev, s1, s2):
    first_diff = next((i for i, (a, b) in enumerate(zip(s1, s2)) if a != b), None)
    if first_diff is None:
        return len(s1) > len(s2)
    idx1, idx2 = map(lambda c: ord(c) - ord("a"), (s1[first_diff], s2[first_diff]))
    map(lambda x: x.add(idx1), (node,)) or map(lambda x: x.add(idx2), (node,))
    list(map(lambda l: l[0].add(l[1]), [(adj_lst, idx1), (adj_rev, idx2)]))
    list(map(lambda l: l[0].add(l[1]), [(adj_lst, idx1), (adj_rev, idx2)]))
    adj_lst[idx1].add(idx2)
    adj_rev[idx2].add(idx1)
    return False

def main():
    list(map(lambda _: (
        lambda n, lst:
            (lambda node, adj_lst, adj_rev, blank_flag:
                (lambda pairs:
                    (lambda has_blank: (
                        lambda node_ixs:
                            (lambda visited, visit:
                                (lambda any_cycle: print("no") if any_cycle or has_blank else print("yes"))(
                                    reduce(or_, map(visit, node_ixs), False))
                            )(
                                [0] * 26,
                                (lambda f: (lambda x: f(f, x)))(
                                    lambda myself, n: True if visited[n] == 2 else False if visited[n] else
                                    (
                                        (lambda _:
                                            any(myself(myself, t) for t in adj_lst[n])
                                        )(setattr(visited, '__setitem__', lambda n, v=2: None)) or [setattr(visited, n, 1)][0]
                                    )
                                )
                            )
                        )(list(node))
                    )
                )(reduce(or_, (add_edge(node, adj_lst, adj_rev, i, j) for i, j in pairs), False))
                )(
                    set(),
                    [set() for _ in range(26)],
                    [set() for _ in range(26)],
                    False
                )
            )(
                list(combinations(lst, 2))
            )
        )
    )(int(input()), [input() for _ in range(int(input()))])
        if (lambda n: n > 0)(int(input()))
        else quit()
    ), iter(count(0))))

main()