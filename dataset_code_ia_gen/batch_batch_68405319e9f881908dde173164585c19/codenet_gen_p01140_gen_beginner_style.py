while True:
    line = input()
    if line == '':
        break
    N, M = map(int, line.split())
    if N == 0 and M == 0:
        break
    h = []
    for _ in range(N):
        h.append(int(input()))
    w = []
    for _ in range(M):
        w.append(int(input()))
    # Calculate vertical cumulative sums
    vertical = [0]
    for i in range(N):
        vertical.append(vertical[-1] + h[i])
    # Calculate horizontal cumulative sums
    horizontal = [0]
    for i in range(M):
        horizontal.append(horizontal[-1] + w[i])
    # Count squares
    count = 0
    # For all pairs of horizontal roads, calculate the segment length and check if exists in vertical segments
    segments_v = {}
    for i in range(N):
        for j in range(i+1, N+1):
            length = vertical[j] - vertical[i]
            if length in segments_v:
                segments_v[length] +=1
            else:
                segments_v[length] =1
    for i in range(M):
        for j in range(i+1, M+1):
            length = horizontal[j] - horizontal[i]
            if length in segments_v:
                count += segments_v[length]
    print(count)