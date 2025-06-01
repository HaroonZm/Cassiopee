hauteur, rapport = map(int, input().split())
if hauteur >= 0:
    print(1)
elif hauteur + rapport == 0:
    print(0)
else:
    print(-1)