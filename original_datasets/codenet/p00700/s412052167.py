if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        maxDist = 0
        treasureX = 0
        treasureY = 0
        posX = 0
        posY = 0
        while True:
            x, y = [ int(x) for x in list(filter(lambda x: x != '', \
                input().strip().split(' '))) ]
            if x == 0 and y == 0:
                break
            posX += x
            posY += y
            dist = posX * posX + posY * posY
            if dist > maxDist or (dist == maxDist and posX > treasureX):
                maxDist = dist
                treasureX = posX
                treasureY = posY
        print(treasureX, treasureY)