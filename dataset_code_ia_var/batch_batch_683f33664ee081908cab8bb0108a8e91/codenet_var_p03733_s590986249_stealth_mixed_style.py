from functools import reduce

def main():
  N,T=[int(x)for x in input().split()]
  t=[*map(int,input().split())]
  total=T
  idx=0
  while idx<N-1:
    total+=T if t[idx+1]-t[idx]>=T else t[idx+1]-t[idx]
    idx+=1
  print(total)

if __name__== '__main__':
  main()