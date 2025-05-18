import sys
sys.setrecursionlimit(2147483647)
input=sys.stdin.readline

def main():
  x = list(map(int, input().split(' ')))
  print(15-sum(x))

if __name__=='__main__':
  main()