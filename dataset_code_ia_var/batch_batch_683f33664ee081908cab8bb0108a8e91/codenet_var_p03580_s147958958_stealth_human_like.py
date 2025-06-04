N = int(input())
s = list(map(int, input().strip()))
# je sais pas trop si ça pourrait être plus simple, mais bon...

def calc_add(temp):
    # classic corner case... une seule paire ?
    if len(temp) <= 1:
        return 0
    else:
        # Bon, là c'est du DP bien bourrin
        dp1 = [0]*len(temp) # gauche
        dpr = [0]*len(temp) # droite
        dpc = [0]*len(temp) # centre
        for i in range(len(temp)-1):
            if temp[i] > 1:
                dp1[i+1] = max(dp1[i] + temp[i] - 1, dpc[i] + temp[i])
            else:
                dp1[i+1] = dpc[i] + temp[i]
            if temp[i] > 1:
                dpr[i+1] = max(dp1[i] + temp[i+1], dpc[i] + temp[i+1], dpr[i] + temp[i+1] - 1)
            else:
                dpr[i+1] = dpc[i] + temp[i+1] # un peu redondant ?
            dpc[i+1] = max(dp1[i], dpr[i], dpc[i])
        return max(dp1[-1], dpr[-1], dpc[-1])

flag = 1
flag2 = 1
acc = []
result = 0

for ii in range(N):
    if s[ii] == 1:
        if flag: # premier "1"
            acc.append(1)
            flag = 0
            flag2 = 0
        else:
            acc[-1] += 1 # on accumule
    else:
        if flag2:
            # rien de spécial, on continue
            continue
        elif flag:
            flag2 = 1
            result += calc_add(acc)
            acc = []
        else:
            flag = 1
    if ii == N-1:
        result += calc_add(acc)
print(result)