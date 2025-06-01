e = list(map(int, input().split()))
e.sort()
print("yes" if e[0] == e[1] and e[2] == e[3] else "no")