import math

def mean_sd(buff):
    n = len(buff)
    m = float(sum(buff)) / n
    s1 = 0.0
    for x in buff:
        a = x - m
        s1 += a * a
    s1 = math.sqrt(s1 / n)
    return s1

while True:
    if raw_input() == "0":
        break
    x = map(float,raw_input().split(" "))
    print mean_sd(x)