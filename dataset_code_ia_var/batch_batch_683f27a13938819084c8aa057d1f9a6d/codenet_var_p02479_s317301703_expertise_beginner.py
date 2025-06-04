import math

r = float(raw_input())

aire = r * r * math.pi
perimetre = 2 * r * math.pi

print(str("%.5f" % aire) + " " + str("%.5f" % perimetre))