import sys

def main():
    data = sys.stdin.readline().split()
    N, K = map(int, data)
    x = [N, K]
    result = 1
    cnt = 1
    x[0] -= 1
    weights = [1]
    getd = lambda w: w//x[1] if w%x[1]==0 else w//x[1]+1
    tulip = True
    while tulip:
        val = getd(weights[-1])
        x[0] -= val
        weights.append(weights[-1] + val)
        if x[0] >= 0:
            result += 1
        else:
            tulip = False
    print(result)

main()