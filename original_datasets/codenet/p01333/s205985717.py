import sys

def solve():
    while True:
        v,m = map(int,raw_input().split())
        if [v,m] == [0,0]:
	    return
	r1,r5,r10 = 0,0,0
	re = m - v
	r10 = re / 1000
	re %= 1000
	r5 = re	/ 500
	re %= 500
	r1 = re	/ 100
	print str(r1) +	" " + str(r5) +	" " + str(r10)

if __name__ == "__main__":
    solve()