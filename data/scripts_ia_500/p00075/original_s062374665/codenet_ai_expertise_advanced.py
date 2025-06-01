import sys

print(*(f"{int(float(s))}" for line in sys.stdin if (vals := list(map(float, line.split(",")))) and vals[1] / vals[2] ** 2 >= 25), sep="\n")