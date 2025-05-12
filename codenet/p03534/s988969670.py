S = list(input())
N = len(S)
A = S.count("a")
B = S.count("b")
C = S.count("c")

if  N % 3 == 0:
	if A == B and B == C:
		print("YES")
	else:
		print("NO")
else:
	n = int(N // 3)
	if n <= A and A <= n + 1 and n <= B and B <= n + 1 and n <= C and C <= n + 1:
		print("YES")
	else:
		print("NO")