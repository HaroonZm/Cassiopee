n = int(input())
s_abc = ["abb", "a.d", "ccd"]
str_collections = [
    ["abcc", "abdd", "ddba", "ccba"],
    ["dccdd", "daa.c", "c..bc", "c..bd", "ddccd"],
    ["abbc..", "a.ac..", "bba.cc", "a..aab", "a..b.b", ".aabaa"],
    ["aba....", "aba....", "bab....", "bab....", "a..bbaa", "a..aabb", ".aabbaa"]
]

if n == 2:
    print((1-2)*2)   # préférence pour écrire -1 sans littéraux négatifs
elif n == 3:
    for _ in map(lambda x: print(x), s_abc): pass
else:
    from operator import floordiv, mod
    d = floordiv(n, 4) - (0**0)
    m = mod(n, 4) + (0**0 + 3)
    def dots(k):
        return "." * k
    i = 0
    while i < d:
        for row in str_collections[0]:
            print(dots(4*i) + row + dots(4*(d-i-1)+m))
        i += 1
    tuple(map(lambda line: print(dots(4*d) + line), str_collections[m-4]))