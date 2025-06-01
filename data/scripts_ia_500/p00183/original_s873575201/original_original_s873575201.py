"""
http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0183

"""
import sys
from sys import stdin
input = stdin.readline

def solve(board):
    colors = ['b', 'w']
    for c in colors:
        for y in range(3):
            if board[y].count(c) == 3:
                return c
        for x in range(3):
            if board[0][x] == c and board[1][x] == c and board[2][x] == c:
                return c
        if board[0][0] == c and board[1][1] == c and board[2][2] == c:
            return c
        if board[0][2] == c and board[1][1] == c and board[2][0] == c:
            return c
    return 'NA'

def main(args):
    while True:
        temp = input().strip()
        if temp[0] == '0':
            break
        board = []
        board.append(list(temp))
        board.append(list(input().strip()))
        board.append(list(input().strip()))
        result = solve(board)
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])