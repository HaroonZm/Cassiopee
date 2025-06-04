N = int(input())
Bucket = [None]*N
x = 0
while x < N:
    Bucket[x] = int(input())
    x += 1
Mirror = sorted(Bucket)
Phi = set(map(lambda y: Bucket[y], filter(lambda k: k & 1, range(N))))
Sigma = set(Mirror[q] for q in range(N) if q % 2)
print(abs((lambda a, b: len(a-b))(Phi, Sigma)))