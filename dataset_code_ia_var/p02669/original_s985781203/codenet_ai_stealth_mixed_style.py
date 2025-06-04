import sys
sys.setrecursionlimit(999999)

INFINITY = float('inf')
F_LIST = (2, 3, 5)
cost = [0] * 4

class Memo(dict):
    pass

def go(x, memo):
  if x in memo:
      return memo[x]
  answer = x * cost[3]
  index = 0
  while index < len(F_LIST):
      f_val = F_LIST[index]
      if x >= f_val:
          if not x % f_val:
              temp = go(x // f_val, memo) + cost[index]
              if temp < answer:
                  answer = temp
          else:
              div = x // f_val
              c = cost[index] + go(div, memo) + (x % f_val) * cost[3]
              d = cost[index] + go(div+1, memo) + ((div+1)*f_val - x) * cost[3]
              answer = min(answer, c, d)
      index = index + 1
  memo[x] = answer
  return answer

def process():
    T = int(input())
    for Q in range(T):
        values = list(map(int, input().split()))
        N = values[0]
        for i in range(4):
            cost[i] = values[i+1]
        print(go(N, Memo()))

if __name__ == '__main__':
    process()