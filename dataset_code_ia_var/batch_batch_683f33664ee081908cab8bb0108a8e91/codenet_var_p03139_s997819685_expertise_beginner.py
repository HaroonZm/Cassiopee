# modules importés, mais seuls 'input' utiles ici
# import math
# import fractions
# import sys
# import bisect
# import heapq
# import collections
# from collections import Counter
# from collections import deque
# import pprint
# import itertools

# Fonctions utilitaires pour entrée
def sr():
    return input()

def ir():
    return int(input())

def lr():
    return list(map(int, input().split()))

# Décomposition en facteurs premiers de n
def factorization(n):
    result = []
    temp = n
    if n == 1:
        return result
    i = 2
    while i * i <= temp:
        if temp % i == 0:
            count = 0
            while temp % i == 0:
                temp //= i
                count += 1
            result.append([i, count])
        i += 1
    if temp != 1:
        result.append([temp, 1])
    if len(result) == 0:
        result.append([n, 1])
    return result

# Puissance modulo
def power(a, n, mod):
    x = 1
    while n > 0:
        if n % 2 == 1:
            x = x * a % mod
        a = a * a % mod
        n = n // 2
    return x % mod

# Produit décroissant modulo
def kaijo(n, l, mod):
    if n == 0:
        return 1
    a = n
    temp = n - 1
    while temp >= l:
        a = a * temp % mod
        temp -= 1
    return a

# Structure Union-Find simple
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        while self.parents[x] >= 0:
            if self.parents[self.parents[x]] >= 0:
                self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        group = []
        for i in range(self.n):
            if self.find(i) == root:
                group.append(i)
        return group

    def roots(self):
        roots = []
        for i in range(self.n):
            if self.parents[i] < 0:
                roots.append(i)
        return roots

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        dic = {}
        for r in self.roots():
            dic[r] = self.members(r)
        return dic

    def __str__(self):
        return "\n".join("{}:{}".format(r, self.members(r)) for r in self.roots())

# Liste des diviseurs de n
def make_divisors(n):
    divisors = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
        i += 1
    divisors.sort()
    return divisors

# Constantes
inf = 10 ** 18
mod = 10 ** 9 + 7

# Entrée et sortie principale
n, a, b = lr()
print(min(a, b), max(0, a + b - n))