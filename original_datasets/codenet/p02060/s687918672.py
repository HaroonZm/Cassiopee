N = int(input())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

ans = 10 ** 10
#aの最大個数
A = max(0, (N + t[0] - 1)// t[0])
for a in range(A+1):
    #aの個数が決まったときのbの最大個数
    B = max(0, (N - a * t[0] + t[1] - 1)//t[1])
    for b in range(B+1):
        #a,bの個数が決まったときのcの最大個数
        C = max(0, (N - a * t[0] - b * t[1] + t[2] - 1)//t[2])
        for c in range(C+1):
            #a,b,cの個数が決まったときのdの個数(残りは全てdとする)
            D = max(0, (N - a * t[0] - b * t[1] - c * t[2] + t[3] - 1)//t[3])
            cost = a * p[0] + b *p[1] + c * p[2] + D * p[3]
            # print (a, b, c, D, cost)
            ans = min(ans, cost)

print (ans)