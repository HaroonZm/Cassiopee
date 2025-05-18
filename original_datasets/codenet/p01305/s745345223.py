from itertools import permutations as pm

def main():
  t = int(input())
  fact9 = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2
  for _ in range(t):
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    ans1 = 0
    ans2 = 0
    for hand in pm(l2, 9):
      score1 = 0
      score2 = 0
      for i, j in zip(l1, hand):
        if i < j:
          score2 += (i + j)
        else:
          score1 += (i + j)
      if score1 < score2:
        ans2 += 1
      elif score1 > score2:
        ans1 += 1
    print(ans1 / fact9, ans2 / fact9)

main()