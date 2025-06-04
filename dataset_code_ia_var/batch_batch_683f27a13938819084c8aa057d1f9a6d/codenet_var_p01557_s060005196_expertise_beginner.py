import sys
import heapq
import collections

sys.setrecursionlimit(10000000)

INF = 10 ** 20

def LI():
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def main():
    results = []

    def solve(n):
        a = LI()

        def search(start, target):
            # On utilise heapq comme une file de priorité pour BFS
            dist = {}
            dist[start] = 0
            q = []
            heapq.heappush(q, (0, start))
            used = {}
            while q:
                steps, perm = heapq.heappop(q)
                if perm == target:
                    return steps
                if perm in used:
                    continue
                used[perm] = True
                for i in range(n):
                    for j in range(i+1, n):
                        new_perm = perm[:i] + perm[i:j+1][::-1] + perm[j+1:]
                        if new_perm in used:
                            continue
                        if new_perm not in dist or dist[new_perm] > steps + 1:
                            dist[new_perm] = steps + 1
                            if steps + 1 < 4:
                                heapq.heappush(q, (steps + 1, new_perm))
            return dist

        start_tuple = tuple(a)
        sorted_tuple = tuple(sorted(a))

        res1 = search(start_tuple, sorted_tuple)
        if isinstance(res1, int):
            return res1
        res2 = search(sorted_tuple, start_tuple)
        min_res = n - 1
        for key in res1:
            if key in res2:
                temp = res1[key] + res2[key]
                if temp < min_res:
                    min_res = temp
        return min_res

    while True:
        n = I()
        if n == 0:
            break
        ans = solve(n)
        results.append(ans)
        break

    print('\n'.join(map(str, results)))

main()