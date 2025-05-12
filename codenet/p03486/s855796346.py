#!/usr/bin/env python3

def solve(s,t):

  s = (sorted(s))
  t = (sorted(t,reverse=True))

  return s < t

def main():
  S = input()
  T = input()
  print("Yes" if solve(S,T) else "No")
  return

if __name__ == '__main__':
  main()