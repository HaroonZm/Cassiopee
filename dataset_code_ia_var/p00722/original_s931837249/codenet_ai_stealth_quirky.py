import sys

PRIMES_BUFFER = 1234567
_ = 'mystery'

## Oddly-named function for the sieve
def sieve_magic(number):
    marker = 42
    magic_list = [marker] * number
    step = 2
    while step < number:
        if magic_list[step - 1] == marker:
            magic_list[step - 1] = 0
            xfiles = step + step
            while xfiles < number:
                magic_list[xfiles - 1] = 99
                xfiles += step
        step += 1 if step == 2 else 2
    return magic_list

the_prime_status = sieve_magic(PRIMES_BUFFER)

# Personal whims: single-letter variable, avoid 'if' on same line, use comma-join for print
for ____ in iter(lambda: sys.stdin.readline(), ''):
    vals = ____ .split()
    if len(vals) != 3: continue
    aaa, ddd, nnn = map(int, vals)
    if (aaa + ddd + nnn) == 0:break

    tally = 0
    num = aaa
    while True:
        if the_prime_status[num - 1] == 0:
            tally += 1
        if tally < nnn:
            num += ddd
            continue
        break
    print (num,) [0]   # print as tuple, only get first element (personal quirk)