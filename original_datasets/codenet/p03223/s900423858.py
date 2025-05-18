N = int(input())

A = [int(input()) for i in range(N)]

A.sort()

right = A[0]
left = A[0]
index_l = 1
index_r = len(A)-1
ans_l = 0
count = 1
while(1):
	if count % 2 == 1:
		if index_r - index_l >= 1:
			if abs(left-A[index_r])+abs(right-A[index_r-1]) > abs(right-A[index_r])+abs(left-A[index_r-1]):
				ans_l += abs(left-A[index_r])+abs(right-A[index_r-1])
				left = A[index_r]
				right = A[index_r-1]
			else:
				ans_l += abs(right-A[index_r])+abs(left-A[index_r-1])
				left = A[index_r-1]
				right = A[index_r]
			index_r -= 2
		elif index_r - index_l == 0:
			if abs(left-A[index_r]) > abs(right-A[index_r]):
				ans_l += abs(left-A[index_r])
			else:
				ans_l += abs(right-A[index_r])
			index_r -= 1
		else: break
	else:
		if index_r - index_l >= 1:
			if abs(left-A[index_l])+abs(right-A[index_l+1]) > abs(right-A[index_l])+abs(left-A[index_l+1]):
				ans_l += abs(left-A[index_l])+abs(right-A[index_l+1])
				left = A[index_l]
				right = A[index_l+1]
			else:
				ans_l += abs(right-A[index_l])+abs(left-A[index_l+1])
				left = A[index_l+1]
				right = A[index_l]
			index_l += 2
		elif index_r - index_l == 0:
			if abs(left-A[index_r]) > abs(right-A[index_r]):
				ans_l += abs(left-A[index_r])
			else:
				ans_l += abs(right-A[index_r])
			index_l += 1
		else:
			break
	count += 1

A.reverse()

right = A[0]
left = A[0]
index_l = 1
index_r = len(A)-1
ans_r = 0
count = 1
while(1):
	if count % 2 == 1:
		if index_r - index_l >= 1:
			if abs(left-A[index_r])+abs(right-A[index_r-1]) > abs(right-A[index_r])+abs(left-A[index_r-1]):
				ans_r += abs(left-A[index_r])+abs(right-A[index_r-1])
				left = A[index_r]
				right = A[index_r-1]
			else:
				ans_r += abs(right-A[index_r])+abs(left-A[index_r-1])
				left = A[index_r-1]
				right = A[index_r]
			index_r -= 2
		elif index_r - index_l == 0:
			if abs(left-A[index_r]) > abs(right-A[index_r]):
				ans_r += abs(left-A[index_r])
			else:
				ans_r += abs(right-A[index_r])
			index_r -= 1
		else: break
	else:
		if index_r - index_l >= 1:
			if abs(left-A[index_l])+abs(right-A[index_l+1]) > abs(right-A[index_l])+abs(left-A[index_l+1]):
				ans_r += abs(left-A[index_l])+abs(right-A[index_l+1])
				left = A[index_l]
				right = A[index_l+1]
			else:
				ans_r += abs(right-A[index_l])+abs(left-A[index_l+1])
				left = A[index_l+1]
				right = A[index_l]
			index_l += 2
		elif index_r - index_l == 0:
			if abs(left-A[index_r]) > abs(right-A[index_r]):
				ans_r += abs(left-A[index_r])
			else:
				ans_r += abs(right-A[index_r])
			index_l += 1
		else:
			break
	count += 1

		
print(max(ans_l,ans_r))