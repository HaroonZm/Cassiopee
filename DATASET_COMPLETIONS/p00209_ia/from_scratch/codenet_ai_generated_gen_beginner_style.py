def rotate_90(matrix):
    n = len(matrix)
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[j][n-1-i] = matrix[i][j]
    return res

def equal_with_hole(sc, ph, x, y):
    # sc: scenery
    # ph: photo pattern
    m = len(ph)
    for i in range(m):
        for j in range(m):
            if ph[i][j] == -1:
                continue
            if sc[x+i][y+j] != ph[i][j]:
                return False
    return True

def find_top_left(photo):
    m = len(photo)
    top = m
    left = m
    for i in range(m):
        for j in range(m):
            if photo[i][j] != -1:
                if i < top:
                    top = i
                if j < left:
                    left = j
    return top, left

def main():
    while True:
        line=input()
        if line == "":
            continue
        n,m= map(int,line.split())
        if n == 0 and m == 0:
            break
        scenery = []
        for _ in range(n):
            scenery.append(list(map(int,input().split())))
        photo = []
        for _ in range(m):
            photo.append(list(map(int,input().split())))
        
        # rotations of photo
        photos = [photo]
        for _ in range(3):
            photos.append(rotate_90(photos[-1]))
        
        candidates = []
        for p in photos:
            for x in range(n - m + 1):
                for y in range(n - m + 1):
                    if equal_with_hole(scenery, p, x, y):
                        # find top-left non -1 cell in photo
                        top,left = find_top_left(p)
                        candidates.append( (x+top, y+left) )
        if not candidates:
            print("NA")
        else:
            candidates.sort()
            print(candidates[0][0], candidates[0][1])

if __name__ == "__main__":
    main()