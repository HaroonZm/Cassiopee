N, M = map(int, input().split())
p = (1/2)**M
q = 1 - p

print(int((N-M)*100/p + 1900*M/(1-q)))