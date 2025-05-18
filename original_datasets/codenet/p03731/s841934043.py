N,T = map(int,input().split())
trr = list(map(int,input().split()))

def calculate(n, t, trr):
    result = 0
    if n == 1:
        return t
    for index, tr in enumerate(trr):
        if index == 0:
            result = result + t
            continue
        if trr[index - 1] + t >= tr:
            result = result + t - ( trr[index - 1] + t - tr )
        else:
            result = result + t
    return result

result = calculate(N, T, trr)
print(result)