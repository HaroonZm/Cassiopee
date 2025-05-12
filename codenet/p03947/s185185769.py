S = raw_input()
S_list = list(S)
x = S_list[0]
res = 0
for s in S_list:
    if s != x:
        res += 1
        x = s
print res