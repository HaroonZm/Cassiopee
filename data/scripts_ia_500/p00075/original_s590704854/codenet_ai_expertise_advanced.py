import sys
from math import pow

print(*(int(float(line.split(',')[0])) for line in sys.stdin if float(line.split(',')[1]) / pow(float(line.split(',')[2]), 2) >= 25), sep='\n')