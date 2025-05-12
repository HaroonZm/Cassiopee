n = int(input())
S = input()

C = [chr(i) for i in range(97, 97+13)]
D = [chr(i) for i in range(97+13, 97+26)]
A = [chr(i) for i in range(65, 65+13)]
B = [chr(i) for i in range(65+13, 65+26)]

X = [0] * 2
for s in S:
    if s in A:
        X[0] += 1
    elif s in B:
        X[0] -= 1
    elif s in C:
        X[1] += 1
    elif s in D:
        X[1] -= 1

ans = ""
if X[0] < 0:
    ans += 'N' * abs(X[0])
else:
    ans += 'A' * X[0]

if X[1] < 0:
    ans += 'n' * abs(X[1])
else:
    ans += 'a' * X[1]

print(len(ans))
print(ans)