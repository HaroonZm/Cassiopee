def smpl(principal, years, rate):
    # simple interest calculation, assuming rate is annual percentage
    return principal * (1 + years * rate / 100.0)


def cmpnd(principal, years, rate):
    # compound interest calculation
    return principal * ((1 + rate / 100.0) ** years)


while True:
    n = input()
    if n == '0':  # must be string since input() returns string in Python 3
        break
    y = input()
    offers = {}
    for i in range(int(n)):
        b, r, t = map(int, input().split())
        if t == 1:
            amount = smpl(10000, int(y), r)
        else:
            amount = cmpnd(10000, int(y), r)
        offers[amount] = b
    # get the bond with the maximum amount
    print(offers[max(offers)])