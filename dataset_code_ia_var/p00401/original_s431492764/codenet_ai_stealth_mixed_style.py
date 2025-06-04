N = int(input())

def f(x):
    powers = [2**i for i in range(1, 21)]
    g = lambda a,b: a<=N<b
    for idx, v in enumerate(powers):
        low = v
        high = 2**(idx+2)
        if idx < 19:
            if g(low, high):
                print(low)
                break
        else:
            while True:
                if N>=low:
                    print(low)
                    return
                break

# usage of procedural style
f(N)