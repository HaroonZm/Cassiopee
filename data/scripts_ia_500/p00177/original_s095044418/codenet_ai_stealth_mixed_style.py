import math
import sys
import os

def to_radians(deg):
    return deg * math.pi / 180

R = 6378.1

if os.getenv("PYDEV") == "True":
    sys.stdin = open("sample-input.txt", "rt")

def distance(lat1, long1, lat2, long2):
    # imperative style with math functions
    s1 = math.sin(lat1)
    s2 = math.sin(lat2)
    c1 = math.cos(lat1)
    c2 = math.cos(lat2)
    delta_long = long2 - long1
    angle = math.acos(s1 * s2 + c1 * c2 * math.cos(delta_long))
    return round(R * angle)

class InputReader:
    def __iter__(self):
        return self
    def __next__(self):
        line = input()
        if line.strip() == "-1 -1 -1 -1":
            raise StopIteration
        return list(map(float, line.strip().split()))

def main():
    reader = InputReader()
    for lat1d, long1d, lat2d, long2d in reader:
        # mix procedural and comprehension style
        lat1, long1, lat2, long2 = [to_radians(x) for x in (lat1d, long1d, lat2d, long2d)]
        print(distance(lat1, long1, lat2, long2))

if __name__ == "__main__":
    main()