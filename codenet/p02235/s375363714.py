def lcs(X,Y):
  L = []
  for yk in Y:
    prev_idx = -1
    for l_idx, l in enumerate(L):
      x_idx = X.find(yk, prev_idx + 1)
      if x_idx < 0:
        break
      L[l_idx] = min(l, x_idx) 
      prev_idx = l
    else:
      x_idx = X.find(yk, prev_idx + 1)
      if x_idx >= 0:
        L.append(x_idx)

  return len(L)

def main():
  q = int(input())
  for _ in range(q):
    X = input()
    Y = input()
    print(lcs(X,Y))

if __name__ == "__main__":
  import sys, io
  main()