import math
def main():
    n = int(input())
    r = list(map(float, input().split()))
    x = [0.0]*n
    for i in range(1,n):
        dist = 0.0
        for j in range(i-1,-1,-1):
            dx = math.sqrt((r[i]+r[j])**2 - (r[i]-r[j])**2)
            dist = max(dist, x[j]+dx)
        x[i] = dist
    left = min(x[i]-r[i] for i in range(n))
    right = max(x[i]+r[i] for i in range(n))
    print("{:.8f}".format(right-left))
main()