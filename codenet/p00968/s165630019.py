import sys
sys.setrecursionlimit(10**6)

def tl(s):
	pre = False
	ref = []
	for i in s:
		if ord(i) < 58:
			if pre:
				ref[-1] = [True, ref[-1][1]*10 + int(i)]
			else:
				pre = True
				ref += [[True, int(i)]]
		else:
			ref += [[False, i]]
			pre=False
	return ref

def main():
	n = int(input())
	pibot = tl(input())
	for _ in range(n):
		temp = tl(input())
		ans = "-"
		for i in range(len(temp)):
			if i >= len(pibot):
				ans = "+"
				break
			if pibot[i] == temp[i]:
				if pibot == temp:
					ans = "+"
					break
				continue
			if pibot[i][0] and not(temp[i][0]):
				ans = "+"
			elif not(pibot[i][0]) and temp[i][0]:
				ans = "-"
			elif pibot[i][0]:
				if pibot[i][1] < temp[i][1]:
					ans = "+"
				else:
					ans = "-"
			else:
				if ord(pibot[i][1]) < ord(temp[i][1]):
					ans = "+"
				else:
					ans = "-"
			break
		print(ans)
	return

main()