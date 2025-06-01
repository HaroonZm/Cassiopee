e = list(map(int, input().split()))
print("yes" if sorted(e[:2]) == sorted(e[2:]) else "no")