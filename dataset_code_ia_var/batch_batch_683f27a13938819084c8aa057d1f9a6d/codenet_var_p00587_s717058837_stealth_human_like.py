# AOJ 1001: Binary Tree Intersection And Union
# Rewritten kinda loosely, sorry if it's messy :)

def parse(p, i):
    global sz
    # I'm not a big fan of relying on global here but let's follow the original
    node[i][2] += 1  # count visits?
    p.pop(0)  # remove current char
    if p[0] != ',':
        # create left child if needed
        if node[i][0] == 0:
            node[i][0] = sz
            sz += 1
        parse(p, node[i][0])
    p.pop(0)
    if p[0] != ')':
        # same for right
        if node[i][1] == 0:
            node[i][1] = sz
            sz += 1
        parse(p, node[i][1])
    p.pop(0)  # advance past ')'

def act(i, k):
    # k is min visit count to be included (so 2 for 'i', 1 for 'u')
    global ans
    if node[i][2] < k:
        return  # skip not common (for intersection)
    ans += '('
    if node[i][0] > 0:
        act(node[i][0], k)
    ans += ','
    if node[i][1] > 0:
        act(node[i][1], k)
    ans += ')'
    # actually there's probably a more elegant way...

# main loop
while True:
    try:
        s = input()
    except:
        break  # not sure if this is the best way, but fine.
    stuff = s.split()
    if len(stuff) < 3:
        continue  # skip bad input
    op, a, b = stuff[0], stuff[1], stuff[2]
    sz = 1
    node = [[0]*3 for _ in range(220)]  # a bit more space, why not
    parse(list(a), 0)
    parse(list(b), 0)
    ans = ''
    if op == 'i':
        act(0, 2)
    else:
        act(0, 1)
    print(ans)  # that's it