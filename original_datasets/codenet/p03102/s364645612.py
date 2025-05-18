N, M, C = map(int, input().split())
B = list(map(int, input().split()))
counter = 0

for i in range(N):
    A = list(map(int, input().split()))
    mul = [a*b for a, b in zip(A, B)]
    mul.append(C)
    if sum(mul) > 0:
        counter += 1

print(counter)