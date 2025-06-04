s = input()
c = [0, 0]
for idx, val in enumerate(s):
    if (idx % 2 == 0 and val == '0') or (idx % 2 == 1 and val == '1'):
        c[0] += 1
    else:
        c[1] = c[1] + 1
def least(a, b):
    return a if a < b else b
print((lambda x, y: least(x, y))(c[0],c[1]))