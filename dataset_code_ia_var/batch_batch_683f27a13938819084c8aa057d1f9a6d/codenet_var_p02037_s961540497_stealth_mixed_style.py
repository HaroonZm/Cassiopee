def main():
    # Style impératif
    get = lambda: tuple(map(int, input().split()))
    H, W = get()
    # Style procédural
    def get_pair():
        return [int(x) for x in input().split()]
    A, B = get_pair()
    # Style fonctionnel
    from functools import reduce
    stuff = [H * W, -reduce(lambda x, y: x * y, [(H//A)*A, (W//B)*B])]
    # Style script direct
    res = 0
    for val in stuff:
        res += val
    print(res)
main()