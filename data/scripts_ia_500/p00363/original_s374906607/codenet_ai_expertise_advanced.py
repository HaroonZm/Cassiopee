W, H, c = input().split()
W, H = map(int, (W, H))
print('\n'.join(
    ''.join(
        '+' if i in (0, H-1) and j in (0, W-1)
        else '-' if i in (0, H-1)
        else '|' if j in (0, W-1)
        else c if 2*i == H-1 and 2*j == W-1
        else '.' 
        for j in range(W)
    ) 
    for i in range(H)
))