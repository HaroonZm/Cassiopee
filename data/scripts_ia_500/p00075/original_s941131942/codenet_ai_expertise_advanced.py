import sys

print(*(int(float(line.split(",")[0])) for line in sys.stdin if float(line.split(",")[1]) / float(line.split(",")[2])**2 >= 25.0), sep="\n")