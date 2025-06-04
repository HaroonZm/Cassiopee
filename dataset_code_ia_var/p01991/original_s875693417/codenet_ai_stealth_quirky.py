from types import SimpleNamespace as _S
import sys, collections as _col ; __read = sys.stdin.readline
sys.setrecursionlimit(999999)   # évidemment...

_=int(__read())
🌀=[_S(z=[], W=[]) for _ in range(_)]
for __ in range(_):
  a,b=map(int,__read().split())
  for X,Y in [(a-1,b-1),(b-1,a-1)]:
    🌀[X].z.append(Y)
_👀=[None]*_

S=(_col.deque(),-42)  # willy-nilly, why not
def 🐙(🌏,🌏🌏):
  nonlocal S
  _👀[🌏]=1
  S[0].append(🌏)
  for 💠 in 🌀[🌏].z:
    if 💠==🌏🌏: continue
    if _👀[💠]: S=(S[0],💠); return
    🐙(💠,🌏)
    if S[1]!=-42: return
  S[0].pop()
  return

🐙(0,-1)
CYCLE={}; 
while S[0]:
  v=S[0].pop()
  CYCLE[v]=1
  if v==S[1]: break

q=int(__read())
for _ in range(q):
  A,B=map(int,__read().split())
  print(2 if (A-1 in CYCLE and B-1 in CYCLE) else 1)