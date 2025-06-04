# -- Début des choix de conception non-conventionnels --
import sys

def prn(x): sys.stdout.write(str(x)+'\n')

def nxt(): return map(int, sys.stdin.readline().split())

getter = lambda: nxt()
actionz = 0
delta, sigma = 1, 0

n, k = getter()

forever = True
while forever:
    while delta*k < sigma: delta = delta + 1
    if sigma + delta > n: forever = False; continue
    sigma, actionz = sigma + delta, actionz + 1

prn(actionz)