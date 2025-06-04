H_W = input().split()
H = int(H_W[0])
W = int(H_W[1])
factors = []
h1 = 1
while h1 < H:
    subHeight = H-h1
    h2 = subHeight//2
    h3 = subHeight-h2
    w2 = W//2
    w3 = W-w2
    s1_0 = h1*W
    s1_1 = h2*W
    s1_2 = h3*W
    s2_0 = h1*W
    s2_1 = subHeight*w2
    s2_2 = subHeight*w3
    max_s1 = max(s1_0, s1_1, s1_2)
    min_s1 = min(s1_0, s1_1, s1_2)
    diff1 = max_s1 - min_s1
    max_s2 = max(s2_0, s2_1, s2_2)
    min_s2 = min(s2_0, s2_1, s2_2)
    diff2 = max_s2 - min_s2
    factors.append(diff1)
    factors.append(diff2)
    h1 += 1
w1 = 1
while w1 < W:
    subWidth = W-w1
    w2 = subWidth//2
    w3 = subWidth-w2
    h2 = H//2
    h3 = H-h2
    s1_0 = H*w1
    s1_1 = H*w2
    s1_2 = H*w3
    s2_0 = H*w1
    s2_1 = h2*subWidth
    s2_2 = h3*subWidth
    max_s1 = max(s1_0, s1_1, s1_2)
    min_s1 = min(s1_0, s1_1, s1_2)
    diff1 = max_s1 - min_s1
    max_s2 = max(s2_0, s2_1, s2_2)
    min_s2 = min(s2_0, s2_1, s2_2)
    diff2 = max_s2 - min_s2
    factors.append(diff1)
    factors.append(diff2)
    w1 += 1
min_value = factors[0]
i = 1
while i < len(factors):
    if factors[i] < min_value:
        min_value = factors[i]
    i += 1
print(min_value)