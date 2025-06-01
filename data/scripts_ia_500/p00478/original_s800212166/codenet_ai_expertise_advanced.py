from collections import deque

x = input()
n = int(input())
length = len(x)
ans = sum(
    x in ''.join(deque(input(), maxlen=length-1) | deque(input()[:length-1]))
    for _ in range(n)
)
print(ans)