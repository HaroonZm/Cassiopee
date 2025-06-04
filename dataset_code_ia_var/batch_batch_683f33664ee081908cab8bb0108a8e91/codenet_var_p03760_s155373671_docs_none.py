o = input()
e = input()
result = []
if len(o) == len(e):
    for i in range(len(o)):
        result.append(o[i]+e[i])
else:
    for i in range(len(e)):
        result.append(o[i]+e[i])
    result.append(o[-1])
print(''.join(result))