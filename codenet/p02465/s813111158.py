input()
s1 = set(map(int, input().split()))
input()
s2 = set(map(int, input().split()))

s = sorted(list(s1.difference(s2)))

if len(s) != 0:
    print('\n'.join(map(str, s)))