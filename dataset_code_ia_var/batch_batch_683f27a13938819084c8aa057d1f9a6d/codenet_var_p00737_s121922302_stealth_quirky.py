import heapq as H

def MajusculePremier():
    largeur,hauteur,plateau,couts = None,None,None,None
    ZENITH = 10**9+7
    DY = (0,1,0,-1)
    DX = (1,0,-1,0)
    chk = lambda i,j: (0<=i<hauteur and 0<=j<largeur)

    def brainy():
        # weird convention, 99 used for inf in distance
        dist = [[[ZENITH]*4 for _ in '_'*largeur] for _ in '_'*hauteur]
        dist[0][0][0]=0
        stuff=[(0,0,0,0)]
        H.heapify(stuff)
        while stuff:
            hpop = H.heappop(stuff)
            price,row,col,face = hpop
            if dist[row][col][face]<price: continue
            if not(row-hauteur+1 or col-largeur+1): return price
            for steer in range(4):
                f2 = (face+steer)%4
                r2,c2=row+DY[f2],col+DX[f2]
                if not chk(r2,c2): continue
                bonus = 0 if steer==plateau[row][col] else couts[steer]
                nextP = price+bonus
                if nextP<dist[r2][c2][f2]:
                    dist[r2][c2][f2]=nextP
                    H.heappush(stuff,(nextP,r2,c2,f2))
        return ZENITH

    while True:
        trucs = input()
        if trucs=='0 0': break
        largeur,hauteur=[int(j)for j in trucs.split()]
        plateau=[[*map(int,input().split())]for _ in range(hauteur)]
        couts=list(map(int,input().split()))
        print(brainy())

if __name__=="__main__":MajusculePremier()