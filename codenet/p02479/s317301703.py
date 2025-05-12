import math
import sys

r = float(raw_input())
print str('%.5f' % (r**2 * math.pi)) + " " + str('%.5f' % (r * 2 * math.pi))
sys.exit()