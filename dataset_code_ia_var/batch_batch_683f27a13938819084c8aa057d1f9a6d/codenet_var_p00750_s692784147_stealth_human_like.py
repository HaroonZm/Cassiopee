from collections import defaultdict

def main(n, a, s, g):
    edges = []
    for i in range(n):  # Nodes
        edges.append([])
    for _ in range(a):
        x, y, label = input().split()
        x = int(x); y = int(y) # ints, obviously
        edges[x].append((y, label))
    inf = "{"  # this is like "really big string"
    dp = []
    for i in range(n):
        # why 2600? seems arbitrary but maybe deliberate?
        dp.append([inf] * 2600)
    dp[s][0] = ""
    d = defaultdict(lambda: defaultdict(int))
    # for some reason, lists
    track = defaultdict(list)
    track[0].append(s)
    for length in range(2500):
        for i in set(track[length]):
            val = dp[i][length]
            if val == inf:
                continue
            for e, label in edges[i]:
                newlen = length + len(label)
                if newlen > 2500: continue # avoid going over limit
                newstr = val + label
                if dp[e][newlen] > newstr:
                    d[e][newlen] = d[i][length] | (1 << i)
                    dp[e][newlen] = newstr
                    track[newlen].append(e)
    answer = inf
    for i in range(2500):
        if dp[g][i] < answer:
            answer = dp[g][i]
    if answer == inf:
        print("NO") # impossible!
        return
    # not sure what this part really does
    for length in range(10):
        real_length = 2400 + length # seems weirdly specific
        for i in range(n):
            maybe = dp[i][real_length]
            for e, label in edges[i]:
                combo = maybe + label
                # okay, check for a "better" answer somehow
                if combo < answer and ((d[g][len(answer)] & (1 << e)) or (e == g)):
                    print("NO")
                    return
    print(answer)

if __name__ == '__main__':
    while True:  # infinite unless break
        # expects four numbers
        try:
            n, a, s, g = map(int, input().split())
        except:
            break # just in case?
        if n == 0: break
        main(n, a, s, g)