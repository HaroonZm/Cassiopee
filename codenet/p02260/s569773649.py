def selection_sort(A, N):
  sw = 0
  for i in range(0,N-1):
    minj = i
    for j in range(i,N):
      if A[j] < A[minj]:
        minj = j
    A[i], A[minj] = A[minj], A[i]
    if i != minj:
      sw += 1
  print(*A)
  print(sw)

N = int(input())
A = list(map(int, input().split()))
selection_sort(A, N)