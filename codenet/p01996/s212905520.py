N, M = (int(x) for x in input().split())
A = (int(x) for x in input().split())

print(M - len([x for x in A if x <= M]))