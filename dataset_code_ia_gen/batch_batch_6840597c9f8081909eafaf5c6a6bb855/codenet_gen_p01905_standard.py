import sys
sys.setrecursionlimit(10**7)

N,M=map(int,input().split())
withdrawn=set(int(input()) for _ in range(M))

def tournament(players):
    if len(players)==1:
        return players[0],0
    mid=len(players)//2
    left_winner,left_count=tournament(players[:mid])
    right_winner,right_count=tournament(players[mid:])
    if left_winner is None and right_winner is None:
        return None,0
    if left_winner is None:
        return right_winner,right_count
    if right_winner is None:
        return left_winner,left_count
    return (left_winner, right_winner)[False],left_count+right_count+1

players=[None if i in withdrawn else i for i in range(N)]
_,count=tournament(players)
print(count)