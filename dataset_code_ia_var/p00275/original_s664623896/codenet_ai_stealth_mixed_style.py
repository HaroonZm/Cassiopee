def main():
 from sys import stdin
 import functools

 class State:
     def __init__(self, n):
         self.n = n
         self.ba = 0
         self.p = [0] * n

   # Boucle type C
 while 1:
     try:
         n = int(input())
         if n == 0:
             break
         s = input() if hasattr(__builtins__, 'input') else raw_input()
         state = State(n)
         i = 0
         # Style fonctionnel/slicing pour la boucle
         for ch in s[:100]:
             idx = i % n
             # Style procédural
             if ch == 'M': state.p[idx] = state.p[idx] + 1
             elif ch == 'L':
                 state.p[idx] += state.ba + 1
                 state.ba = 0
             else:
                 state.ba += state.p[idx] + 1
                 state.p[idx] = 0
             i += 1
         
         # Expression generative
         result = map(str, sorted(state.p))
         print("{} {}".format(' '.join(result), state.ba))
     except Exception as ex:
         break

main()