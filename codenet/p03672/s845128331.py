import sys
input = sys.stdin.readline

S = list(input().rstrip())
if len(S) % 2 == 0:
    S.pop()
    S.pop()
else:
    S.pop()
m = len(S) // 2
if S[:m] == S[m:]:
    print(len(S))
    sys.exit()
for i in range(len(S) // 2):
    S.pop()
    S.pop()
    m = len(S) // 2
    if S[:m] == S[m:]:
        print(len(S))
        sys.exit()