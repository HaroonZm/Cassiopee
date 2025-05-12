def solve():
    H,W = map(int,input().split())
    field = [list(map(int,input().split())) for _ in range(H)]

    nh = 0
    nw = 0
    ans = []
    haveCoin = False
    while True:

        if field[nh][nw] % 2 != 0:
            if haveCoin:
                haveCoin = False
            else:
                haveCoin = True
        
        frm = [nh+1,nw+1]

        if nh % 2 == 0:
            nw += 1
            if nw == W:
                nh += 1
                nw = W-1
        else:
            nw -= 1
            if nw == -1:
                nh += 1
                nw = 0
        
        to = [nh+1,nw+1]

        if nh == H:
            break
            
        if haveCoin:
            ans.append(frm+to)
    
    print(len(ans))
    for elem in ans:
        print(*elem)

if __name__ == '__main__':
    solve()