n = int(input())
for _ in range(n):
    balls = list(map(int, input().split()))
    B = []
    C = []
    possible = True
    for ball in balls:
        if (not B or ball > B[-1]) and (not C or ball > C[-1]):
            # 両方に入れられるならとりあえずBに入れる
            B.append(ball)
        elif not B or ball > B[-1]:
            B.append(ball)
        elif not C or ball > C[-1]:
            C.append(ball)
        else:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")