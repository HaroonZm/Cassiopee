h1_h2 = raw_input().split()
h1 = int(h1_h2[0])
h2 = int(h1_h2[1])

k1_k2 = raw_input().split()
k1 = int(k1_k2[0])
k2 = int(k1_k2[1])

abcd = raw_input().split()
a = int(abcd[0])
b = int(abcd[1])
c = int(abcd[2])
d = int(abcd[3])

def calc(p, q):
    return p * a + p // 10 * c + q * b + q // 20 * d

v1 = calc(h1, h2)
v2 = calc(k1, k2)

if v1 > v2:
    print "hiroshi"
elif v1 == v2:
    print "even"
else:
    print "kenjiro"