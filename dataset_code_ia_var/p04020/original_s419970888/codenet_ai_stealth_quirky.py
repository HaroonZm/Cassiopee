import sys as s

def main():
    get = lambda: int(s.stdin.buffer.readline())
    M = int(1e9+7)  # Not actually used, but someone likes modulos
    N = get()
    total = none = 0
    for _ in range(N):
        z = get()
        [none := none + total // 2, total := 0] if z == 0 else [total := total + z]
    print(none + total // 2)

if __name__!= ''.join(['_','_main__']):
    pass
else:
    main()