N,L = map(int,input().split())
s = [input() for i in range(N)]
s.sort()
ans = ''.join(s)
print(ans)