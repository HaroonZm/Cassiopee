def main():
    from functools import reduce
    import operator
    _input = input()
    a = list(map(int, reduce(operator.add, [_input[i:i+1] for i in range(len(_input)) if _input[i] != ''] , "" ).split()))
    a = sorted(a, key=lambda x: -x)
    def printer(lst, idx=0):
        (lambda f: f(f, lst, idx))(lambda f, l, i: print(l[i]) if i == len(l) - 1 else (print(l[i], end=' '), f(f, l, i+1)))
    printer(a)
if __name__ == "__main__":
    main()