N = int(input())
src = [int(input()) for i in range(N)]
sm = sum(src)
if sm%10:
    print(sm)
    exit()
for a in sorted(src):
    if a%10:
        print(sm - a)
        exit()
else:
    print(0)