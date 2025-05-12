if __name__ == '__main__':
  N = int(input())
  A = []
  B = []
  for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
  ans = 0
  for i in range(N-1, -1, -1):
    if (A[i]+ans) % B[i] == 0:
      continue
    ans += B[i] - (A[i]+ans) % B[i]
  print(ans)