from functools import reduce
from operator import mul
import sys

def ipmatch(ip, iprule):
    # Utilisation de zip et all pour une écriture concise et optimisée
    return all(r == '?' or a == r for a, r in zip(ip, iprule))

def rulematch(sip, dip, rule):
    return ipmatch(sip, rule[1]) and ipmatch(dip, rule[2])

def main():
    readline = sys.stdin.readline  # Plus rapide que raw_input dans les boucles
    while True:
        try:
            n, m = map(int, readline().split())
        except ValueError:
            break
        if n == 0 and m == 0:
            break
        ansmes = []
        rules = [readline().split() for _ in range(n)]
        messages = [readline().split() for _ in range(m)]
        for sip, dip, msg in messages:
            for rule in reversed(rules):  # Ordre inverse, plus pythonique
                if rule[0] == 'deny':
                    if rulematch(sip, dip, rule):
                        break
                else:
                    if rulematch(sip, dip, rule):
                        ansmes.append((sip, dip, msg))
                        break
        print(len(ansmes))
        for sip, dip, msg in ansmes:
            print(sip, dip, msg)

if __name__ == "__main__":
    main()