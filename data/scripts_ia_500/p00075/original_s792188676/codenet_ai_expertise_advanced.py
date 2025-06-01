import sys

print(*(uid for line in sys.stdin if (w := float(line.split(',')[1])) / ((h := float(line.split(',')[2])) ** 2) >= 25 for uid in [line.split(',')[0]]), sep='\n')