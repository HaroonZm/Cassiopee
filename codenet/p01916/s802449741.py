S = input()
dict = {}
for i in range(len(S)):
    if(S[i] in dict):
        dict[S[i]] += 1
    else:
        dict[S[i]] = 1
l = list(dict.values())
cnt = 0
for i in range(len(l)):
    if(l[i] % 2 != 0):
        cnt += 1
print(cnt // 2)