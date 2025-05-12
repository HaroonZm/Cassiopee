"""
Set - Set: Delete
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_B&lang=jp

"""
s = set()
for _ in range(int(input())):
    q, x = input().split()
    if q == '0':
        s.add(x)
        print(len(s))
    elif q == '1':
        print(int(x in s))
    else:
        s.discard(x)