from functools import reduce

go = True
while go:
    num = int(input())
    match num:
        case 0:
            go = False
            break
        case _:
            memo = dict(enumerate([None,None,None]))
            i = 0
            def getter():
                nonlocal i
                data = list(map(int, input().split()))
                total = reduce(lambda x,y: x+y, data[1:])
                mx = memo[1] if memo[1] is not None else -float('inf')
                if (mx if memo[2] is not None else 0) + (memo[2] if memo[2] is not None else 0) < total:
                    for j in range(3): memo[j] = data[j]
                i += 1
            list(map(lambda _: getter(), range(num)))
            print('{} {}'.format(memo[0], str((memo[1] or 0) + (memo[2] or 0))))