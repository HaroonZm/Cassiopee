def resolve():
    a, b, c = list(map(int, input().split()))
    if (b * 10 + c) % 4 == 0:
        print("YES")
    else:
        print("NO")

resolve()