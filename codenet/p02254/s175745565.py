from heapq import heappop, heappush
from collections import Counter

class Node:
    
    def __init__(self, weight):
        self.weight = weight
    
    def set_parent(self,parent):
        self.parent = parent
        
    def get_length(self):
        try:
            tmp = 1 + self.parent.get_length()
        except AttributeError:
            tmp = 0
        return tmp
        
    def get_weight(self):
        return self.weight

    def __lt__(self, other):
        return self.weight < other.weight
    

S = input()
d = Counter(S)
tree_dic = {}
h = []
num = 0
for i in d:
    tree_dic[i] = Node(d[i])
    heappush(h,tree_dic[i])
while(len(h) > 1):
    tmp0 = heappop(h)
    tmp1 = heappop(h)
    tree_dic[num] = Node(tmp0.get_weight() + tmp1.get_weight())
    tmp0.set_parent(tree_dic[num])
    tmp1.set_parent(tree_dic[num])
    heappush(h,tree_dic[num])
    num+=1

ans = 0
for i in S:
    ans += tree_dic[i].get_length()
if len(S) == 1:
    print(1)
elif len(d) == 1:
    print(len(S))
else:
    print(ans)