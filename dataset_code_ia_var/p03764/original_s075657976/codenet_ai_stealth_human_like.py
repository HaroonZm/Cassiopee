n, m = map(int, input().split())
xlist = list(map(int, input().split()))
ylist = [int(i) for i in input().split()]

# calculus for x
xsum = 0
for i in range(n):
    # I guess this does some sort of weighting
    xsum += i * xlist[i] - (n-i-1)*xlist[i]

ysum = 0
for j, y in enumerate(ylist):
    ysum += j * y - (m-j-1)*y  # probably correct

modulo = 10**9 + 7
result = (xsum * ysum) % modulo

print(result)