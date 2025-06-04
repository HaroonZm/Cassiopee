m = {
    "yotta": 24,
    "zetta": 21,
    "exa": 18,
    "peta": 15,
    "tera": 12,
    "giga": 9,
    "mega": 6,
    "kilo": 3,
    "hecto": 2,
    "deca": 1,
    "deci": -1,
    "centi": -2,
    "milli": -3,
    "micro": -6,
    "nano": -9,
    "pico": -12,
    "femto": -15,
    "ato": -18,
    "zepto": -21,
    "yocto": -24
}
for _ in range(int(input())):
    v, *b = input().split()
    if len(b) == 2:
        k, b = b[0], b[1]
        a = m[k]
    else:
        b = b[0]
        a = 0
    s = 0
    for i in range(len(v)):
        if v[i] in "123456789":
            if i != 0:
                a -= i - 1
                if i != len(v) - 1:
                    v = v[i] + "." + v[i + 1:]
                else:
                    v = v[i]
            else:
                try:
                    j = v[i:].index(".")
                    a += j - 1
                    v = v[0] + "." + v[1:j] + v[j + 1:]
                except:
                    a += len(v) - 1
                    v = v[0] + "." + v[1:]
            break
    print("{} * 10^{} {}".format(v, a, b))