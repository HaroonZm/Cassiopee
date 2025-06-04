n = int(input())
heights = list(map(int, input().split()))

max_area = 0
for i in range(n):
    min_height = heights[i]
    for j in range(i, n):
        if heights[j] < min_height:
            min_height = heights[j]
        area = min_height * (j - i + 1)
        if area > max_area:
            max_area = area

print(max_area)