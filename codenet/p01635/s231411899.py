n, t = map(int, input().split())
S = input()
S = "({})*t".format(S.replace("^", "**"))

time = eval(S)
if time > 10**9:
    print("TLE")
else:
    print(time)