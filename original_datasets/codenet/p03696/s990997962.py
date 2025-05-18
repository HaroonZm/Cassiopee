def two_int():
    N, K = map(int, input().split())
    return N,K

def one_int():
    return int(input())

def one_str():
    return input()

def many_int():
    return list(map(int, input().split()))
# import sys
# input = sys.stdin.readline

N=one_int()
S=one_str()

head = 0
tail = 0

point=0
for a in S:
    if a =="(":
        point+=1
    else:
        point -=1
    if point<0:
        head += 1
        
        #ここで先頭にカッコをつけるのでその分のポイントは差し引き０
        point += 1

print("("*head + S + abs(point)*")")