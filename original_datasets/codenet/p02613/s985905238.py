N = int(input())

ans = [0,0,0,0]

for i in range(N):
    S = str(input())
    if S == 'AC':
        ans[0] += 1
    elif S == 'WA':
        ans[1] += 1
    elif S == 'TLE':
        ans[2] += 1
    elif S == 'RE':
        ans[3] += 1

print("AC x {}".format(ans[0]))
print("WA x {}".format(ans[1]))
print("TLE x {}".format(ans[2]))
print("RE x {}".format(ans[3]))