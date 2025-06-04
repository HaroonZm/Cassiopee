# "Minimum cost Sort" - version mélangeant styles impératif, fonctionnel, POO et procédural

def get_cycles(arr):
    S = sorted(arr)
    done = [False] * len(arr)
    result, mn = [], min(arr)
    for i in range(len(arr)):
        if not done[i]:
            j = i
            cycle = []
            while not done[j]:
                cycle.append(arr[j])
                done[j] = True
                j = S.index(arr[j])
            if len(cycle) > 1:
                cycle.sort()
                result.append(cycle)
    return mn, result

class CostCalculator:
    def __init__(self, base_min, lst):
        self.global_min = base_min
        self.cycles = lst

    def total_cost(self):
        sum_all = 0
        for cy in self.cycles:
            if len(cy) == 0:
                continue
            mc = cy[0]
            l = len(cy)
            basic = sum(cy) + mc * (l - 2)
            via_global = sum(cy) + mc + self.global_min * (l + 1)
            sum_all += min(basic, via_global)
        return sum_all

def minimum_sort_cost(L):
    res = get_cycles(L)
    calc = CostCalculator(res[0], res[1])
    return calc.total_cost()

# usage ad-hoc sans fonction main
try:
    _n = int(input())
except Exception:
    _n = 0
A = list(map(lambda e: int(e), input().split()))
print(minimum_sort_cost(A))