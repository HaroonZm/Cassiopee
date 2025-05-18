import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**10
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    while True:
        n, w, d = LI()
        if n==0 and w==0 and d==0:
            break

        cake = []
        cake.append([w, d])
        for _ in range(n):
            ps = LI()
            p = ps[0]-1
            s = ps[1]
            # ケーキカット
            cake_w = cake[p][0]
            cake_d = cake[p][1]
            s %= (cake_w+cake_d)*2
            if s<cake_w:
                new_cake_s = [min(s, cake_w-s), cake_d]
                new_cake_l = [max(s, cake_w-s), cake_d]
            elif cake_w<s<cake_w+cake_d:
                new_cake_s = [cake_w, min(s-cake_w, cake_w+cake_d-s)]
                new_cake_l = [cake_w, max(s-cake_w, cake_w+cake_d-s)]
            elif cake_w+cake_d<s<cake_w+cake_d+cake_w:
                new_cake_s = [min(s-(cake_w+cake_d), cake_w+cake_d+cake_w-s), cake_d]
                new_cake_l = [max(s-(cake_w+cake_d), cake_w+cake_d+cake_w-s), cake_d]
            else:
                new_cake_s = [cake_w, min(s-(cake_w+cake_d+cake_w), cake_w+cake_d+cake_w+cake_d-s)]
                new_cake_l = [cake_w, max(s-(cake_w+cake_d+cake_w), cake_w+cake_d+cake_w+cake_d-s)]

            # id付け替え
            del cake[p]
            # 新ケーキ追加 
            cake.append(new_cake_s)
            cake.append(new_cake_l)

        print(*sorted([i[0]*i[1] for i in cake]))

if __name__ == '__main__':
    resolve()