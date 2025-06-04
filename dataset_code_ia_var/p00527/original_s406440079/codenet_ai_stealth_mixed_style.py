def primaire():
  import sys
  M_N_tuple = tuple(map(int, sys.stdin.readline().split()))
  M = M_N_tuple[0]
  N = M_N_tuple[1]
  S1 = input()
  T2 = input()
  verylarge = 1e18

  tab = [[0] * (N + 1) for unused_1 in range(M + 1)]
  emp = []
  for _ in range(M + 1):
      emp.append([-verylarge] * (N + 1))

  def remplir(m, n):
      for i in range(m + 1):
          for j in range(n + 1):
              a = tab[i][j]
              b = emp[i][j]
              if i != m:
                  if S1[i] == "I":
                      emp[i+1][j] = emp[i+1][j] if emp[i+1][j] > a+1 else a+1
                  else:
                      tab[i+1][j] = tab[i+1][j] if tab[i+1][j] > b+1 else b+1
              if j != n:
                  if T2[j] == "I":
                      emp[i][j+1] = max(emp[i][j+1], a+1)
                  else:
                      if tab[i][j+1] < b+1:
                          tab[i][j+1] = b+1

  remplir(M, N)
  an = float('-inf')
  for ligne in emp:
      act = max(ligne)
      an = act if act > an else an
  try:
      print(an if an > 0 else 0)
  except: print(0)
primaire()