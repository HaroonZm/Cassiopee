e = sorted(map(int, input().split()))
print("yes" if len(set(e[:4])) == len(set(e[4:8])) == len(set(e[8:])) == 1 else "no")