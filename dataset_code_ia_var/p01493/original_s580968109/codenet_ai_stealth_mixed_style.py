import collections
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
printer = sys.stdout.write

def main():
 N = int(input())
 Graph = [[] for _ in range(N)]
 idx = 0
 while idx < N:
     buf = input()
     for column, ch in enumerate(buf.strip()):
         if ch == 'Y':
             Graph[idx].append(column)
     idx += 1
 degree_sum = 0
 odd_even_parts = [0, 0]
 marks = [False] * N
 count = 0
 for u in range(N):
     degree_sum += len(Graph[u])
     if marks[u]: continue
     marks[u] = True
     q = collections.deque()
     q.append(u)
     visited_cnt = 0
     while len(q):
         k = q.popleft()
         visited_cnt += 1
         for nb in Graph[k]:
             if marks[nb]:
                 continue
             marks[nb] = True
             q.append(nb)
     if visited_cnt % 2 == 0:
         odd_even_parts[0] += 1
     else:
         odd_even_parts[1] += 1
 pairs_parity = ((N*(N-1))//2 - degree_sum//2) & 1
 dp = dict()
 def rec(t, o, e):
     mykey = (o, e)
     if mykey in dp:
         return dp[mykey]
     if o+e == 2:
         res = (e==2) ^ pairs_parity
         out = res ^ (t&1)
         dp[mykey] = out
         return out
     val = 0
     if o > 1 or (o and e):
         if not rec(t+1, o-1, e):
             val = 1
     if e > 1:
         if not rec(t+1, o+1, e-2):
             val = 1
     dp[mykey] = val
     return val
 print_result = lambda s: printer(s+'\n')
 who = rec(0, odd_even_parts[0], odd_even_parts[1])
 print_result('Taro' if who else 'Hanako')

main()