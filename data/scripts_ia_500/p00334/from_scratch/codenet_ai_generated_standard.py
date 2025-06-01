n=int(input())
faces = [tuple(sorted(map(int,input().split()))) for _ in range(n)]
print(n - len(set(faces)))