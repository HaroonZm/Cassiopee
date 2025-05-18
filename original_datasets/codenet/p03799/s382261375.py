S, c = map(int, raw_input().split())
if 2*S<c:
    print S + (c - 2*S)/4
else:
    print c/2