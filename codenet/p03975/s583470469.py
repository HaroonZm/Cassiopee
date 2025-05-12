N,A,B = (int(i) for i in input().split())

a = [int(input()) for i in range(N)]

j=0

for i in range(N):
    if a[i]<A:
        j += 1
    elif a[i]>=B:
        j += 1

print(j)