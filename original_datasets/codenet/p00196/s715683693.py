while True:
    n = int(input())
    if n == 0: break
    result = [input().split() for _ in range(n)]
    result = [[r[0], r.count('0'), r.count('1')] for r in result]
    result.sort(key=lambda x: [-x[1], x[2]])
    result = [r[0] for r in result]
    print('\n'.join(result))