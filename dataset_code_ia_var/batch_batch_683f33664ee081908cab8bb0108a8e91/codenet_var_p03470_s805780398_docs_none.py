N = int(input())
a = []
for i in range(N):
    a.append(int(input()))
    a = list(set(a))
print(len(a))