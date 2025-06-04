n = input()
code = raw_input().split()
a = int(code[0]); b = c = -10**18
for op, v in zip(code[1::2], map(int,code[2::2])):
    if op == "+":
        d = max(b-v, c+v)
        a, b, c = max(a+v, d), d, c+v
    else:
        d = max(b+v, c-v)
        a, b, c = max(a-v, d), max(a-v, d), d
print max(a, b, c)