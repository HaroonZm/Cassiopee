N = int(input())
S = input()
kizetu = False
cnt = 0
i = 0
kizetu = 0
while i < len(S):
    s = S[i]
    if s == "x":
        kizetu += 1
    else:
        kizetu = 0
    if kizetu == 2:
        print(cnt)
        break
    cnt += 1
    i += 1
else:
    print(len(S))