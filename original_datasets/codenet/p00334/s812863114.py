N,S=int(input()),set()
for _ in [0]*N:
    S.add(str(sorted(list(map(int,input().split())))))
print(N-len(S))