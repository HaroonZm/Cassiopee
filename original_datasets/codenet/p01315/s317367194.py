while True:
    N = int(input())
    if N == 0:
        break
    
    data = []
    for _ in range(N):
        inp = input().split()
        P, A, B, C, D, E, F, S, M = map(int, inp[1:])
        time = A + B + C + M * (D + E)
        money = M * F * S - P

        da = [inp[0], money/time]
        data.append(da)

    data.sort(key=lambda x:x[0])
    data.sort(key=lambda x:-x[1])
    for i in range(N):
        print(data[i][0])
    print('#')