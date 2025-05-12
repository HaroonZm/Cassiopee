import sys
def input():
	return sys.stdin.readline().strip()

N = int(input())
A, B = list(map(int, input().split()))
P = list(map(int, input().split()))

sum_list = [0]*3
for i in range(N):
	if P[i] <= A:
		sum_list[0] += 1
	elif P[i] <= B:
		sum_list[1] += 1
	else:
		sum_list[2] += 1

print(min(sum_list))