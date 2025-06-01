import sys
import math

def solve():
    input = sys.stdin.readline
    while True:
        n = int(input())
        if n == 0:
            break
        m = int(input())
        edges = []
        for _ in range(m):
            line = input().strip()
            a,b,d = line.split(",")
            a,b,d = int(a),int(b),int(d)
            edges.append((d,a,b))
        edges.sort()
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(a,b):
            a=find(a)
            b=find(b)
            if a==b:
                return False
            parent[b]=a
            return True
        mst_total = 0
        count = 0
        for d,a,b in edges:
            if union(a,b):
                mst_total += d
                count += 1
                if count == n-1:
                    break
        # Nombre de lampions = (somme des distances dans MST) /100 - nombre_de_noeuds + 1
        # car chaque segment est éclairé par des lampions tous les 100m, pas sur les noeuds.
        lamps = mst_total//100 - (n - 1)
        print(lamps)

if __name__ == "__main__":
    solve()