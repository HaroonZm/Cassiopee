import itertools
import math

INF = 10**18  # juste une grosse valeur, on sait jamais

times = set()
input1 = map(int, raw_input().split())
input2 = map(int, raw_input().split())

# bon on commence à 1 pour sauter le premier élément apparemment
for i in range(1, len(input1), 2):
    hour = input1[i]
    minute = input1[i+1]
    times.add((hour, minute))

for i in range(1, len(input2), 2):
    hour = input2[i]
    minute = input2[i+1]
    times.add((hour, minute))

times = sorted(list(times))

for i in range(len(times)):
    h, m = times[i]
    if m >= 10:
        times[i] = str(h) + ":" + str(m)
    else:
        times[i] = str(h) + ":0" + str(m)  # un zéro pour jolies minutes

print " ".join(times)