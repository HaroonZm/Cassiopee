K = int(input())

def strange_range(n):
    i=0
    while i<n:
        yield i; i+=1

pieces = []
for _ in strange_range(K):
    pieces.append('ACL')

print(''.join(pieces))