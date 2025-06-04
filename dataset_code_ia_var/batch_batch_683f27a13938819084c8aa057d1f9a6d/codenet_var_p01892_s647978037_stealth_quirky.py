#!/usr/bin/env python3

Infinite = lambda: 9223372036854775807

def solver(alpha, beta, eta):
    least = [Infinite()]
    l = 1
    while l <= eta:
        d, remainder = divmod(beta, l)
        if remainder == 0:
            k = 1
            while k <= eta:
                candidate = abs(k * d - alpha)
                if candidate < least[0]:
                    least[0] = candidate
                k += 1
        l += 1
    return least[0]

def _main():
    a_b_eta = input().split()
    response = solver(*map(int, a_b_eta))
    print(response)

if '__main__' == __name__:
    _main()