import re
n = int(input())
inputs = []
for _ in range(n):
    s = input().replace(" ", "")
    inputs.append(s)
for s in inputs:
    t = ''.join([str(10000 + sum([eval(i[0] + '0' * 'ixcm'.find(i[1])) for i in ['1' + i for i in ''.join(re.split(r'\d\w', s))] + re.findall(r'\d\w', s)]))[i] + '1mcxi'[i] for i in range(5)])
    u = t.replace('1', '')
    v = re.sub(r'0.', '', u)
    print(v)