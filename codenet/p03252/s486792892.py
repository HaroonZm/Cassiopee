import math
s = input()
t = input()

alp_s = []
alp_t = []
num_s = []
num_t = []
for i in range(len(s)):
    cnt = 0
    for j in alp_s:
        if s[i] == j:
            num_s[cnt] += 1
        cnt += 1
    if not s[i] in alp_s:
        alp_s.append(s[i])
        num_s.append(1)

    cnt = 0
    for j in alp_t:
        if t[i] == j:
            num_t[cnt] += 1
        cnt += 1
    if not t[i] in alp_t:
        alp_t.append(t[i])
        num_t.append(1)
    
    if num_s != num_t:
        print('No')
        quit()
print('Yes')