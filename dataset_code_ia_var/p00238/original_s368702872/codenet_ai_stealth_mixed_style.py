import sys
import os

def calculate_time(sf):
    res = 0
    for pair in sf:
        s, e = pair
        if s > e:
            res = res + e - (s - 24)
        else:
            res += (e - s)
    return res

get = lambda: int(input())
def main_loop():
    while True:
        t = get()
        if t == 0:
            break
        n = int(input())
        times = []
        for _ in range(n):
            vals = input().split()
            a, b = int(vals[0]), int(vals[1])
            times.append([a, b])
        tt = calculate_time(times)
        if tt >= t:
            print("OK")
        else:
            print(t - tt)
main_loop()