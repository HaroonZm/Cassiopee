import sys
input = sys.stdin.readline

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    segments = [tuple(map(int, input().split())) for _ in range(N)]
    segments.sort(key=lambda x: x[1], reverse=True)

    total_cost = 0
    expected_attacks = 0
    for D, P in segments:
        cost = D
        if total_cost + cost <= M:
            total_cost += cost
        else:
            remain = M - total_cost
            protected = remain
            unprotected = D - protected
            expected_attacks += unprotected * P
            total_cost = M
        if total_cost == M and segments[-1] != (D, P):
            # remaining segments unprotected
            ind = segments.index((D, P))
            for rest_D, rest_P in segments[ind + 1:]:
                expected_attacks += rest_D * rest_P
            break
    else:
        # all protected or cost allows some protection in last segment
        if total_cost < M:
            expected_attacks += 0
        elif total_cost == M:
            pass
        else:
            pass
    print(int(expected_attacks))