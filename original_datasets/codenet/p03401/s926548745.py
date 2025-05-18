N, *A = map(int, open(0).read().split())
A = [0] + A + [0]
diff = [abs(A[i + 1] - A[i]) for i in range(N + 1)]
diff_i = [abs(A[i + 2] - A[i]) for i in range(N)]
a = sum(diff)
for i in range(N):
  print(a + diff_i[i] -  (diff[i] + diff[i + 1]))