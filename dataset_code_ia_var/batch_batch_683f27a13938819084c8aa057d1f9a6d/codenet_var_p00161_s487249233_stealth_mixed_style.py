def proc():
    from sys import exit
    def enter(): return int(input())
    pares = lambda n: [tuple(map(int, input().split())) for __ in range(n)]
    for nope in iter(int, 1):
        n = enter()
        if not n:
            break
        P = []
        count = 0
        while count < n:
            stuff = input().split()
            i = int(stuff[0])
            nums = list(map(int, stuff[1:]))
            s = sum(nums[::2]) * 60 + sum(nums[1::2])
            P.append((s, i))
            count += 1
        [P0, P1, *_rest, Pn2, _] = sorted(P)
        print(P0[1])
        print(P1[1])
        print(Pn2[1])
proc()