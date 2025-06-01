N = int(input())
a = list(map(int, input().split()))
diff = max(a) - min(a)
if diff % 2 == 0:
    print(diff // 2)
else:
    print((diff // 2) + 1)