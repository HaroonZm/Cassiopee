S = input()
dict_string = {}
dict_depth = {}

i = 0
while i < len(S):
    s = S[i]
    if s in dict_string:
        dict_string[s] += 1
    else:
        dict_string[s] = 1
        dict_depth[s] = 0
    i += 1

dict_string_calc = {}
for k in dict_string:
    dict_string_calc[k] = dict_string[k]

while True:
    if len(dict_string_calc) == 1:
        break
    pairs = []
    for k in dict_string_calc:
        pairs.append((dict_string_calc[k], k))
    pairs.sort()
    x_cnt, x = pairs[0]
    y_cnt, y = pairs[1]
    j = 0
    while j < len(x + y):
        s2 = (x + y)[j]
        if s2 in dict_depth:
            dict_depth[s2] += 1
        else:
            raise Exception
        j += 1
    del dict_string_calc[x]
    del dict_string_calc[y]
    dict_string_calc[x + y] = x_cnt + y_cnt

ans = 0
for k in dict_depth:
    ans += dict_string[k] * dict_depth[k]

if len(dict_string) == 1:
    ans = len(S)
print(ans)