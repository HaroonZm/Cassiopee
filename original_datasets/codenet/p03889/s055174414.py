import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

S = input().rstrip()

T = S[::-1]
T = T.replace('b','*').replace('d','b').replace('*','d')
T = T.replace('p','*').replace('q','p').replace('*','q')

answer = 'Yes' if S == T else 'No'
print(answer)