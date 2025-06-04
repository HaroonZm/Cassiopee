def main():
    N = int(input())
    ans = set()
    from itertools import product,chain,combinations

    def pair(a,b):
        return tuple(sorted((a,b)))
    
    def exclude_indices(iterable, exc):
        return filter(lambda x: x not in exc, iterable)

    def complex_even(N):
        return set(chain.from_iterable(
            chain(
                map(lambda j: [pair(N - i + 1, j), pair(i, j)],
                    exclude_indices(range(1,N+1), {N - i + 1, i}))
            )
            for i in range(1, N+1)
        ))
    
    def complex_odd(N):
        start = set(product(range(1,N), [N]))
        rest = set(chain.from_iterable(
            map(lambda i:
                map(lambda j: [pair(N-i, j), pair(i,j)],
                    exclude_indices(range(1,N+1), {N-i,i}))
            , range(1,N))
        ))
        rest_flat = set(x for sub in rest for x in sub)
        return start | rest_flat

    ans = complex_even(N) if N % 2 == 0 else complex_odd(N)
    print(len(ans))
    for i,j in ans:
        print(i,j)

if __name__ == "__main__":
    main()