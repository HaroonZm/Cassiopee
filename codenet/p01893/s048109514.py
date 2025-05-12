from operator import itemgetter
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt_a = 0
cnt_b = 0
for i, (a, b) in enumerate(zip(A, B)):
    cnt_a += i*a
    cnt_b += i*b

if cnt_a!=cnt_b or not sum(A)==sum(B)==N:
    print("NO")
    exit()

B_ = []
cumi = 0
for i, b in enumerate(B):
    for j in range(b):
        B_.append([cumi, i])
        cumi += 1
B_.sort(key=itemgetter(1), reverse=True)

Ans = [[0]*N for _ in range(N)]
cumi = 0
for i, a in enumerate(A[1:], 1):
    if len(B_) < i:
        print("NO")
        exit()
    for k in range(a):
        for j in range(i):
            B_[j][1] -= 1
            if B_[j][1] < 0:
                print("NO")
                exit()
            Ans[B_[j][0]][cumi] = 1
        cumi += 1
        B_.sort(key=itemgetter(1), reverse=True)
print("YES")
for ans in Ans:
    print(*ans)