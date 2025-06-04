import sys
input=sys.stdin.readline

def field_clear(field):
    new_field=[]
    cleared=0
    for layer in field:
        if all(cell=='#' for row in layer for cell in row):
            cleared+=1
        else:
            new_field.append(layer)
    # after clearance, blocks above drop one layer, but only once per clearance
    return new_field, cleared

def can_place(field,x,y,z,block):
    for dz in range(2):
        for dx in range(2):
            for dy in range(2):
                if block[dz][dx][dy]=='#':
                    fx = x+dx
                    fy = y+dy
                    fz = z+dz
                    if fz<0 or fx<0 or fy<0:
                        return False
                    if fz < len(field):
                        if field[fz][fx][fy]=='#':
                            return False
    return True

def place_block(field,x,y,z,block):
    # may extend field height if needed
    H = len(field)
    if z+1>=H:
        for _ in range(z+2 - H):
            field.append([['.' for _ in range(2)] for __ in range(2)])
    for dz in range(2):
        for dx in range(2):
            for dy in range(2):
                if block[dz][dx][dy]=='#':
                    fx = x+dx
                    fy = y+dy
                    fz = z+dz
                    field[fz][fx][fy]='#'

def copy_field(field):
    return [[row[:] for row in layer] for layer in field]

def main():
    while True:
        H,N = map(int,input().split())
        if H==0 and N==0:
            break
        field=[]
        for _ in range(H):
            layer = [list(input().rstrip()) for __ in range(2)]
            field.append(layer)
        blocks=[]
        for _ in range(N):
            block=[ [list(input().rstrip()) for __ in range(2)] for ___ in range(2)]
            blocks.append(block)

        max_cleared=0

        def dfs(cur_field, idx, cleared_count):
            nonlocal max_cleared
            if idx==N:
                if cleared_count>max_cleared:
                    max_cleared=cleared_count
                return
            block = blocks[idx]
            # try all horizontal translations: x,y in {0,1}
            for x in range(1):
                for y in range(1):
                    # find drop z
                    z=-1
                    while True:
                        if can_place(cur_field,x,y,z+1,block):
                            z+=1
                        else:
                            break
                    if z==-1:
                        continue
                    new_field=copy_field(cur_field)
                    place_block(new_field,x,y,z,block)
                    total_cleared=0
                    while True:
                        new_field, cleared = field_clear(new_field)
                        if cleared==0:
                            break
                        total_cleared+=cleared
                    dfs(new_field,idx+1,cleared_count+total_cleared)

        # Since translations are 0 or 1 (horizontal plane is always 2x2)
        dfs(field,0,0)
        print(max_cleared)

if __name__=="__main__":
    main()