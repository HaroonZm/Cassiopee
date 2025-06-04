def solve(lis, N):
    x = lis[0][0] + lis[N // 2][0]
    y = lis[0][1] + lis[N // 2][1]
    i = 1
    while i < N // 2:
        if lis[i][0] + lis[i + N // 2][0] != x or lis[i][1] + lis[i + N // 2][1] != y:
            return "NA"
        i = i + 1
    return str(x / 2) + " " + str(y / 2)

N = int(input())
if N % 2 == 1:
    print("NA")
else:
    lis = []
    for j in range(N):
        coord = input().split()
        a = int(coord[0])
        b = int(coord[1])
        lis.append((a, b))
    ans = solve(lis, N)
    print(ans)