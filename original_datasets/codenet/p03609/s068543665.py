#n = int(input())
x, t = map(int, input().split())
#l = list(map(int,input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
print(max(x-t, 0))