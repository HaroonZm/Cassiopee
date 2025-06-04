N, S = map(int, input().split())
As = list(map(int, input().split()))
i = 0
j = 0
sum = 0
m_l = float('inf')
broken = False

while not broken:
	while j < N and sum < S:
		sum += As[j]
		j += 1
	if sum < S:
		break
	if j - i < m_l:
		m_l = j - i
	sum -= As[i]
	i += 1

if m_l != float('inf'):
	print(m_l)
else:
	print(0)