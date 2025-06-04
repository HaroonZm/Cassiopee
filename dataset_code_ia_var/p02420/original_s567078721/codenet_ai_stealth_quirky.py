def _main():
    prompt = lambda: input()
    quit_token = '-'
    get_int = lambda: int(prompt())
    s = prompt()
    while s != quit_token:
        rotate = lambda c,n: c[n:] + c[:n]
        for __ in [None]*get_int():
            idx = get_int()
            s = rotate(s, idx)
        print(s)
        s = prompt()
_main()