import sys
from array import array

def main():
	while True:
		m = input()
		if m == 0: return 0
		dp = [array('I', [0] * 1001) for i in range(m + 1)]
		dp[0][0] = 1
		for i in xrange(m):
			v, c = map(int, raw_input().split())
			for j in xrange(1001):
				for k in xrange(c + 1):
					next = j + v * k
					if next > 1000: continue
					dp[i + 1][next] += dp[i][j]
		n = input()
		for i in range(n):
			x = input()
			print dp[m][x]

if __name__ == '__main__':
	sys.exit(main())