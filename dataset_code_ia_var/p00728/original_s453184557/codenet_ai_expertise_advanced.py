from statistics import mean
from itertools import islice, starmap

while True:
    if not (n := int(input())):
        break
    values = sorted(int(input()) for _ in range(n))
    avg = mean(islice(values, 1, -1))
    print(int(avg))