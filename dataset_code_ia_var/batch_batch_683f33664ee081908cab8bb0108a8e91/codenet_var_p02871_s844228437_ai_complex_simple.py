import functools
import itertools
import collections
import operator
import sys

# Redéfinir raw_input pour Python 3 compatibilité
try:
    raw_input
except NameError:
    raw_input = lambda: sys.stdin.readline()

out = open('out.txt', 'a')

class graph:
    INF = float('inf')
    G = None
    Path = None
    E = None
    V = None

    def __init__(self):
        dataRaw = raw_input()
        raw = list(map(int, dataRaw.strip().split()))
        self.E, self.V = raw[0]+1, raw[1]
        # Génère une matrice carré via accumulate et map en imitant list comprehension
        def build_matrix(val):
            return list(map(lambda _: [val]*self.E, range(self.E)))
        self.G = list(map(list, build_matrix(self.INF)))
        self.Path = list(map(list, build_matrix(0)))

        # construction via un générateur + tuple unpacking et items
        for _ in map(lambda x: x, range(self.V)):
            dataRaw = raw_input()
            i, j, k = tuple(map(int, dataRaw.strip().split()))
            # Utilise l'opérateur setitem pour assigner 
            operator.setitem(self.G[i], j, k)
            operator.setitem(self.G[j], i, k)

        # Force diagonal à 0 en compressant i->[i,i]
        for i, v in enumerate(itertools.repeat(0, self.E), 1):
            operator.setitem(self.G[i], i, 0)

        # Floyd-Warshall non-idiot-proof via itertools.product et astuce lambda triplement imbriquée
        for i, j, k in itertools.product(range(self.E), repeat=3):
            self.G[i][j], _ = min(
                (self.G[i][j], 0),
                (self.G[i][k]+self.G[k][j], 1),
                key=lambda x: x[0]
            )
            if self.G[i][j] == self.G[i][k] + self.G[k][j]:
                self.Path[i][j] = k

    def shortPath(self, i, j):
        # Recursion par une fonction curryfiée et reduce
        path = []
        def core(a, b, p=path):
            if self.Path[a][b]==0:
                if not p or p[-1] != a:
                    p.append(a)
                p.append(b)
            else:
                core(a, self.Path[a][b])
                core(self.Path[a][b], b)
        core(i, j)
        path = list(itertools.islice(path, 1, None))
        return path

class driver:
    plan = None
    order = None
    location = None
    nextSegmentLeftTime = None
    target = None

    def __init__(self, g):
        self.plan = []
        self.order = set()
        self.location = 1
        self.nextSegmentLeftTime = 0
        self.target = 1
        self.map = g

    def route(self):
        # Utilise un double reduce pour transformer une série de detours
        if not self.order and not self.plan:
            self.order.add(1)
        last = functools.reduce(lambda x, y: y, self.plan, self.location) if self.plan else self.location
        if self.order:
            # Chainer tous les chemins à suivre via chain et update
            combined_path = []
            for i in self.order:
                combined_path.extend(self.map.shortPath(last, i))
                last = i
            self.plan.extend(combined_path)
            self.order.clear()
        if self.plan:
            self.target = self.plan[0]
            self.nextSegmentLeftTime = self.map.G[self.location][self.target]
            del self.plan[0]

    def move(self):
        if self.location == self.target:
            print(-1)
            return
        assert self.nextSegmentLeftTime > 0
        self.nextSegmentLeftTime -= 1
        print(self.target)
        if self.nextSegmentLeftTime == 0:
            self.location = self.target

    def onRoute(self):
        return bool(self.nextSegmentLeftTime)

class shop:
    def __init__(self):
        self.order = set()

class timer:
    orders = None
    times = None
    orderIndex = None
    currTime = None
    Tmax = None

    def __init__(self):
        self.orders = []
        self.times = []
        self.orderIndex = 0
        self.currTime = 0
        self.Tmax = int(raw_input())
        for i in range(self.Tmax):
            n = int(raw_input())
            if n == 0:
                continue
            else:
                data = list(map(int, raw_input().strip().split()))
                self.times.append(i+1)
                self.orders.append(data[1])

    def run(self, shop, driver):
        # Découpe le temps en itérateurs d'une manière cryptique
        while self.currTime < self.Tmax:
            self.currTime += 1
            if (self.orderIndex < len(self.times) and
                self.currTime == self.times[self.orderIndex] and
                driver.map.G[1][self.orders[self.orderIndex]] < float('inf')):
                shop.order.add(self.orders[self.orderIndex])
                self.orderIndex += 1
            if not driver.onRoute() and driver.location == 1:
                driver.order |= shop.order
                shop.order.clear()
            if not driver.onRoute():
                driver.route()
            driver.move()
            out.write("status after : ")
            out.write("shop status : " + str(shop.order))
            out.write("driver status : ")
            out.write("order : " + str(driver.order))
            out.write("| plan : " + str(driver.plan))
            out.write("| on route : " + str(driver.onRoute()))
            out.write("| location : " + str(driver.location))
            out.write("| target : " + str(driver.target))
            out.write("| left time : " + str(driver.nextSegmentLeftTime) + '\n')
            out.write("================================\n")

if __name__ == "__main__":
    s = shop()
    g = graph()
    d = driver(g)
    t = timer()
    t.run(s, d)