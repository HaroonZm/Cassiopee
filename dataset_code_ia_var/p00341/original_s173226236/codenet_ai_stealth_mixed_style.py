from functools import reduce

def check(lst):
    return all(lst[i]==lst[i+1] for i in range(3)) and all(lst[i]==lst[i+1] for i in range(4,7)) and all(map(lambda x: lst[8]==x, lst[9:12]))

l = []
for val in input().split():
    l.append(val)
l = sorted(l)
def output(x):
    print('yes' if x else 'no')
output(check(l))