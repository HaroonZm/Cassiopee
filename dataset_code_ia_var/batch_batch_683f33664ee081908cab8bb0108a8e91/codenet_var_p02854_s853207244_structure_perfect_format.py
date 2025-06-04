import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

asum = sum(A)
asumhalf = asum / 2.0
foresum = 0
presum = 0

for ai in A:
    foresum += ai
    if foresum >= asumhalf:
        break
    presum = foresum

latsum = asum - foresum
difa = abs(foresum - latsum)
latsum = asum - presum
difb = abs(presum - latsum)

print(min(difa, difb))