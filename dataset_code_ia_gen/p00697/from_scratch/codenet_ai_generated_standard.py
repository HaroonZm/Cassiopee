import sys
sys.setrecursionlimit(10**7)

pairs = {'R':'r','G':'g','B':'b','W':'w'}
def match(a,b):
    return pairs.get(a,'') == b

def rotations(piece):
    # piece: top,right,bottom,left
    t,r,b,l = piece
    return [piece, (l,t,r,b), (b,l,t,r), (r,b,l,t)]

def canonical(piece):
    return min(rotations(piece))

def edge_constrain(pos,piece_rot,board):
    r,c = pos//3,pos%3
    top,right,bottom,left = piece_rot
    # up
    if r>0:
        up_piece = board[pos-3]
        if not match(up_piece[2],top):
            return False
    # left
    if c>0:
        left_piece = board[pos-1]
        if not match(left_piece[1],left):
            return False
    return True

def backtrack(pos, pieces, board, used, count):
    if pos==9:
        count[0]+=1
        return
    for i,piece in enumerate(pieces):
        if not used[i]:
            for rot in rotations(piece):
                if edge_constrain(pos, rot, board):
                    board[pos]=rot
                    used[i]=True
                    backtrack(pos+1,pieces,board,used,count)
                    used[i]=False

def solve(puzzle):
    pieces = [p for p in puzzle.split()]
    pieces = [tuple(p) for p in pieces]
    return

def main():
    input = sys.stdin.read().strip().split('\n')
    n=int(input[0])
    for line in input[1:1+n]:
        pieces = [tuple(p) for p in line.strip().split()]
        board = [None]*9
        used = [False]*9
        count = [0]
        backtrack(0,pieces,board,used,count)
        print(count[0])

if __name__=='__main__':
    main()