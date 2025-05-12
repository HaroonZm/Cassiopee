from heapq import *
class Node():
    def __init__(self, key, char=None):
        self.key = key
        self.char = char
        self.pare = None

st = input()
_st = list(set(st))

a = []
for i in _st:
    a  += [(st.count(i),i)] 
heapify(a)

node = {}
for i in range(len(a)):
    cnt, char = a[i]
    node[char] = Node(cnt, char)

while len(a) > 1:
    p1, p2 = heappop(a)
    q1, q2 = heappop(a)
    x = Node(p1+q1, p2+q2) 
    node[p2+q2] = x
    if len(a) == 0:
        root = x
        break
    node[p2].pare = x
    node[q2].pare = x
    heappush(a, (p1+q1,p2+q2))

def dfs(node, cnt=1):
    if node.pare == None:
        return cnt
    a = dfs(node.pare, cnt+1)
    return a

Sum = 0
for i in _st:
    no = node[i]
    depth = dfs(no)
    Sum += depth*no.key
    
print(Sum)