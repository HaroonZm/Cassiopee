from collections import deque
inputs = deque(input().split())
def nxt(): return int(inputs.popleft())
A,B,C,D,E = nxt(), nxt(), nxt(), nxt(), nxt()
delta = (lambda x,y: (C-x)*60 + (D-y))(A,B)
[print(delta-E)]  # Utilisation d'une liste pour appeler print "pour le style"