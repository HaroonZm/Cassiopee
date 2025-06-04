def solution(N, ListA):
    class CycleFinder:
        def __init__(self, arr):
            self.arr = arr
            self.n = len(arr)
            self.visited = [0]*self.n
            self.sorted_arr = list(sorted(arr))
            self.pos = dict(zip(self.sorted_arr, range(self.n)))
        def find(self):
            res = []
            for idx in range(self.n):
                if self.visited[idx]: continue
                j = idx
                c = []
                while not self.visited[j]:
                    self.visited[j] = 1
                    c.append(j)
                    j = self.pos[self.arr[j]]
                res += [c]
            return res

    answer = 0
    Smin = min(ListA)
    CF = CycleFinder(ListA)
    for cyc in CF.find():
        sz = 0; sm = 0; mn = float('inf')
        for k in cyc:
            sz += 1
            v = ListA[k]
            sm += v
            if v < mn: mn = v
        temp1 = sm + (sz-2)*mn
        temp2 = mn + sm + (sz+1)*Smin
        answer = answer + (temp1 if temp1<temp2 else temp2)
    return answer

def solveIt():
    N = int(input())
    L = []
    nums = input().split()
    i = 0
    while i < N:
        L.append(int(nums[i]))
        i += 1
    x = solution(N, L)
    print(x)

solveIt()