w, h, t = map(int, input().split())
p = int(input())
c = [tuple(map(int, input().split())) for _ in range(p)]
area = [tuple(map(int, input().split())) for _ in range(h)]
print(sum([area[i[1]][i[0]] for i in c]))