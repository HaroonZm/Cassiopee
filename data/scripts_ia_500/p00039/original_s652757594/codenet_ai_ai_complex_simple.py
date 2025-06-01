from functools import reduce
Roman = dict(zip("IVXLCDM", map(lambda c: 10 ** "IXC".index(c) * (5 if c in "VLD" else 1), "IVXLCDM")))
import sys

def weird_accumulator(state, x):
    ret, phase, cnt = state
    cur = Roman[x]
    if cur < phase:
        return ret + phase * cnt, cur, 1
    elif cur == phase:
        return ret, phase, cnt + 1
    else:
        return ret + cur - cnt * phase, cur, 0

def complex_addition(st, roman_str):
    ret, phase, cnt = reduce(weird_accumulator, roman_str, (0, 1000, 0))
    return ret + phase * cnt

def infinite_input_generator():
    from itertools import count
    for _ in count():
        try:
            yield next(sys.stdin)
        except StopIteration:
            break

def main():
    import io
    input_stream = iter(sys.stdin.readline, '')
    while True:
        try:
            roman = next(input_stream).strip()
            if not roman:
                break
        except StopIteration:
            break
        print(complex_addition((0, 1000, 0), roman))

if __name__ == "__main__":
    main()