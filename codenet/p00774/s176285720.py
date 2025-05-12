def puyo_one(A):
  ans = 0
  now = 1
  for i in range(1, 5):
    if A[i] == A[i - 1]:
      now += 1
    else:
      if now >= 3:
        ans += now * A[i - 1]
      now = 1
  return ans

def puyo(A):#A:配列
  p = 0#消せるものがなくなったらp=1とし、ansを返す
  ans = 0
  while p == 0:
    this = 0
    #ぷよを消して加点
    for i in range(len(A)):
      now = 1 
      for j in range(1, 5):
        if (A[i][j] == A[i][j - 1]) and (A[i][j] != 0):
          now += 1
        else:
          if now >= 3:
            this = 1
            ans += A[i][j - 1] * now 
            for k in range(j - now, j):
              A[i][k] = 0
          now = 1
      if now >= 3:
        this = 1
        ans += A[i][j - 1] * now 
        for k in range(j - now + 1, j + 1):
          A[i][k] = 0
    #print(A, this, ans)
    #一回も消してない場合
    if this == 0:
      p = 1
    #残ったぷよを落とす
    #落とすところ
    N = len(A)
    for i in range(1, N + 1):
      for j in range(5):
        if (A[N - i][j] == 0) and (i != N):
          k = 1
          while (A[N - i - k][j] == 0) and (k + i < N):
            k += 1
          A[N - i][j] = A[N - i - k][j]
          A[N - i - k][j] = 0
    #一つもない行がある時、その行ごと消す
    q = 0
    while q == 0:
      if [0, 0, 0, 0, 0] in A:
        A.pop(A.index([0, 0, 0, 0, 0]))
      else:
        q = 1
    #print(A)
  return ans

l = 0
while l == 0:
  H = int(input())
  if H == 0:
    quit()
  else:
    A = [0] * H
    for i in range(H):
      A[i] = list(map(int, input().split()))
      #print(A)
    print(puyo(A))